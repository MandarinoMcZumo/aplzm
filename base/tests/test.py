import pytest
import base.utils.classes as c
import base.utils.functions as f
import pandas as pd

client_id = '12345678A'
client_payload = {
    'experian-score': 1,
    'experian-score_probability_default': 0.5,
    'experian-score_percentile': 80.0,
    'experian-mark': 'B'
}

predict_value_str = """{"experian-score": 1, "experian-score_probability_default": 0.5, "experian-score_percentile": 80.0, "experian-mark": "B", "prediction": null, "client-id": "12345678A"}"""


def test_client_class_ok():
    client = c.Client(client_id, client_payload)
    assert client.data is None
    data = client.validate_attrs().build_df()
    assert client.data.shape == data.shape
    assert type(client.data) == pd.DataFrame
    assert client.build_predict_payload() == predict_value_str


def test_client_ko():
    client_payload_ko = client_payload.copy()
    client_payload_ko.update({'experian-score': "A"})
    try:
        c_ko = c.Client(client_id, client_payload_ko)
    except:
        assert True


def test_numeric_validation():
    f.numeric_validation(1, int, [0, 2], Exception)
    assert True


def test_numeric_validation_ko():
    try:
        f.numeric_validation(5, int, [0, 2], Exception)
    except:
        assert True

def test_string_validation():
    f.string_validation('a', '[a-zA-Z]', Exception)
    assert True

def test_string_validation_ko():
    try:
        f.string_validation('1', '[a-zA-Z]', Exception)
    except:
        assert True
