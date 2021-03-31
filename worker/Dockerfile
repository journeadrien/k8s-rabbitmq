FROM python:3.8
RUN pip install pika
RUN pip install requests
COPY ./worker.py worker.py
CMD python worker.py
