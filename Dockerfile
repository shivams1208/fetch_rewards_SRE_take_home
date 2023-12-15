FROM python:3.9.7-slim

WORKDIR /fetch_rewards
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
COPY . ./