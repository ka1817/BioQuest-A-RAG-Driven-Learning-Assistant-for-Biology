# BioQuest: A RAG-Driven Learning Assistant for Biology

BioQuest is a Retrieval-Augmented Generation (RAG) based intelligent learning assistant designed to help students and teachers explore biology concepts from 9th and 10th grade textbooks. It leverages modern LLM capabilities to provide context-aware answers and explanations, making learning interactive and accessible.

## 🚀 Features
- **RAG Pipeline** using LangChain
- **Custom embedding generation** and storage with FAISS
- **LLM-powered answers** using `llama-3.3-70b-versatile` via GROQ API
- **Cross Encoder Re-ranking** for improved relevance
- **Streamlit frontend** for a user-friendly interface
- **FastAPI backend** for efficient processing
- **Dockerized deployment** with `docker-compose`
- **GitHub Actions** for CI/CD
- **Deployment on AWS EC2**

---

## 📁 Folder Structure
```
.github/workflows        -> CI/CD workflows
Research/                -> Experiments and hybrid search exploration
__pycache__/             -> Python cache files
data/                    -> Preprocessed textbook data
requirements.txt         -> Project dependencies
tests/                   -> Test scripts
app.py                   -> Streamlit frontend entry
main.py                  -> FastAPI backend entry
backend.Dockerfile       -> Dockerfile for backend
frontend.Dockerfile      -> Dockerfile for frontend
docker-compose.yml       -> Compose config for deployment
```

---

## 🔧 Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Vector DB**: FAISS
- **Framework**: LangChain
- **Model**: `llama-3.3-70b-versatile`
- **API Provider**: GROQ (via `GROQ_API_KEY`)
- **Containerization**: Docker + Docker Compose
- **CI/CD**: GitHub Actions
- **Deployment**: AWS EC2 instance

---

## 🛠️ Installation & Running

### Prerequisites
- Docker & Docker Compose installed
- GROQ API Key setup as environment variable `GROQ_API_KEY`

### Clone the Repository
```bash
git clone https://github.com/ka1817/BioQuest-A-RAG-Driven-Learning-Assistant-for-Biology.git
cd BioQuest-A-RAG-Driven-Learning-Assistant-for-Biology
```

### Run with Docker Compose
```bash
docker-compose up --build
```

### Or Run Manually
#### Backend
```bash
python main.py
```
#### Frontend
```bash
streamlit run app.py
```

---

## 🐳 Docker Images
- Frontend: `pranavreddy123/biorag-frontend:latest`
- Backend: `pranavreddy123/biorag-backend:latest`

To pull and run them:
```bash
docker pull pranavreddy123/biorag-frontend:latest
docker pull pranavreddy123/biorag-backend:latest
```

---

## 🧪 GitHub Actions
This project uses GitHub Actions for:
- **Running tests** on every push
- **Building Docker images** for frontend and backend
- **Pushing images to Docker Hub**

Workflow configuration is located in `.github/workflows/`.

---

## ☁️ Deployment
The application is deployed on an **AWS EC2 instance**. Docker Compose is used to manage the containers on the instance.

---

## 📚 Data Source
- 9th and 10th grade biology textbooks (preprocessed and chunked)

---

## 📬 Contact
For suggestions, issues or collaboration:
**GitHub**: [BioQuest Repository](https://github.com/ka1817/BioQuest-A-RAG-Driven-Learning-Assistant-for-Biology)

---

Happy Learning! 🧬

