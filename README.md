# Smart Travel Planner 🧳🗺️

A personalized travel planning app powered by LLMs and Streamlit, with a dashboard for tracking user activity.

## 🧠 Problem Statement

Planning a trip can be overwhelming — juggling destinations, activities, budgets, and logistics often leads to decision fatigue. Traditional travel tools offer static suggestions, but they lack personalization, adaptability, and intelligent guidance.

## 📘 Solution 
Smart Travel Planner is an AI-powered application that generates personalized travel itineraries by retrieving relevant information from a custom knowledge base using a RAG approach. This project integrates document ingestion, vector-based retrieval, and a language model for generation to deliver accurate and context-aware travel plans.

## Data Source 
https://huggingface.co/datasets/osunlp/TravelPlanner
In TravelPlanner, for a given query, language agents are expected to formulate a comprehensive plan that includes transportation, daily meals, attractions, and accommodation for each day.TravelPlanner comprises 1,225 queries in total. The number of days and hard constraints are designed to test agents' abilities across both the breadth and depth of complex planning.

## Features
The app includes:

Document Ingestion: Load and preprocess FAQs and travel guides into a vector database.
Vector Search: Use semantic embeddings to retrieve the most relevant information.
LLM Integration: Generate personalized travel itineraries based on retrieved data.
User Interface: Simple web interface to input queries and view generated plans.
Evaluation & Monitoring: Built-in evaluation flow to test retrieval and generation quality.
Containerization: Docker setup for easy deployment and reproducibility.

Whether you're planning a weekend getaway or a multi-city adventure, Smart Travel Planner simplifies the process and makes travel planning intuitive, intelligent, and fun.

## Architecture Diagram
<img width="1000" height="1300" alt="ChatGPT Image Aug 9, 2025, 01_24_32 PM" src="https://github.com/user-attachments/assets/2444ef50-ba7c-49e2-8bcd-d01e00d31450" />



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


## 📦 Setup Guide for Smart Travel Planner
Step 1: Get What You Need
Make sure your computer has these installed:

Python 3.10 or higher

Docker and Docker Compose

Git
(Optional) Node.js if you want to work with frontend frameworks

Step 2: Download the Project
Open your terminal (command prompt) and type:

bash
Copy
Edit
git clone https://github.com/your-username/smart-travel-planner.git
cd smart-travel-planner
Step 3: Prepare Your Python Environment
Create and activate a virtual environment to keep things tidy:

bash
Copy
Edit
python -m venv venv
On Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
On Windows:

bash
Copy
Edit
venv\Scripts\activate
Then install all needed packages:

bash
Copy
Edit
pip install -r requirements.txt
Step 4: Configure and Load Data
Create a file named .env in the project folder with these lines:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key
VECTOR_DB_PATH=./embeddings/faiss_index
DATA_PATH=./data/processed
Next, process your travel data by running:

bash
Copy
Edit
python ingestion/ingest.py
Step 5: Run the App
Choose how you want to run it:

Using Streamlit (easy GUI):

bash
Copy
Edit
streamlit run app/main.py

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

<img width="700" height="473" alt="image" src="https://github.com/user-attachments/assets/a30c1d4e-40d1-430f-b03a-9e4c12052678" />

# 🧭 Full Project Roadmap

<img width="468" height="282" alt="image" src="https://github.com/user-attachments/assets/e41f0a51-fb18-4d43-9ff1-542858915993" />

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

# Smart Travel Planner- Demonstration

Dashboard
<img width="1501" height="1008" alt="Screenshot 2025-08-08 at 10 55 37 PM" src="https://github.com/user-attachments/assets/3cede29d-35e5-441b-8ad9-92582a0da547" />

<img width="1920" height="1014" alt="Screenshot 2025-08-08 at 10 55 52 PM" src="https://github.com/user-attachments/assets/c53bae95-210d-493b-9df0-d7a1a4362df8" />

Plotviews and log activities.
<img width="1918" height="1012" alt="Screenshot 2025-08-08 at 11 11 21 PM" src="https://github.com/user-attachments/assets/bb172ff0-55cd-46ad-88ff-579bf48e4e31" />
<img width="1918" height="1004" alt="Screenshot 2025-08-08 at 11 40 23 PM" src="https://github.com/user-attachments/assets/a9879123-4252-4cbd-a107-9d52a2dbc8a2" />
<img width="1919" height="968" alt="Screenshot 2025-08-08 at 11 40 41 PM" src="https://github.com/user-attachments/assets/653fab56-0331-4cc0-882d-90c47e2718e8" />

Docker deployment.
<img width="1918" height="1080" alt="Screenshot 2025-08-08 at 11 57 26 PM" src="https://github.com/user-attachments/assets/722edf01-e47d-4a7f-bb30-f344f3ab3c34" />
<img width="1669" height="538" alt="Screenshot 2025-08-08 at 11 59 18 PM" src="https://github.com/user-attachments/assets/3722f401-3658-416b-88e4-224b22ab4dfc" />

Render connection from github.
<img width="1919" height="966" alt="Screenshot 2025-08-09 at 11 37 12 AM" src="https://github.com/user-attachments/assets/58996403-808e-4cdb-b7ca-3f17728d1e16" />
<img width="1901" height="978" alt="Screenshot 2025-08-09 at 11 39 27 AM" src="https://github.com/user-attachments/assets/378d232e-bc46-43cc-b9cd-686620ae7025" />
<img width="1912" height="1003" alt="Screenshot 2025-08-09 at 11 44 27 AM" src="https://github.com/user-attachments/assets/5afb86f9-7765-4e47-b08d-d3ee87f645cd" />

Github CI/CD.
<img width="1910" height="670" alt="Screenshot 2025-08-09 at 12 21 13 PM" src="https://github.com/user-attachments/assets/dd1a7c11-6ee9-4ae5-b305-5a6e81ca743f" />
<img width="1904" height="681" alt="Screenshot 2025-08-09 at 12 23 32 PM" src="https://github.com/user-attachments/assets/7780af31-f4a2-44a0-962a-8736e17828bd" />
<img width="1801" height="618" alt="Screenshot 2025-08-09 at 12 24 40 PM" src="https://github.com/user-attachments/assets/b0af18c6-a9db-40df-a1a1-85bb0d51a206" />

API key generation in Render
<img width="1424" height="727" alt="Screenshot 2025-08-09 at 12 39 58 PM" src="https://github.com/user-attachments/assets/498aafff-6790-4fe7-b9c8-153b1d37edf6" />

Github mail alert when CI/CD failed
<img width="1598" height="703" alt="Screenshot 2025-08-09 at 12 40 15 PM" src="https://github.com/user-attachments/assets/39b3766c-6bf4-4f4a-84db-0ce55805ce11" />
