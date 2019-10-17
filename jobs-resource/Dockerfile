FROM python:3-slim

COPY requirements.txt /requirements.txt
RUN python -m pip install -r requirements.txt

RUN mkdir -p /opt/resource
COPY check in out test /opt/resource
