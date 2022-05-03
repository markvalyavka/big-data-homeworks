# big-data-homeworks
HWs for Big Data course UCU

### Run
1. Put your dataset into cassandra/init_data/amazon_reviews_100k.tsv


2. Run startup script (DDL is done on startup automatically)
```bash
sh run-cluster.sh
```

3. Populate tables with data (Might need to wait until cassandra init before running)
```bash
sh populate-tables-with-data.sh
```

4. Try out queries via API
5. Shutdown
```bash
sh shutdown-cluster.sh
```

