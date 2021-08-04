FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8010

CMD ["gunicorn", "sample.wsgi", "--bind 0.0.0.0:8010", "--workers 3"]