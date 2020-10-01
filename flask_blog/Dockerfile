FROM ubuntu:18.04 

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip


COPY requirements.txt ./
RUN pip install -r requirements.txt
 
CMD flask run --host=0.0.0.0 --port=5000
