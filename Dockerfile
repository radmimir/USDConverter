FROM python:3.7

RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
ENTRYPOINT python ./app/server.py
