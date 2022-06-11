
import datetime
import json
import random
import time
from csv import DictReader
from kafka import KafkaProducer


import logging
logging.basicConfig(level=logging.DEBUG)

TOPIC_NAME = "user_transactions"


producer = KafkaProducer(
    bootstrap_servers=['kafka_node:9092'],
    value_serializer=lambda m: json.dumps(m).encode('ascii'),
)

def random_1mo_ago_date(delta=datetime.timedelta(days=31)):
    """
    This function will return a random datetime between
    [now() - 31days, now()]
    """
    date_31d_ago = datetime.datetime.now() - delta
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (date_31d_ago + datetime.timedelta(seconds=random_second)).strftime("%Y-%m-%d")

from pprint import pprint
def produce_from_file(filename):

    with open(filename) as f:
        csv_reader = DictReader(f, delimiter=',')
        for row in csv_reader:
            # artificial sending delay
            time.sleep(0.2)
            time.sleep(1)
            # replace date with datetime.now()
            upd_row = {
                **row,
                'transactionDate': random_1mo_ago_date()
            }
            pprint(upd_row)

            producer.send(TOPIC_NAME, upd_row)
            producer.flush()
            print(f"sent {upd_row}")



if __name__ == "__main__":
    print("Producing tweets in 10 seconds..")
    time.sleep(10)

    produce_from_file("res/fraud_detection.csv")
