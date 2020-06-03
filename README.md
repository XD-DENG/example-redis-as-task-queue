# example-redis-as-task-queue

Simple example using Redis as task queue

```bash
# Console 1
docker run -d -p 6379:6379 redis

python worker.py
```

```bash
# Console 2
python producer.py ...
```
