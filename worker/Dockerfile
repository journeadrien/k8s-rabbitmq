FROM python
RUN pip install redis
RUN pip install rq
COPY ./worker.py /worker.py
CMD python worker.py
