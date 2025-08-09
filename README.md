# Smart Travel Planner 🧳🗺️

A personalized travel planning app powered by LLMs and Streamlit, with a dashboard for tracking user activity.

## 🧠 Problem Statement

Planning a trip can be overwhelming — juggling destinations, activities, budgets, and logistics often leads to decision fatigue. Traditional travel tools offer static suggestions, but they lack personalization, adaptability, and intelligent guidance.

## 📘 Solution 
Smart Travel Planner is an AI-powered application that generates personalized travel itineraries by retrieving relevant information from a custom knowledge base using a RAG approach. This project integrates document ingestion, vector-based retrieval, and a language model for generation to deliver accurate and context-aware travel plans.



## Features
The app includes:

Document Ingestion: Load and preprocess FAQs and travel guides into a vector database.
Vector Search: Use semantic embeddings to retrieve the most relevant information.
LLM Integration: Generate personalized travel itineraries based on retrieved data.
User Interface: Simple web interface to input queries and view generated plans.
Evaluation & Monitoring: Built-in evaluation flow to test retrieval and generation quality.
Containerization: Docker setup for easy deployment and reproducibility.

Whether you're planning a weekend getaway or a multi-city adventure, Smart Travel Planner simplifies the process and makes travel planning intuitive, intelligent, and fun.

# Architecture Diagram
+---------------------+
|   User Interface    |  ← Streamlit 
|  (Planner + Dashboard)
+---------------------+
           |
           v
+---------------------+
|     LLM Engine      |  ← OpenAI 
|  (Generates itinerary)
+---------------------+
           |
           v
+---------------------+
|   Prompt Builder    |  ← Custom prompts based on query
+---------------------+
           |
           v
+---------------------+
|   Retrieval Layer   |  ← FAISS or Chroma
|  (Semantic search from vector DB)
+---------------------+
           |
           v
+---------------------+
|   Embedded Chunks   |  ← Travel data from OSU TravelPlanner
|  (Stored as vectors)
+---------------------+
           |
           v
+---------------------+
|   Ingestion Script  |  ← Python-based pipeline
|  (Cleans, chunks, embeds data)
+---------------------+
           |
           v
+---------------------+
|   Monitoring Layer  |  ← Streamlit Dashboard + Plotly
|  (User feedback, logs, charts)
+---------------------+
           |
           v
+---------------------+
|   Docker Container  |  ← Docker + docker-compose
|  (Encapsulates planner + dashboard)
+---------------------+
           |
           v
+---------------------+
|   CI/CD Pipeline    |  ← GitHub Actions
|  (Auto-deploy on push)
+---------------------+
           |
           v
+---------------------+
|   Cloud Deployment  |  ← Render
|  (Live app hosting)
+---------------------+


# 🧰 Technologies Used & Documentation

| Category          | Technology / Tool          | Documentation Link                                   |
|-------------------|---------------------------|----------------------------------------------------|
| Language          | Python                    | [Python Docs](https://docs.python.org/3/)          |
| UI Framework      | Streamlit / FastAPI       | [Streamlit Docs](https://docs.streamlit.io/) / [FastAPI Docs](https://fastapi.tiangolo.com/) |
| Vector Database   | FAISS / Chroma            | [FAISS Docs](https://faiss.ai/) / [Chroma Docs](https://docs.trychroma.com/)             |
| LLM Integration   | OpenAI / Ollama           | [OpenAI API Docs](https://platform.openai.com/docs) / [Ollama API Docs](https://ollama.com/docs)       |
| RAG Framework     | LangChain / LlamaIndex    | [LangChain Docs](https://python.langchain.com/docs/) / [LlamaIndex Docs](https://gpt-index.readthedocs.io/) |
| Monitoring        | Streamlit Charts / Plotly | [Streamlit Charts](https://docs.streamlit.io/library/api-reference/charts) / [Plotly Docs](https://plotly.com/python/) |
| Containerization  | Docker                    | [Docker Docs](https://docs.docker.com/)             |
| CI/CD             | GitHub Actions            | [GitHub Actions Docs](https://docs.github.com/en/actions) |
| Deployment        | Render                    | [Render Docs](https://render.com/docs)              |
| Optional APIs     | TripAdvisor / Booking.com | [TripAdvisor API](https://developer-tripadvisor.com/) / [Booking.com API](https://developers.booking.com/api/index.html) |


# 📁 Recommended Folder Structure
<img width="791" height="422" alt="image" src="https://github.com/user-attachments/assets/fe740da6-ab9b-4cc9-9e1f-8b48a03c6a38" />


# 📦 Setup Guide for Smart Travel Planner

1. 🔧 Prerequisites
Make sure you have the following installed:

Python 3.10+

Docker & Docker Compose

Git

(Optional) Node.js if you plan to use frontend frameworks

2. 📁 Clone the Repository
bash
git clone https://github.com/your-username/smart-travel-planner.git
cd smart-travel-planner
3. 🐍 Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
4. 📦 Install Dependencies
bash
pip install -r requirements.txt
5. 🔐 Set Up Environment Variables
Create a .env file in the root directory:

env
OPENAI_API_KEY=your_openai_key
VECTOR_DB_PATH=./embeddings/faiss_index
DATA_PATH=./data/processed
6. 🧠 Ingest Travel Data
Run the ingestion script to clean, chunk, and embed travel data:

bash
python ingestion/ingest.py
7. 🚀 Run the App
Option A: Streamlit
bash
streamlit run app/main.py
Option B: FastAPI
bash
uvicorn app.main:app --reload
8. 🐳 Run with Docker
bash
docker-compose up --build
9. 🧪 Run Tests
bash
pytest tests/
10. 🌐 Deploy to Render (Optional)
Push your repo to GitHub

Connect it to Render

Set environment variables in Render dashboard

Choose Docker or Python build


# 🧭 Usage Guide
This app helps users generate personalized travel itineraries using AI. You can run it via a user-friendly interface or interact with it through an API.

✨ Streamlit Interface
To launch the planner UI:

bash
streamlit run app/main.py
Features:
Input destination, travel dates, and preferences

Generate AI-powered itineraries

View and download your plan

Submit feedback for improvement

📊 Monitoring Dashboard
To view user feedback and usage analytics:

bash
streamlit run dashboard/dashboard.py
Dashboard Includes:
Most requested destinations

Feedback ratings

LLM response quality metrics

# 📁 Code Structure
smart-travel-planner/
├── app/
│   ├── main.py              # Entry point for Streamlit or FastAPI app
│   ├── planner.py           # Core logic for itinerary generation
│   ├── utils.py             # Helper functions (e.g., date parsing, formatting)
│   ├── config.py            # Configuration settings and constants
│   └── feedback.py          # Handles user feedback and storage
│
├── dashboard/
│   └── dashboard.py         # Streamlit dashboard for analytics and feedback
│
├── data/
│   └── destinations.json    # Sample data for popular destinations
│
├── tests/
│   ├── test_planner.py      # Unit tests for itinerary logic
│   └── test_feedback.py     # Tests for feedback handling
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Files to ignore in version control

# 📊 Evaluation and Monitoring
This project includes tools to evaluate itinerary quality and monitor user feedback to continuously improve the travel planning experience.

✅ Evaluation Metrics
We assess the AI-generated itineraries using the following criteria:

Relevance: Are the suggested activities appropriate for the destination and user preferences?

Diversity: Does the itinerary include a mix of cultural, culinary, and outdoor experiences?

Feasibility: Are the activities realistically achievable within the time frame?

User Satisfaction: Based on feedback ratings and comments.

📈 Monitoring Dashboard
Launch the dashboard to visualize usage trends and feedback:

bash
streamlit run dashboard/dashboard.py
Dashboard Features:
🔥 Most requested destinations

💬 User feedback and ratings

📊 Itinerary quality scores

🧠 LLM response analysis (e.g., token count, response time)

🧪 Feedback Loop
User feedback is stored and periodically reviewed to fine-tune the itinerary generation logic.

Feedback is collected via a form in the UI

Stored in a local database or cloud storage

Used to retrain or adjust prompt templates for better results

🛠️ Future Enhancements
Planned improvements include:

Sentiment analysis on feedback

Automated itinerary scoring using external travel APIs

A/B testing different prompt styles





