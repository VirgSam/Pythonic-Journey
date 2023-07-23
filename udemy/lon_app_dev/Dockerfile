FROM python:3.12.0b4-alpine3.17
LABEL maintainer="https://github.com/VirgSam"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000

RUN python -m vvenv /py && \
         /py/bin/pip install --upgrade pip && \
         /py/bin/pip install -r /requirementst.txt && \
         adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"