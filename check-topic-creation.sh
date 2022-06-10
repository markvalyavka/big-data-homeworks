#!/bin/sh
echo "Checking test-topic creation."
docker run -it --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --list  --bootstrap-server kafka_node:9092
