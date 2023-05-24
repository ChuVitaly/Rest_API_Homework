FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY smart_home_app1 /app/
WORKDIR /app/

RUN python manage.py makemigrations
RUN python manage.py migrate


