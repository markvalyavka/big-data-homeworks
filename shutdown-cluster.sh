#!/bin/sh

echo "Removing spark network."
docker network remove spark-network

echo "Starting Spark and Spark worker."
docker-compose -f ./docker-compose.yaml down




