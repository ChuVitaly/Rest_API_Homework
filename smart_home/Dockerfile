FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

#COPY .. /requirements.txt /app/

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


RUN python manage.py makemigrations
RUN python manage.py migrate


