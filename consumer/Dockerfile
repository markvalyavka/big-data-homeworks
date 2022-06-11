FROM python:3.9.0-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY kafka_read.py .

COPY cassandra_client.py .

COPY resulting_files/ ./resulting_files/

VOLUME .:/app

ENTRYPOINT ["python3", "kafka_read.py"]

