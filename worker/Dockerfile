FROM python:3.8
RUN pip install pika
RUN pip install requests
RUN pip install yfinance
COPY ./worker.py worker.py
CMD python worker.py
