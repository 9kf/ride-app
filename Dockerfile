# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

