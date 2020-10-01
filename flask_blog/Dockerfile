FROM ubuntu:18.04

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install -r requirements.txt

CMD flask run --host=0.0.0.0
