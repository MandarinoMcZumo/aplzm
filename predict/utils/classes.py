import json
from flask_restful import abort
import pandas as pd

import predict.utils.functions as f


class ApzmException(Exception):
    def __init__(self, error_message=None):
        self.__error__ = error_message

    pass


class PredictException(ApzmException):
    pass

def exception_handler(exc):
    if isinstance(exc, PredictException):
        err_code = "ERR905"
        description = "Something went wrong applying the prediction - " + str(exc.__error__)
    else:
        err_code = "ERR999"
        description = "Something went wrong - " + str(exc)

    return abort(403, success=False, message=err_code, description=description)
