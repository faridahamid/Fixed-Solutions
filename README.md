# Fixed-Solutions Internship

 
This repo documents practical tasks and solutions developed during the internship.


---

## Tasks Overview

### Task 1: Iris Classification App (Full Stack)

 A full-stack mini project combining a **machine learning model**, **Flask backend**, and **Streamlit frontend**. The application allows users to input features and receive real-time predictions via an API.

- **Flask** API serves the prediction model
- **Streamlit** UI calls the API
- Deployed locally and Docker-ready
- Contains:
  - `api.py` – Flask backend  
  - `Streamlit.py` – Streamlit UI  
  - `Dockerfile`, `docker-compose.yml` – for containerization  
  - `README.md` – full setup instructions

---

### Task 2: Customer Segmentation – Online Retail Dataset

 A full data science project focused on **customer behavior analysis** and **clustering using RFM and K-Means**.

- Dataset from UCI (Excel to CSV conversion)
- Cleaned and transformed data
- Monthly sales trend analysis
- RFM segmentation + clustering
- Business recommendations and KPIs
- **Power BI dashboard** and presentation slides included

**Contents:**
- `/Task 2/Model/` – contains the dataset  
- `/Task 2/Presentation/` – final 10-slide presentation  
- `onlineRetailmodel.ipynb` – main project notebook  
- `README.md` – full explanation and results

---
## File Structure

This section outlines the folder and file organization within this repository:
Fixed-Solutions/
│
├── Task 1/ # Full-stack Iris classification project
│ ├── Backend/ # Flask backend (API)
│ ├── Frontend/ # Streamlit frontend (UI)
│ ├── Docker_file.prod # Production Dockerfile
│ ├── Dockerfile # Development Dockerfile
│ ├── docker-compose.yml # Docker orchestration
│ ├── Iris.csv # Dataset used for training
│ ├── Task 1.ipynb # Notebook for training and testing
│ └── README.md # Documentation for Task 1
│
├── Task 2/ # Customer segmentation project
│ ├── Model/ # Data and notebook
│ │ ├── Online Retail.xlsx - Online Retail.csv
│ │ └── onlineRetailmodel.ipynb # RFM and K-Means analysis
│ ├── Presentation/ # PowerPoint slides
│ │ └── Customer Segmentation.pptx
│ └── README.md # Documentation for Task 2
│
└── README.md # Main README for the entire repo
---





