# Devops_CI-CD_pipeline
Optimize CI/CD YAML pipelines using LLM! React + Flask + FastAPI app that detects issues and suggests improvements with Hugging Face AI.


# 🚀 DevOps Assistant for CI/CD Pipeline Optimization

A smart assistant that **analyzes and optimizes CI/CD pipelines** using Large Language Models (LLMs). This tool detects **bottlenecks**, suggests **improvements**, and implements **optimizations** to reduce **build time** and **resource consumption** in DevOps workflows.

---

## 🧠 What It Does

- ✅ Accepts CI/CD YAML files via **upload or URL**
- 🔍 Analyzes pipeline structure and detects inefficiencies
- 💡 Suggests modern practices, parallelization, caching, and syntax improvements
- 🤖 Uses **LLM (Hugging Face + LangChain)** to generate optimized pipeline code
- 📉 Aims to reduce build duration and cloud compute costs

---

## 🛠 Tech Stack

| Layer       | Technology                            |
|-------------|----------------------------------------|
| Frontend    | React.js                              |
| Backend     | FastAPI + Flask                       |
| Language AI | LangChain + Hugging Face (open source)|
| Language    | Python                                |
| DevOps      | CI/CD YAML, GitHub Actions, etc.      |

```

## 📂 Project Structure

devops-assistant/
Devops_CI-CD_pipeline/
├── Backend/
│ ├── pycache/
│ ├── models/
│ │ ├── pycache/
│ │ └── llm_helper.py # Handles Hugging Face model logic
│ ├── services/
│ │ ├── pycache/
│ │ ├── analyzer.py # Analyzes CI/CD YAML files
│ │ └── parser.py # YAML file parser
│ ├── uploads/ # Stores uploaded pipeline files
│ ├── utils/
│ │ └── file_utils.py # Utility functions for file handling
│ ├── main.py # FastAPI entry point
│ └── requirements.txt # Python dependencies
│
├── Frontend/
│ ├── node_modules/ # React dependencies
│ ├── public/
│ │ └── devops.png # Frontend image asset
│ ├── src/
│ │ ├── assets/ # Additional static assets
│ │ ├── components/
│ │ │ └── PipelineAnalyzer.jsx # UI component for analysis
│ │ ├── services/
│ │ │ └── api.jsx # Frontend API service functions
│ │ ├── App.css
│ │ ├── App.jsx # Main React component
│ │ ├── index.css
│ │ └── main.jsx # Entry point for React app
│ ├── .gitignore # Git ignore rules
│ └── eslint.config.js # ESLint configuratio

```

## ⚙️ Installation

### 🔧 Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
The backend runs at: http://localhost:8000

🌐 Frontend Setup
```
cd frontend
npm install
npm run dev
```
The frontend runs at: http://localhost:3000

📤 Usage
Launch both backend and frontend

In the web UI:

Upload a .yaml pipeline file or

Paste a public URL to a CI/CD YAML file

Click "Analyze" to:

View detected issues

Get AI-powered optimization suggestions

Click "Download" or "Copy" the optimized pipeline

🔒 Notes
Keep your .env file (containing HF_TOKEN) out of version control

backend/.env

🚀 Future Improvements
 Support for GitLab CI, Jenkins, CircleCI, etc.

 GitHub Action integration for auto-analysis on pull requests

 Visual timeline for bottleneck locations

 Model fine-tuning with user feedback

📄 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Created by S Shivaprasad
📧 Email: shivaprasad20005@gmail.com

