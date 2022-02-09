from registry.log.log_console import logger
import registry.app.endpoints.register as rgs
import registry.utils.functions as f

from flask import Flask
from flask_restful import Api
from flask_talisman import Talisman


def create_app():
    """
        Create a new Flask App with Configuration file or Default Config if is None.

    :param config: Name of the configuation file
    :return: New Flask App Instance
    """

    # Only to debug
    logger.debug('Starting v1 Registry API ... ')

    # instantiate the base
    app = Flask(__name__)
    Talisman(app, force_https=False)
    api = Api(app)
    api.add_resource(rgs.ClientPredictions, '/asnef/register/<string:user_id>')
    return app


# For Unicorn
app = create_app()
