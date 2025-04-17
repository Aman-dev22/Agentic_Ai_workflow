# LangGraph-Driven AI Workflow for FastAPI Project Generation

This project builds an intelligent system that takes a Software Requirements Specification (SRS) document as input, analyzes it using LangGraph, and generates a production-ready FastAPI backend. The system uses large language models (LLMs) and agentic workflows to automate analysis, code generation, testing, debugging, documentation, and deployment.

---

## 🚀 Features

- 📄 **SRS-Driven Development** – Parses structured SRS input to extract API endpoints, business logic, and database schema.
- 🧠 **LangGraph AI Workflow** – Uses nodes, agents, and tools to model the software development lifecycle.
- 🧪 **Test-Driven Development** – Generates unit tests before code using LLMs and executes with `pytest`.
- 🐞 **Autonomous Debugging** – Refines failing or buggy code iteratively.
- 🛠️ **Modular FastAPI Generation** – Produces a scalable folder structure with API routes, models, services, and config.
- 🖼️ **Graph Visualization** – Visualizes workflow with tools like Graphviz or Mermaid.
- 📝 **Comprehensive Documentation** – Auto-generates `README.md` and API usage guide.
- 📦 **Optional Deployment** – Can zip and deploy the generated project.
- 📊 **LangSmith Integration** – Tracks execution, responses, and logs for debugging and audit.


## 🛠️ Tech Stack

- 🐍 Python
- ⚡ FastAPI
- 🧪 Pytest
- 🔗 LangGraph
- 🧠 LLMs (e.g., LLaMA 3, Groq, OpenAI)
- 📊 LangSmith (for logs & debugging)
- 📈 Graphviz / Mermaid (visualization)

---

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
cp .env.example .env  # Fill in your .env values

# 5. Run FastAPI server
uvicorn app.main:app --reload

#6 Run agentic Ai workflow
py agentic.py
```

---

## 🧪 Usage

1. Upload a `.docx` SRS file via the FastAPI endpoint.
2. The system:
   - Parses the doc
   - Generates and tests FastAPI code
   - Logs the process via LangSmith
   - Returns a zip of the working backend project

3. Optionally, use the dynamic agent endpoint to generate new task-specific agents from PDF knowledge.

---

## 📊 LangSmith Logs

LangSmith tracks:

- Graph execution steps
- LLM calls and outputs
- API routes, failures, and debugging info
- Iterative refinements



## 👨‍💻 Author

Made with ❤️ using LangGraph, LLMs, and FastAPI  
Contributor: [Aman Purohit / GitHub URL]

---

## 📄 License

[MIT](LICENSE)
