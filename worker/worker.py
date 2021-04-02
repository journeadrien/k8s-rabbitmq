#!/usr/bin/env python
import pika, sys, os, time
import yfinance as yf
RABBITMQ_HOST = os.environ["RABBITMQ_HOST"]
print("Worker init")
def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                        credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='hello', auto_delete=True)

    def callback(ch, method, properties, body):
        symbol = body.decode()
        print(" [x] Received %r" % body.decode())
        yf_request(symbol)
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def yf_request(symbol):
    data = yf.download(symbol, start="2017-01-01", end="2017-04-30")
    return None

def factorielle(n):
    """Ceci est une fonction récursive qui appelle
   lui-même pour trouver la factorielle du nombre donné"""
    if n == 1:
        return n
    else:
        return n * factorielle(n - 1)

if __name__ == '__main__':
    main()
