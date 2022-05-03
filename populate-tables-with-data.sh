
# Run DML script
docker exec -it cassandra_node1 cqlsh -f /docker-entrypoint-initdb.d/2_populate_with_data.cql

