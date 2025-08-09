# Smart Travel Planner 🧳🗺️

A personalized travel planning app powered by LLMs and Streamlit, with a dashboard for tracking user activity.

🧠 Problem Statement
Planning a trip can be overwhelming — juggling destinations, activities, budgets, and logistics often leads to decision fatigue. Traditional travel tools offer static suggestions, but they lack personalization, adaptability, and intelligent guidance.

📘 Project Description
Smart Travel Planner is an AI-powered travel assistant that helps users design personalized itineraries based on their preferences, constraints, and goals. Built with Streamlit and powered by large language models (LLMs), it generates dynamic travel plans and adapts to user feedback in real time.

The app includes:

🧳 A Planner interface for generating and customizing itineraries

📊 A Dashboard for visualizing user activity and logs

🐳 Dockerized architecture for easy deployment and scalability

Whether you're planning a weekend getaway or a multi-city adventure, Smart Travel Planner simplifies the process and makes travel planning intuitive, intelligent, and fun.


## 🚀 Features

- ✈️ AI-powered itinerary generation
- 📍 Location-based recommendations
- 📊 Dashboard for user logs and analytics
- 🐳 Dockerized for easy deployment

## 🛠️ Tech Stack

- Python + Streamlit
- Docker + Docker Compose
- GitHub for version control

## 📦 Setup

```bash
git clone https://github.com/yourusername/smart-travel-planner.git
cd smart-travel-planner
docker-compose up --build

smart-travel-planner/
├── planner/       # Streamlit app
├── dashboard/     # Log visualization
├── data/          # Shared data
├── logs/          # User activity logs
├── docker-compose.yml
└── .env
