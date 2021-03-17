from redis import StrictRedis
from rq import Queue, Connection
from time import sleep
from random import randint

REDIS_HOST = "redis-master"
REDIS_PORT = 6379

conn = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

if __name__ == '__main__':
    with Connection(conn):
        q = Queue(connection=conn)
        #job = q.enqueue(count_words_at_url, 'https://kubernetes.io/docs/concepts/workloads/controllers/job/')
        job = q.enqueue(randint,0,10)

        while not job.is_finished:
            if job.is_failed:
                print('Job has failed!')
                exit(0)
            else:
                print("Running job")
                sleep(1)
        print("Result of your job is : %s"%job.result)
