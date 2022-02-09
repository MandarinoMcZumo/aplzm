FROM python:3.9.10-slim-buster

RUN mkdir -p /usr/src/aplzm
RUN mkdir -p /usr/src/aplzm/predict
RUN mkdir -p /usr/src/aplzm/predict/app
WORKDIR /usr/src/aplzm
COPY requirements.txt /usr/src/aplzm/predict

RUN pip install --no-cache-dir -r predict/requirements.txt
COPY . /usr/src/aplzm/predict
ENV PYTHONPATH /usr/src

CMD ["gunicorn","--workers=5","-b", "0.0.0.0:5001", "predict.app:app"]