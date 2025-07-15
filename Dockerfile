FROM python:3.10-slim


WORKDIR /app

# Copy everything
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8501
EXPOSE 5000

# Run Flask and Streamlit
CMD ["sh", "-c", "python api/api.py & streamlit run streamlit/streamlit.py --server.headless true --server.enableCORS false"]

