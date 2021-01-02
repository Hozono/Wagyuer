FROM ubuntu


ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes
ENV PYTHONUNBUFFERED 1

RUN mkdir /wagyuer
WORKDIR /wagyuer

RUN apt-get update -yq
RUN apt-get install -yq --no-install-recommends curl
RUN apt-get install -yq --no-install-recommends less
RUN apt-get install -yq --no-install-recommends tzdata
RUN apt-get install -yq --no-install-recommends language-pack-ja
RUN apt-get install -yq --no-install-recommends python3
RUN apt-get install -yq --no-install-recommends python-is-python3
RUN apt-get install -yq --no-install-recommends python3-distutils

RUN update-locale LANG=ja_JP.UTF-8
RUN apt-get purge python3-pip
RUN curl -k https://bootstrap.pypa.io/get-pip.py | python

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
# RUN poetry new wagyuer
# RUN cd ./wagyuer
# RUN poetry add django
# RUN poetry install
# TODO: SSL証明書エラー対応　RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python


EXPOSE 8000
CMD ["ping", "192.168.1.1"]