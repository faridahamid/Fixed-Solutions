FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Use faster PyPi mirror (optional)
RUN pip install --upgrade pip \
    && pip config set global.timeout 100 \
    && pip install --no-cache-dir -i https://pypi.org/simple -r requirements.txt

EXPOSE 5000

CMD ["python", "api/api.py"]
