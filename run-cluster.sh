#!/bin/sh

echo "Creating kafka network."
docker network create kafka-network

echo "Starting kafka and zookeeper."
docker-compose -f ./docker-compose.yaml up --build -d kafka_node zookeeper_server

echo "Sleeping for 5 sec"
sleep 5

echo "Creating tweets topic."
docker run -d --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server kafka_node:9092 --replication-factor 1 --partitions 3 --topic tweets

