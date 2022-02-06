import pandas as pd

import app.utils.functions as f


class Client:
    def __init__(self, client_id, payload):
        self.__id__ = client_id
        self.__experian_score__ = payload['experian-score']
        self.__experian_score_probability_default__ = payload['experian-score_probability_default']
        self.__experian_score_percentile__ = payload['experian-score_percentile']
        self.__experian_mark__ = payload['experian-mark']
        self.data = None
        self.predict_value = None

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

