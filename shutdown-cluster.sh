#!/bin/sh

echo "Stopping kafka and zookeeper."
docker-compose -f ./docker-compose.yaml down

echo "Removing kafka network."
docker network remove kafka-network
