FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit/streamlit.py", "--server.headless=true", "--server.enableCORS=false", "--server.port=8501"]
