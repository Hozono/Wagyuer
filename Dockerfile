FROM python:3.9.1-buster

WORKDIR /usr/local/wagyuer

ENTRYPOINT ["ping","localhost"]