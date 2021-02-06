FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/local/wagyuer

ENTRYPOINT ["ping","localhost"]