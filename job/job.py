#!/usr/bin/env python
import pika
import os
RABBITMQ_HOST = os.environ["RABBITMQ_HOST"]
credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                    credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

for _ in range(100):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World !')

print(" [x] Sent 'Hello World!'")
connection.close()
