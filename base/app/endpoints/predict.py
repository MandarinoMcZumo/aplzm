from flask import request
from flask_restful import Resource
from base.log.log_console import logger
from base.utils.classes import Client
from base.config import app_config as config
import base.utils.functions as f
import base.utils.classes as c


class Asnef(Resource):

    def post(self, user_id):
        try:
            logger.debug('Starting new prediction')
            payload = request.get_json()
            client = Client(user_id, payload)
            predict_values = client.validate_attrs().build_df()
            logger.debug(predict_values)

            prediction = f.request_prediction(config.ASNEF_PREDICTION_ENDPOINT, predict_values)

            client.predict_value = prediction

            f.request_new_record(config.ASNEF_REGISTER_ENDPOINT, client)

            return {"asnef-score": prediction}

        except Exception as e:
            c.exception_handler(e)
