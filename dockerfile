FROM python:3.8

RUN pip3 install -r "./requirements.txt"

RUN python3 -u "./app.py"