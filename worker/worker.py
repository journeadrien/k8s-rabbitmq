import os

from redis import StrictRedis
from rq import Worker, Queue, Connection
from utils import count_words_at_url

listen = ['high', 'default', 'low']

#REDIS_HOST = os.environ['REDIS_HOST']
REDIS_HOST = "redis-master"
print("REDIS_HOST : %s"%REDIS_HOST)
REDIS_PORT = 6379
conn = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen), path="./")
        worker.work()
