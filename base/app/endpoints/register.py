import base.utils.functions as f

from flask_restful import Resource
import base.utils.classes as c
import base.config.app_config as config


class Registry(Resource):
    def get(self, user_id):
        try:
             registry = f.request_registry(config.ASNEF_REGISTER_ENDPOINT + f'/{user_id}')
             return {"registry": registry}

        except Exception as e:
            raise c.RegisterException(e)
