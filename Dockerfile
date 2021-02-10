FROM python:3.7

RUN pip install --upgrade pip
COPY ./app /app
WORKDIR /app
EXPOSE 8000:8000
CMD python /app/server.py
