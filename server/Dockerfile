FROM python:3.9-alpine

COPY ./requirements.txt ./requirements.txt

RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev

RUN apk del .tmp-build-deps

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./server /app

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

USER user