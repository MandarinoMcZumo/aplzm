from flask import request
from flask_restful import Resource
from app.log.log_console import logger
from app.utils.classes import Client
import app.config.app_config as config
import app.utils.functions as f


class Asnef(Resource):

    def post(self, user_id):
        try:
            logger.debug('Starting new prediction')
            payload = request.get_json()
            client = Client(user_id, payload)
            predict_values = client.validate_attrs().build_df()

            prediction = f.apply_prediction(predict_values, config.MODEL_PATH)
            client.predict_value = prediction

            f.register_prediction(client, prediction)

            return {"asnef-score": prediction}

        except Exception as e:
            f.exception_handler(e)
