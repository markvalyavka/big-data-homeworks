FROM python:3.8.9

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY config.py .

COPY app.py .

COPY cassandra_client.py .

EXPOSE 8080

ENTRYPOINT ["python3", "runserver.py"]