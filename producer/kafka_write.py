import csv
import datetime
import json
import time

from kafka import KafkaProducer


import logging
logging.basicConfig(level=logging.DEBUG)

TOPIC_NAME = "tweets"


producer = KafkaProducer(
    bootstrap_servers=['kafka_node:9092'],
    value_serializer=lambda m: json.dumps(m).encode('ascii'),
)


def produce_from_file(filename):

    with open(filename) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:

            # replace date with datetime.now()
            row[3] = datetime.datetime.now().isoformat()
            producer.send(TOPIC_NAME, row)
            producer.flush()
            print(f"sent {row}")


if __name__ == "__main__":
    print("Producing tweets in 10 seconds..")
    time.sleep(10)
    print("Producing tweets in 5 seconds..")
    time.sleep(10)
    produce_from_file("res/tweets.csv")
