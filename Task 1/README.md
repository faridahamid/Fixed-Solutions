## Task 1: Iris Classification App (Full Stack)

### Objective:
Build a complete machine learning pipeline that:
- Trains a model to classify iris flowers
- Provides a REST API using **Flask**
- Offers a user interface via **Streamlit**
- Is containerized with **Docker** for easy testing and deployment

### Technologies:
- Python 3.10  
- Flask  
- Streamlit  
- Scikit-learn  
- Docker

### Features:
- API endpoint: `/predict` for real-time predictions  
- Streamlit app to input flower data and display the prediction  
- Dockerized in two modes:
  - Development (`Dockerfile`)
  - Production (`Docker_file.prod`)

---

##  How to Run

###  Development Mode

```bash
cd Task_1
docker build -t iris-dev -f Dockerfile .
docker run -p 8501:8501 -p 5000:5000 iris-dev
```



