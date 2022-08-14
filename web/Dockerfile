# Build from python:latest
FROM python:latest

COPY requirements.txt ./

# Is more easily to manage the requirements from Dockerfile
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]