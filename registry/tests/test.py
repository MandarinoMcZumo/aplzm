from unittest import TestCase
from unittest.mock import patch
from registry.app import create_app
import pytest
import os


class FakeCursor:
    def __init__(self):
        self.__iter_count__ = 0
        self.__iter_values__ = {"0": ("some_date", "some_score")}
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter_count__ == 1:
            raise StopIteration
        value = self.__iter_values__.get(str(self.__iter_count__))
        self.__iter_count__ += 1
        return value

    def cursor(self):
        return FakeCursor()

    def execute(self, q=None, p=None):
        pass

    def commit(self=None):
        pass

    def close(self=None):
        pass

os.chdir(os.getcwd().replace("tests", "app"))
payload_value = {
    "data": '{"experian-score":1,"experian-score_probability_default":0.91,"experian-score_percentile":80.0,"experian-mark":"G","prediction":6, "client-id":"testID"}'}




class TestRegistry(TestCase):
    def setUp(self):
        os.chdir(os.getcwd().replace("tests", "app"))
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client

    @patch('registry.utils.functions')
    @patch('registry.database.db_connection.connect_db')
    def test_new_registry_ok(self, mock_connect_db, mock_functions):
        mock_connect_db.return_value = FakeCursor()
        mock_functions.return_value = None

        headers = {"Content-Type": "application/json"}
        response = self.client().post('/asnef/register/testID', headers=headers, json=payload_value)
        assert response.status_code == 200

    @patch('registry.utils.functions')
    @patch('registry.database.db_connection.connect_db')
    def test_get_registry_ok(self, mock_connect_db, mock_functions):
        mock_connect_db.return_value = FakeCursor()
        mock_functions.return_value = None

        headers = {"Content-Type": "application/json"}
        response = self.client().get('/asnef/register/testID', headers=headers, json=payload_value)
        assert response.status_code == 200
