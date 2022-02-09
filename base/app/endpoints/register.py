import base.utils.functions as f

from flask_restful import Resource
import base.utils.classes as c
import base.config.app_config as config
from base.log.log_console import logger


class Registry(Resource):
    def get(self, user_id):
        try:
            logger.info(f"Starting get registry request for user {user_id}")
            registry = f.request_registry(config.ASNEF_REGISTER_ENDPOINT + f'/{user_id}')

            logger.info(f"Registry request for user {user_id} - SUCCESS")
            return {"registry": registry}

        except Exception as e:
            raise c.RegisterException(e)
