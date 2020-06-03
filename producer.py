import sys
from datetime import datetime

import redis


conn = redis.Redis(host="localhost", port=6379, db=0)
queue_name = "test_queue"

conn.rpush(queue_name, str(datetime.now()) + sys.argv[1])