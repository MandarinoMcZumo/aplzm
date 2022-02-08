import pytest

payload_value = {"data": '{"experian-score":{"0":1},"experian-score_probability_default":{"0":0.91},"experian-score_percentile":{"0":80.0},"experian-mark":{"0":"G"}}'}


def test_prediction_ok(client):
    headers = {"Content-Type": "application/json"}
    response = client.post('/model/asnef/predict', headers=headers, json=payload_value)
    assert response.status_code == 200


def test_prediction_ko(client):
    headers = {"Content-Type": "application/json"}
    payload_value_ko = payload_value.copy()
    payload_value_ko.update({'data': 'not_valid_payload_string'})
    response = client.post('/model/asnef/predict', headers=headers, json=payload_value_ko)
    assert response.status_code == 403

