from flask import request
from flask_restful import Resource
from predict.log.log_console import logger
import predict.config.app_config as config
import predict.utils.classes as c
import joblib
import pandas as pd


class Asnef(Resource):

    def post(self):
        try:
            logger.info('Loading Asnef model...')
            payload = request.get_json()
            df = pd.read_json(payload['data'])
            m = joblib.load(config.ASNEF_MODEL)
            prediction = m.predict(df)[0]
            r_pred = round(prediction)
            logger.info('Asnef Prediction - SUCCESS')
            return {"prediction": r_pred}

        except Exception as e:
            return c.exception_handler(e)
