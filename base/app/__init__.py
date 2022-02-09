from base.log.log_console import logger

from flask import Flask
from flask_restful import Api
from flask_talisman import Talisman
import base.app.endpoints.predict as pdct
import base.app.endpoints.register as rgs


def create_app():
    """
        Create a new Flask App with Configuration file or Default Config if is None.

    :param config: Name of the configuation file
    :return: New Flask App Instance
    """

    # Only to debug
    logger.debug('Starting v1 BASE API ... ')

    # instantiate the base
    app = Flask(__name__)
    Talisman(app, force_https=False)
    api = Api(app)

    api.add_resource(pdct.Asnef, '/model/asnef/predict/<string:user_id>')
    api.add_resource(rgs.Registry, '/asnef/register/<string:user_id>')
    return app


# For Unicorn
app = create_app()
