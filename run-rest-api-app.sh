#!/bin/sh
echo "Run REST API app."
docker-compose -f ./docker-compose.yaml up --build app_rest_api

