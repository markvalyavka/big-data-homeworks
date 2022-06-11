# big-data-homeworks | kafka-producer
HWs for Big Data course UCU.

1. Create cluster:
```
sh ./run-cluster.sh
```

![res](screenshots/run_cluster_1.png)
![res](screenshots/run_cluster_2.png)

2. Run consumer:
```
sh ./run-cli-consumer.sh
```

3. Run producer app:
```
sh ./run-producer-app.sh
```

4. Results:
  -  Producer ran:
![res](screenshots/producer_run.png)
  -  Consumer ran:
![res](screenshots/consumer_run.png)

5. Shutdown cluster:

To shutdown Kafka cluster:
```
sh ./shutdown-cluster.sh
```
![res](screenshots/shutdown_cluster.png)
