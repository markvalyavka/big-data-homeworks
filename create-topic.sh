#!/bin/sh

docker exec kafka_node "kafka-topics.sh --create --topic test-topic --replication-factor 1 --partitions 3 --bootstrap-server kafka-server:9092"
