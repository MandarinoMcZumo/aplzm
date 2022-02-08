import json
import pandas as pd
from flask_restful import abort
import base.utils.functions as f


class Client:
    def __init__(self, client_id, payload):
        self.__id__ = client_id
        self.__experian_score__ = payload['experian-score']
        self.__experian_score_probability_default__ = payload['experian-score_probability_default']
        self.__experian_score_percentile__ = payload['experian-score_percentile']
        self.__experian_mark__ = payload['experian-mark']
        self.data = None
        self.predict_value = None
        self.predict_payload = None

    def validate_attrs(self):
        f.numeric_validation(self.__experian_score__, int, [0, 200], ExpScoreException)
        f.numeric_validation(self.__experian_score_probability_default__, float, [0, 1], ExpScoreProbabilityException)
        f.numeric_validation(self.__experian_score_percentile__, float, [0, 100], ExpPercentileException)
        f.string_validation(self.__id__, '^[0-9]{8,8}[A-Za-z]$', ClientIdException)
        f.string_validation(self.__experian_mark__, '[a-zA-Z]', ExpMarkException)
        return self

    def build_df(self):
        self.data = pd.DataFrame.from_dict({
            'experian-score': [self.__experian_score__],
            'experian-score_probability_default': [self.__experian_score_probability_default__],
            'experian-score_percentile': [self.__experian_score_percentile__],
            'experian-mark': [self.__experian_mark__.upper()]
        })
        return self.data

    def build_predict_payload(self):
        self.predict_payload = {
            'experian-score': self.__experian_score__,
            'experian-score_probability_default': self.__experian_score_probability_default__,
            'experian-score_percentile': self.__experian_score_percentile__,
            'experian-mark': self.__experian_mark__.upper(),
            'prediction': self.predict_value,
            "client-id": self.__id__
        }
        return json.dumps(self.predict_payload)


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
