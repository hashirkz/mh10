FROM python:3.8

COPY . /app/

WORKDIR /app

EXPOSE 8080 

RUN pip3 install -r "./requirements.txt"

RUN python3 -u "./app.py"