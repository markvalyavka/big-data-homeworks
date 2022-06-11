#!/bin/sh
echo "Run producer."
docker-compose -f ./docker-compose.yaml up --build producer_app

