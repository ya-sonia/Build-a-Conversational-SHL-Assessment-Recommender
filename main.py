"""
main.py
FastAPI service — SHL Assessment Recommender
Endpoints:
  GET  /health  →  {"status": "ok"}
  POST /chat    →  ChatResponse
"""

import time
from typing import Literal

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, field_validator, model_validator
import agent

app = FastAPI(
    title="SHL Assessment Recommender",
    description="Conversational agent for recommending SHL Individual Test Solutions.",
    version="1.0.0",
)


# ── Request / Response models ──────────────────────────────────────────────────
class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str

    @field_validator("content")
    @classmethod
    def content_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("content must not be blank")
        return v.strip()


class ChatRequest(BaseModel):
    messages: list[Message]

    @field_validator("messages")
    @classmethod
    def validate_messages(cls, v: list[Message]) -> list[Message]:
        if len(v) == 0:
            raise ValueError("messages must be a non-empty list")
        if len(v) > 8:
            raise ValueError("messages list exceeds 8-turn limit")
        if v[0].role != "user":
            raise ValueError("First message must have role 'user'")
        for i in range(1, len(v)):
            if v[i].role == v[i - 1].role:
                raise ValueError(
                    f"Messages must alternate roles (conflict at index {i})"
                )
        return v


class Recommendation(BaseModel):
    name: str
    url: str
    test_type: str


class ChatResponse(BaseModel):
    reply: str
    recommendations: list[Recommendation]
    end_of_conversation: bool


# ── Middleware: response timing ────────────────────────────────────────────────
@app.middleware("http")
async def add_response_time(request: Request, call_next):
    t0 = time.time()
    response = await call_next(request)
    response.headers["X-Response-Time"] = f"{round(time.time() - t0, 3)}s"
    return response


# ── Custom validation error handler (returns clean JSON, not FastAPI default) ──
@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    # Extract the first human-readable error message
    errors = exc.errors()
    msg = errors[0]["msg"] if errors else "Validation error"
    return JSONResponse(status_code=422, content={"error": msg})


# ── Endpoints ──────────────────────────────────────────────────────────────────
@app.get("/health", summary="Readiness check")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse, summary="Conversational assessment recommender")
def chat(body: ChatRequest):
    messages = [{"role": m.role, "content": m.content} for m in body.messages]

    result = agent.chat(messages)

    return ChatResponse(
        reply=result["reply"],
        recommendations=[
            Recommendation(
                name=r["name"],
                url=r["url"],
                test_type=r["test_type"],
            )
            for r in result.get("recommendations", [])
        ],
        end_of_conversation=result.get("end_of_conversation", False),
    )


# ── Run directly ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import os
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        reload=False,
    )