# smart-travel-planner
Create personalized travel itineraries using real-time data from travel APIs

# Smart Travel Planner 🧳🗺️

A personalized travel planning app powered by LLMs and Streamlit, with a dashboard for tracking user activity.

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
