FROM debian:stretch

ADD . /app

WORKDIR /app

RUN apt-get update && apt-get install -y python python-pip && pip install --upgrade gensim flask

CMD python wrapper.py
