FROM python:3.9.0-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY kafka_write.py .

COPY res/ ./res/

VOLUME .:/app

ENTRYPOINT ["python3", "kafka_write.py"]

