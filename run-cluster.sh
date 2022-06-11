#!/bin/sh

echo "Creating spark network."
# If not exists..
docker network create spark-network || true

echo "Starting Spark and Spark worker."
docker-compose -f ./docker-compose.yaml up --build -d spark spark-worker

echo "Sleeping for 5 sec"
sleep 5


