import time
from datetime import datetime

import redis

conn = redis.Redis(host="localhost", port=6379, db=0)
queue_name = "test_queue"

def consumer(job_msg):
    print(f"{datetime.now()} Received job: {job_msg}")
    sleep_time = str(job_msg).count(".")
    if sleep_time == 0:
        sleep_time = 1
    print(f"Sleeping for {sleep_time} seconds ({sleep_time} dots found in the string)")
    time.sleep(sleep_time)
    print("Done")

while True:
    job_msg = conn.blpop([queue_name], 3)
    if not job_msg:
        continue
    consumer(job_msg[1])
