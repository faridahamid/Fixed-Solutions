### Based On

This project is **cloned and adapted** from the original repo:  
 [AchilleasKn/flask_api_python](https://github.com/AchilleasKn/flask_api_python)  
We extended and **refactored** it into a full-stack application with:

- A Streamlit frontend
- A complete Docker setup (including `docker-compose`)
- Mobile accessibility via ngrok

---

## Task 1: Iris Classification App (Full Stack)

###  Objective:
Build a complete machine learning pipeline that:
- Trains a model to classify iris flowers
- Provides a REST API using **Flask**
- Offers a user interface via **Streamlit**
- Is containerized with **Docker** for development and deployment

---

### Technologies:
- Python 3.10  
- Flask  
- Streamlit  
- Scikit-learn  
- Docker & Docker Compose

---

### Features:
- API endpoint: `/predict` for real-time predictions  
- Streamlit web app to input flower features and display predictions  
- Exposed via **ngrok** for testing on **mobile**  
- Modular structure with separate containers for backend and frontend

---

##  How to Run the Project

###  Option 1: Development Mode (Single Dockerfile)

```bash
cd Task 1
docker build -t iris-dev -f Dockerfile .
docker run -p 8501:8501 -p 5000:5000 iris-dev
```

---

### Option 2: Using Docker Compose (Multi-container)

#### Folder Structure:
```
Task_1/
│
├── backend/
│   └── Dockerfile  (Flask API)
│
├── frontend/
│   └── Dockerfile  (Streamlit UI)
│
├── docker-compose.yml
```

####  Build and Run:
```bash
cd Task 1
docker-compose up --build
```

This will run both the backend and frontend containers simultaneously.

---

## Accessing the App

### On Your Local Machine:
- Streamlit UI: [http://localhost:8501](http://localhost:8501)
- API Endpoint: [http://localhost:5000/predict](http://localhost:5000/predict) (you can use postman to test it)

### Test on Mobile

#### Option 1: Using Ngrok
1. Install ngrok:
```bash
curl -o ngrok.zip https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-windows-amd64.zip
tar -xf ngrok.zip
./ngrok config add-authtoken YOUR_AUTHTOKEN
```

2. Run ngrok for Streamlit:
```bash
ngrok http 8501
```

#### Option 2: Local Network (Same Wi-Fi)
Visit `http://your-local-ip:8501` from your mobile browser (use `ipconfig` to find IP).

---

## Project Structure

```
Task_1/
├── backend/
│   ├── api/
│   │   └── api.py
│   ├── iris_model.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit.py
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

---

## Improvements Made

- Split project into `backend` (Flask) and `frontend` (Streamlit)
- Added multi-container Docker support via `docker-compose.yml`
- Enabled mobile access using Ngrok tunnels
-  End-to-end pipeline: ML model → API → UI → Dockerized

---
