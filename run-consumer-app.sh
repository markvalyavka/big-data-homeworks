#!/bin/sh
echo "Run consumer."
docker-compose -f ./docker-compose.yaml up --build consumer_app
