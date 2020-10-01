FROM ubuntu:18.04 

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "flask_blog/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install -r requirements.txt   
 
CMD flask run --host=0.0.0.0 --port=5000
