FROM python:3.9.10-slim-buster

RUN mkdir -p /usr/src/aplzm
RUN mkdir -p /usr/src/aplzm/registry
RUN mkdir -p /usr/src/aplzm/registry/app
WORKDIR /usr/src/aplzm
COPY requirements.txt /usr/src/aplzm/registry

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential && apt-get install -y libmariadb3 libmariadb-dev
RUN pip install --no-cache-dir -r registry/requirements.txt
COPY . /usr/src/aplzm/registry
ENV PYTHONPATH /usr/src/aplzm

CMD ["gunicorn","--workers=5","-b", "0.0.0.0:5002", "registry.app:app"]