import json
from flask_restful import abort
import pandas as pd

import registry.utils.functions as f


class NewRecord:
    def __init__(self,payload):
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


class ExpScoreException(ApzmException):
    pass


class ExpMarkException(ApzmException):
    pass


class ExpScoreProbabilityException(ApzmException):
    pass


class ExpPercentileException(ApzmException):
    pass


class PredictException(ApzmException):
    pass


class ClientIdException(ApzmException):
    pass


class RegisterException(ApzmException):
    pass



def exception_handler(exc):
    if isinstance(exc, ExpMarkException):
        err_code = "ERR901"
        description = "Paramater Experian Mark - " + str(exc.__error__)
    elif isinstance(exc, ExpScoreException):
        err_code = "ERR902"
        description = "Parameter Experian Score - " + str(exc.__error__)
    elif isinstance(exc, ExpScoreProbabilityException):
        err_code = "ERR903"
        description = "Parameter Experian Score Probability - " + str(exc.__error__)
    elif isinstance(exc, ExpPercentileException):
        err_code = "ERR904"
        description = "Parameter Experian Percentile - " + str(exc.__error__)
    elif isinstance(exc, PredictException):
        err_code = "ERR905"
        description = "Something went wrong applying the prediction - " + str(exc.__error__)
    elif isinstance(exc, ClientIdException):
        err_code = "ERR906"
        description = "Paramter ID - " + str(exc.__error__)
    else:
        err_code = "ERR999"
        description = "Something went wrong - " + str(exc)

    return abort(403, success=False, message=err_code, description=description)
