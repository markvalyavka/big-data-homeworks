#!/bin/sh
echo "Creating test-topic topic."
docker run -d --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server kafka_node:9092 --replication-factor 1 --partitions 3 --topic test-topic
