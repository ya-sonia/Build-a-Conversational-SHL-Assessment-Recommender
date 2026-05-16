"""
catalog.py
SHL Individual Test Solutions catalog.
Source: https://www.shl.com/solutions/products/product-catalog/ (type=1, Individual Test Solutions only)
Pre-packaged Job Solutions are excluded per the assignment spec.
"""

CATALOG = [
    # ── COGNITIVE / ABILITY  (test_type A) ────────────────────────────────────
    {
        "name": "Verify - Numerical Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-numerical-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures the ability to make correct decisions or inferences from numerical or "
            "statistical data, including graphs, tables, and financial data. "
            "18 minutes, 18 items. Relevant for analytical and finance roles."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["numerical", "number", "math", "statistics", "finance", "quantitative",
                     "data analysis", "analyst"],
    },
    {
        "name": "Verify - Verbal Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-verbal-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses the ability to understand and evaluate written information, reading "
            "comprehension and drawing logical conclusions from text. 19 minutes, 30 items. "
            "Suitable for communication, writing, and analytical roles."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales", "Customer Service"],
        "keywords": ["verbal", "reading", "comprehension", "language", "writing",
                     "communication", "text"],
    },
    {
        "name": "Verify - Inductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-inductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures the ability to identify patterns and rules to solve novel problems. "
            "Relevant for roles dealing with new concepts, strategy, and complex ambiguous "
            "problems. 25 minutes."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology"],
        "keywords": ["inductive", "patterns", "abstract", "reasoning", "problem solving",
                     "innovative", "strategy"],
    },
    {
        "name": "Verify - Deductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-deductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures the ability to draw logical conclusions from information, evaluate "
            "arguments, and complete scenarios using incomplete data. 18 minutes, 20 items. "
            "Relevant for engineers, analysts, and decision-makers."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor", "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology"],
        "keywords": ["deductive", "logical", "reasoning", "logic", "critical thinking",
                     "conclusions", "arguments"],
    },
    {
        "name": "Verify G+",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-g-plus/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": True,
        "description": (
            "General cognitive ability test combining Numerical, Inductive, and Deductive "
            "Reasoning in one adaptive assessment. 36 minutes, 30 items. Adaptive difficulty. "
            "Appropriate for all levels; best for roles requiring broad cognitive skills."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor", "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["general ability", "cognitive", "g+", "aptitude", "intelligence",
                     "reasoning", "adaptive"],
    },
    {
        "name": "Verify Interactive G+",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/shl-verify-interactive-g/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": True,
        "description": (
            "Mobile-first interactive version of Verify G+. Combines Deductive, Inductive, and "
            "Numerical Reasoning. 36 minutes, 24 items. Provides general ability score plus "
            "three sub-scores. Suitable for all job levels."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor", "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["interactive", "general ability", "cognitive", "mobile", "g+",
                     "aptitude", "adaptive"],
    },
    {
        "name": "Verify Interactive - Deductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-deductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": True,
        "description": (
            "Mobile-first interactive deductive reasoning assessment. Measures logical thinking "
            "and the ability to draw sound conclusions from data. Suitable for manager "
            "and above levels."
        ),
        "job_levels": ["Graduate", "Manager", "Front Line Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology"],
        "keywords": ["interactive", "deductive", "logical", "mobile", "manager",
                     "reasoning", "adaptive"],
    },
    {
        "name": "Verify - Mechanical Comprehension",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-mechanical-comprehension/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures understanding of mechanical and physical principles. Relevant for "
            "engineering, manufacturing, technical, and maintenance roles."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["mechanical", "engineering", "technical", "physics", "maintenance",
                     "industrial", "manufacturing"],
    },
    {
        "name": "Verify - Calculation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-calculation/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests basic numerical calculation skills — arithmetic, percentages, and "
            "order of operations — without a calculator. Suitable for clerical and "
            "customer service roles requiring numeric accuracy."
        ),
        "job_levels": ["Entry-Level", "General Population", "Supervisor"],
        "job_families": ["Clerical", "Customer Service", "Contact Center"],
        "keywords": ["calculation", "arithmetic", "math", "numeric", "clerical",
                     "numbers", "basic math"],
    },
    {
        "name": "Verify - Reading Comprehension",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-reading-comprehension/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses ability to read and understand written information relevant to the job. "
            "Suitable for supervisory, operator, and customer service roles requiring "
            "practical comprehension."
        ),
        "job_levels": ["Entry-Level", "General Population", "Supervisor"],
        "job_families": ["Clerical", "Customer Service", "Contact Center"],
        "keywords": ["reading", "comprehension", "text", "understanding", "supervisor",
                     "operator", "practical"],
    },
    {
        "name": "Verify - Checking",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-checking/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures the ability to identify errors in data by comparing tables and "
            "spotting discrepancies. Relevant for data entry, administrative, and "
            "quality-control roles."
        ),
        "job_levels": ["Entry-Level", "General Population", "Supervisor"],
        "job_families": ["Clerical", "Customer Service"],
        "keywords": ["checking", "error detection", "data entry", "accuracy",
                     "clerical", "quality", "admin"],
    },
    {
        "name": "Verify - Numerical Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-numerical-ability/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Next-generation numerical ability test measuring ability to derive numerical "
            "problems from written descriptions, calculate answers, and work with numerical "
            "data in realistic workplace contexts. 20 minutes, 16 items."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["numerical ability", "workplace numeracy", "numbers", "calculation",
                     "math", "data"],
    },
    {
        "name": "General Ability Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/general-ability-assessment/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Entry-level cognitive ability assessment covering numerical, verbal, and abstract "
            "reasoning at general population level. Designed for non-professional and "
            "frontline roles."
        ),
        "job_levels": ["Entry-Level", "General Population"],
        "job_families": ["Clerical", "Customer Service", "Contact Center"],
        "keywords": ["general ability", "entry level", "frontline", "operational",
                     "reasoning", "basic cognitive"],
    },
    {
        "name": "Graduate 8.0 Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/graduate-8-0-solution/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive": True,
        "description": (
            "Designed for graduate-level hiring, combining cognitive ability and behavioural "
            "measurement. Assesses potential for high performance in professional roles. "
            "Suitable for campus and early career programmes."
        ),
        "job_levels": ["Graduate", "Entry-Level"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["graduate", "early career", "entry level", "campus", "potential",
                     "trainee", "fresh graduate"],
    },

    # ── PERSONALITY & BEHAVIOUR  (test_type P) ────────────────────────────────
    {
        "name": "OPQ32r",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32r/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "SHL's flagship Occupational Personality Questionnaire. Assesses 32 specific "
            "personality characteristics across three domains: Relationships with People, "
            "Thinking Styles, and Feelings & Emotions. 104 forced-choice items, ~25 minutes. "
            "Used for hiring, development, and succession."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Front Line Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales", "Customer Service"],
        "keywords": ["personality", "behaviour", "OPQ", "OPQ32r", "occupational",
                     "traits", "culture fit", "leadership", "soft skills"],
    },
    {
        "name": "OPQ32",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Rating-scale version of the Occupational Personality Questionnaire. Measures "
            "the same 32 work-relevant personality traits as OPQ32r using a Likert-style "
            "format. Suitable for all professional levels."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["personality", "OPQ", "OPQ32", "occupational", "traits",
                     "rating scale", "likert"],
    },
    {
        "name": "Motivational Questionnaire (MQ)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/motivational-questionnaire-mq/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses 18 motivational dimensions — what drives and engages an individual at "
            "work, including achievement, autonomy, commercial outlook, and teamwork. "
            "Used for hiring, onboarding, development, and retention. Untimed, ~25 minutes."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["motivation", "engagement", "values", "culture fit", "retention",
                     "MQ", "drive", "what motivates"],
    },
    {
        "name": "RemoteWorkQ",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/remoteworkq/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures personality traits and work preferences critical for success in remote "
            "and hybrid work environments: self-discipline, digital communication, "
            "collaboration, and adaptability."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor", "Manager"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["remote work", "hybrid", "work from home", "digital", "self-discipline",
                     "collaboration", "remote"],
    },
    {
        "name": "Personality based Emotional Intelligence (EIP3)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/personality-based-emotional-intelligence-eip3/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures emotional intelligence traits: self-awareness, empathy, motivation, "
            "and social skills. Used for leadership development, coaching, and high-potential "
            "identification programmes."
        ),
        "job_levels": ["Mid-Professional", "Manager", "Front Line Manager",
                       "Director", "Executive"],
        "job_families": ["Business", "Sales"],
        "keywords": ["emotional intelligence", "EQ", "EI", "empathy", "leadership",
                     "social skills", "self-awareness", "coaching"],
    },
    {
        "name": "Occupational Personality Questionnaire (OPQ) Short",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq-short/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "A shorter OPQ providing key personality insights with reduced candidate burden. "
            "Suitable for high-volume screening where a full OPQ is not feasible."
        ),
        "job_levels": ["Entry-Level", "General Population", "Graduate"],
        "job_families": ["Business", "Customer Service", "Contact Center"],
        "keywords": ["personality", "OPQ", "short", "screening", "high volume",
                     "quick", "traits"],
    },

    # ── BEHAVIOURAL / SITUATIONAL JUDGEMENT  (test_type B) ───────────────────
    {
        "name": "Situational Judgement Test (SJT)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/situational-judgement-test/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Scenario-based assessment presenting realistic workplace situations. Tests "
            "judgement and decision-making in context. Available for various roles and "
            "levels; can be used off-the-shelf or customised."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Manager", "Front Line Manager"],
        "job_families": ["Business", "Sales", "Customer Service", "Contact Center"],
        "keywords": ["situational judgement", "SJT", "scenarios", "decision making",
                     "judgement", "job simulation", "workplace situations"],
    },
    {
        "name": "Sales Achievement Predictor",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sales-achievement-predictor/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Behavioural assessment specifically for sales roles. Measures critical "
            "competencies: prospecting, persuasion, relationship building, and resilience "
            "under rejection."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Sales"],
        "keywords": ["sales", "achievement", "persuasion", "prospecting",
                     "business development", "account management", "resilience"],
    },
    {
        "name": "Customer Contact Styles Questionnaire",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/customer-contact-styles-questionnaire/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses preferred styles of interacting with customers. Identifies individuals "
            "likely to provide excellent customer experience and handle difficult situations "
            "professionally."
        ),
        "job_levels": ["Entry-Level", "General Population"],
        "job_families": ["Customer Service", "Contact Center"],
        "keywords": ["customer service", "contact center", "customer interaction",
                     "soft skills", "customer experience"],
    },
    {
        "name": "Dependability & Safety Instrument",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/dependability-safety-instrument/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures behavioural tendencies related to reliability, integrity, and safe "
            "working practices. Used for screening in safety-sensitive industries: "
            "manufacturing, oil & gas, logistics."
        ),
        "job_levels": ["Entry-Level", "General Population"],
        "job_families": ["Safety"],
        "keywords": ["safety", "dependability", "integrity", "manufacturing",
                     "oil and gas", "reliability", "safety-sensitive"],
    },
    {
        "name": "Workplace English Language Test (WELT)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/workplace-english-language-test/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures English language proficiency for workplace communication including "
            "reading, listening, and grammar. For contact center, BPO, customer service, "
            "and any role requiring English communication."
        ),
        "job_levels": ["Entry-Level", "General Population"],
        "job_families": ["Contact Center", "Customer Service", "Clerical"],
        "keywords": ["english", "language", "communication", "BPO", "contact center",
                     "customer service", "grammar", "proficiency"],
    },
    {
        "name": "Smart Interview On Demand",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/smart-interview-on-demand/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "AI-powered asynchronous video interview platform. Candidates record video "
            "responses to structured questions at their convenience. Provides scoring and "
            "structured insights for hiring teams."
        ),
        "job_levels": ["Entry-Level", "Graduate", "Mid-Professional",
                       "Professional Individual Contributor", "Manager"],
        "job_families": ["Business", "Information Technology", "Sales",
                         "Customer Service", "Contact Center"],
        "keywords": ["interview", "video interview", "structured interview",
                     "screening", "AI interview", "on demand"],
    },

    # ── KNOWLEDGE & SKILLS  (test_type K) ────────────────────────────────────
    {
        "name": "Java (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/java-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests Java programming fundamentals: OOP, data structures, exceptions, "
            "collections, and core APIs. For software developers, engineers, and IT "
            "professionals."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["java", "programming", "software development", "coding",
                     "developer", "OOP", "backend", "J2EE"],
    },
    {
        "name": "Core Java (Entry Level)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/core-java-entry-level/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests foundational Java knowledge for entry-level developers. Covers basic "
            "OOP concepts, syntax, data types, and standard Java APIs."
        ),
        "job_levels": ["Entry-Level", "Graduate"],
        "job_families": ["Information Technology"],
        "keywords": ["java", "entry level", "junior", "programming", "basics",
                     "developer", "fresher"],
    },
    {
        "name": "Python (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests Python programming: syntax, data types, libraries, file handling, and "
            "OOP. Used for data science, software development, and automation roles."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["python", "programming", "data science", "scripting", "automation",
                     "developer", "machine learning", "AI"],
    },
    {
        "name": "JavaScript (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/javascript-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses JavaScript proficiency: ES6+, DOM manipulation, async programming, "
            "and common patterns. For front-end, full-stack, and web developers."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["javascript", "js", "frontend", "web development", "node",
                     "react", "full stack", "typescript"],
    },
    {
        "name": "SQL (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sql-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests SQL: queries, joins, aggregations, subqueries, and database concepts. "
            "Relevant for data analysts, DBAs, backend developers, and BI roles."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["SQL", "database", "data analyst", "queries", "DBA",
                     "backend", "BI", "analytics", "relational"],
    },
    {
        "name": ".NET Framework 4.5 (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/net-framework-4-5-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Assesses .NET framework knowledge including C#, ASP.NET, and core libraries. "
            "Relevant for enterprise software developers in Microsoft ecosystems."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": [".net", "C#", "dotnet", "ASP.NET", "microsoft",
                     "enterprise", "software developer"],
    },
    {
        "name": "Manual Testing (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/manual-testing-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Evaluates knowledge of software testing principles, test case design, defect "
            "reporting, and QA methodologies. For QA engineers and software testers."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["testing", "QA", "quality assurance", "test cases",
                     "software testing", "defects", "JIRA"],
    },
    {
        "name": "Automata - Fix (Coding Simulation)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-fix/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Coding simulation where candidates debug and fix broken code in a realistic "
            "IDE environment. Assesses debugging skills across multiple languages. "
            "Highly relevant for software engineering roles."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["coding", "debugging", "simulation", "software engineer",
                     "programming", "developer", "IDE", "fix bugs"],
    },
    {
        "name": "Automata Pro (Coding Simulation)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-pro/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Full IDE coding simulation: write and run code to solve algorithmic problems. "
            "Tests algorithmic thinking, data structures, and problem-solving. "
            "For mid-to-senior software engineering roles."
        ),
        "job_levels": ["Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["coding", "algorithms", "data structures", "simulation",
                     "software engineer", "senior developer", "full stack"],
    },
    {
        "name": "Technology Professional 8.0 Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/technology-professional-8-0-solution/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Comprehensive assessment for technology professionals combining cognitive ability, "
            "personality, and skills. Designed for mid-to-senior IT roles: analysts, "
            "architects, and project managers."
        ),
        "job_levels": ["Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Information Technology"],
        "keywords": ["technology", "IT", "software", "analyst", "architect",
                     "tech professional", "project manager"],
    },
    {
        "name": "Agile Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/agile-assessment/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Measures knowledge of Agile methodologies: Scrum, Kanban, Lean. Tests "
            "understanding of sprints, ceremonies, backlog management, and Agile principles. "
            "For product managers, developers, and scrum masters."
        ),
        "job_levels": ["Mid-Professional", "Professional Individual Contributor", "Manager"],
        "job_families": ["Information Technology", "Business"],
        "keywords": ["agile", "scrum", "kanban", "product manager", "scrum master",
                     "sprint", "lean", "SDLC"],
    },
    {
        "name": "Microsoft Excel (Office 365)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/microsoft-excel-office-365/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Tests Excel skills: formulas, pivot tables, data analysis, and spreadsheet "
            "management. For business analysts, financial professionals, and any role "
            "requiring advanced spreadsheet skills."
        ),
        "job_levels": ["Entry-Level", "Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Business", "Clerical"],
        "keywords": ["excel", "spreadsheet", "microsoft", "data", "office",
                     "business analyst", "finance", "pivot tables"],
    },
    {
        "name": "Business Analyst Skills Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/business-analyst-skills/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Comprehensive skills test for business analyst roles: requirements gathering, "
            "process modelling, stakeholder management, and data interpretation."
        ),
        "job_levels": ["Mid-Professional", "Professional Individual Contributor"],
        "job_families": ["Business", "Information Technology"],
        "keywords": ["business analyst", "BA", "requirements", "stakeholder",
                     "process", "analysis", "BPMN"],
    },

    # ── SIMULATIONS  (test_type S) ────────────────────────────────────────────
    {
        "name": "Multitasking Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/multitasking-ability/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Split-screen simulation measuring ability to manage multiple tasks simultaneously "
            "while handling email interruptions. Relevant for roles with high task-switching "
            "demands: managers, contact center staff, and administrative professionals."
        ),
        "job_levels": ["Entry-Level", "Front Line Manager", "Manager", "Mid-Professional",
                       "Professional Individual Contributor", "Director", "Executive"],
        "job_families": ["Business", "Contact Center", "Customer Service"],
        "keywords": ["multitasking", "attention", "multi-task", "manager",
                     "busy environment", "contact center", "juggling tasks"],
    },
    {
        "name": "Contact Center Simulation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/customer-service-phone-solution/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Simulates real contact center interactions. Tests a candidate's ability to "
            "listen, resolve customer issues, navigate systems, and enter data accurately. "
            "Part of the Customer Service Phone Solution."
        ),
        "job_levels": ["Entry-Level", "General Population"],
        "job_families": ["Contact Center", "Customer Service"],
        "keywords": ["contact center", "call center", "customer service", "simulation",
                     "BPO", "phone support", "inbound"],
    },

    # ── COMPETENCIES / 360  (test_type C / D) ────────────────────────────────
    {
        "name": "Universal Competency Framework (UCF)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/universal-competency-framework/",
        "test_type": "C",
        "remote_testing": True,
        "adaptive": False,
        "description": (
            "Standardised competency framework with 8 universal competencies and 20 dimensions. "
            "Used as a foundation for job profiling, assessment design, and linking personality "
            "data to job performance requirements across all levels."
        ),
        "job_levels": ["Graduate", "Mid-Professional", "Professional Individual Contributor",
                       "Manager", "Director", "Executive"],
        "job_families": ["Business", "Information Technology", "Sales"],
        "keywords": ["competency", "framework", "UCF", "job profile", "leadership",
                     "development", "succession"],
    },
]

# ── Utility helpers ────────────────────────────────────────────────────────────
CATALOG_URL_SET = {item["url"] for item in CATALOG}
CATALOG_BY_NAME = {item["name"].lower(): item for item in CATALOG}


def search_catalog(query: str, top_k: int = 10) -> list:
    """Keyword-overlap search. Returns top_k scored catalog items."""
    import re
    tokens = set(t for t in re.split(r'\W+', query.lower()) if len(t) > 2)
    scored = []
    for item in CATALOG:
        score = 0
        # Name match (highest weight)
        for t in tokens:
            if t in item["name"].lower():
                score += 4
        # Keyword match
        for kw in item["keywords"]:
            kw_tokens = set(re.split(r'\W+', kw.lower()))
            if kw_tokens & tokens:
                score += 2
        # Description match
        for t in tokens:
            if t in item["description"].lower():
                score += 1
        if score > 0:
            scored.append((score, item))
    scored.sort(key=lambda x: -x[0])
    return [item for _, item in scored[:top_k]]


if __name__ == "__main__":
    print(f"Catalog size: {len(CATALOG)} items")
    print("\nSearch 'java developer stakeholder':")
    for r in search_catalog("java developer stakeholder"):
        print(f"  {r['name']} [{r['test_type']}]")