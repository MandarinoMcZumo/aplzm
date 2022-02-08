FROM python:3.9.10-slim-buster

RUN mkdir -p /usr/src/aplzm
RUN mkdir -p /usr/src/aplzm/base
RUN mkdir -p /usr/src/aplzm/base/app
WORKDIR /usr/src/aplzm
COPY requirements.txt /usr/src/aplzm/base

RUN pip install --no-cache-dir -r base/requirements.txt
COPY . /usr/src/aplzm/base
ENV PYTHONPATH /usr/src/aplzm

EXPOSE 5000
CMD ["gunicorn","--workers=5","-b", "0.0.0.0:5000", "base.app:app"]