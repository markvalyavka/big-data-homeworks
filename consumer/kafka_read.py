import csv
from datetime import datetime
import json
import time

from kafka import KafkaConsumer


import logging
logging.basicConfig(level=logging.DEBUG)

TOPIC_NAME = "tweets"


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=['kafka_node:9092'],
    value_deserializer=lambda m: json.loads(m.decode('ascii')),
)


def filename_from_datetime(dt):
    return f"tweets_{dt.day}_{dt.month}_{dt.year}_{dt.hour}_{dt.minute}.csv"


def start_consuming():
    tweet_header = ['author_id', 'created_at', 'text']
    next_to_write = []
    last_date = None

    for tweet in consumer:

        tweet_vals = [tweet.value[1], tweet.value[3], tweet.value[4]]
        print("--------------")
        print(f"Got {tweet_vals}")
        print("--------------")
        # trunc s and ms in 'created' time
        tweet_date = datetime.fromisoformat(tweet.value[3]).replace(second=0, microsecond=0)

        if tweet_date != last_date:
            if not last_date:
                last_date = tweet_date
            # if cur date != last date, we write accumulated tweets
            with open(f"./resulting_files/{filename_from_datetime(last_date)}", "w+") as f:
                f_writer = csv.writer(f)
                f_writer.writerow(tweet_header)
                f_writer.writerows(next_to_write)
                print("Wrote", filename_from_datetime(last_date))
            last_date = tweet_date
            # reset tweets to write
            next_to_write = []
        # accumulate tweets for a new minute
        next_to_write.append(tweet_vals)



if __name__ == "__main__":

    print("Started consuming..")
    start_consuming()
