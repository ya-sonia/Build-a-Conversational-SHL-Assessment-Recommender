
# SHL Assessment Recommender

A conversational AI agent that helps hiring managers choose the right SHL assessments based on job requirements.

---

## Features
- Chat-based assessment recommendations  
- Suggests 1–10 SHL tests  
- Asks clarifying questions if needed  
- Supports follow-up improvements  
- Works with Ollama (local) or Groq (cloud)  

---

## Project Structure
```
shl_recommender/
├── catalog.py        
├── agent.py          
├── main.py           
├── tests/
│   └── test_app.py   
├── requirements.txt
├── Dockerfile
└── .env.example
```  

---

## Setup

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run Ollama (optional)
```bash
ollama pull llama3.2:3b
ollama serve
```


### Start server
```bash
python main.py
```

## API

### Health Check
```bash
GET /health

```

### Chat Endpoint
```bash
POST /chat

```

### Example Request
```json
{
  "messages": [
    { "role": "user", "content": "Hiring a Python developer" }
  ]
}

```

### Testing

```bash

python -m unittest tests/test_app.py -v
```


## Deployment 

1. Get a free Groq API key at [console.groq.com](https://console.groq.com)
2. Push this repo to GitHub
3. Create a Web Service pointing at the repo
4. Set env var: `GROQ_API_KEY=gsk_...`
5. Start command: `gunicorn main:app --bind 0.0.0.0:$PORT --workers 2 --timeout 60`
6. Health check path: `/health`

