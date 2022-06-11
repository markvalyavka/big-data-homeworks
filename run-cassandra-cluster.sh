docker network create kafka-network || true

echo "Starting cassandra node."
docker-compose -f ./docker-compose.yaml up --build -d cassandra