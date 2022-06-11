import csv
from datetime import datetime
import json
import time

from kafka import KafkaConsumer
from cassandra_client import cs


TOPIC_NAME = "user_transactions"
CASSANDRA_HOST = "cassandra_node1"
CASSANDRA_PORT = 9042
CASSANDRA_KEYSPACE = "hw8_valyavka"

import logging
logging.basicConfig(level=logging.DEBUG)


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=['kafka_node:9092'],
    value_deserializer=lambda m: json.loads(m.decode('ascii')),
)
cs.init_app(CASSANDRA_HOST, CASSANDRA_PORT, CASSANDRA_KEYSPACE)

from pprint import pprint

def start_consuming():

    for user_tx in consumer:
        print("Received:")
        pprint(user_tx)
        cs.insert_into_user_by_is_fraud(user_tx)
        cs.insert_into_user_by_amount(user_tx)
        cs.insert_into_user_transactions_by_date(user_tx)




if __name__ == "__main__":

    print("Started consuming..")
    start_consuming()
