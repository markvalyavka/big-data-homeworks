#!/bin/sh

echo "Creating kafka network."
docker network create kafka-network

echo "Starting kafka and zookeeper."
docker-compose -f ./docker-compose.yaml up --build

