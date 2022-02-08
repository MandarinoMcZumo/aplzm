import json
from flask_restful import abort
import pandas as pd

import registry.utils.functions as f


class NewRecord:
    def __init__(self, payload):
        self.id = payload['client-id']
        self.experian_score = payload['experian-score']
        self.experian_score_probability_default = payload['experian-score_probability_default']
        self.experian_score_percentile = payload['experian-score_percentile']
        self.experian_mark = payload['experian-mark']
        self.predict_value = payload['prediction']


class ApzmException(Exception):
    def __init__(self, error_message=None):
        self.__error__ = error_message

    pass


class DBException(ApzmException):
    pass


def exception_handler(exc):
    if isinstance(exc, DBException):
        err_code = "ERR907"
        description = "Database Error - " + str(exc.__error__)
    else:
        err_code = "ERR999"
        description = "Registry APP - Something went wrong - " + str(exc)
    return abort(403, success=False, message=err_code, description=description)
