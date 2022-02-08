from flask import request
from flask_restful import Resource
from predict.log.log_console import logger
import predict.config.app_config as config
import predict.utils.classes as c
import joblib
import pandas as pd
import os


class Asnef(Resource):

    def post(self):
        try:
            logger.info('Loading model...')
            payload = request.get_json()
            df = pd.read_json(payload['data'])
            m = joblib.load(config.ASNEF_MODEL)
            prediction = m.predict(df)[0]
            r_pred = round(prediction)
            return {"prediction": r_pred}

        except Exception as e:
            print(str(e))
            logger.error(str(e))
            logger.info(os.getcwd())
            return c.PredictException(e)
