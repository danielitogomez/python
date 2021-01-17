.PHONY: help database build run all

help:
	@echo 'Use make database for create init database'
	@echo 'Use make build for build the container'
	@echo 'Use make run for run the container'
	@echo 'Use make all for make 3 before steps'

database:
	python3.9 init_db.py

build:
	docker build --tag flask_blog:1.0 .

run:
	docker run --publish 8000:5000 --detach --name flask_blog flask_blog:1.0

all:
	python3.9 init_db.py
	docker build --tag flask_blog:1.0 .
	docker run --publish 8000:5000 --detach --name flask_blog flask_blog:1.0
