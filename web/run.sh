#!/bin/bash

docker build -t web-scraping . && docker run -it --rm --name web-scraping web-scraping