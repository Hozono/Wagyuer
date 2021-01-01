FROM ubuntu


ENV TZ=Asia/Tokyo
ENV PYTHONUNBUFFERED 1

RUN apt-get update -yq ; apt-get install -yq --no-install-recommends \
    tzdata \
    language-pack-ja \
    python3 \
    python-is-python3 \
    python3-distutils

RUN update-locale LANG=ja_JP.UTF-8
RUN apt-get purge python3-pip ; \
    curl -sSL https://bootstrap.pypa.io/get-pip.py | python

# WORKDIR /usr/local/bsa_schedule_web

EXPOSE 8000
CMD ["ping", "192.168.1.1"]