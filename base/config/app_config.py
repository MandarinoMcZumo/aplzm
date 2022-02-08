import os
import platform

import gunicorn

gunicorn.SERVER_SOFTWARE = 'evil'

LOG_LEVEL_CONSOLE = os.environ.get('LOG_LEVEL_CONSOLE')
if LOG_LEVEL_CONSOLE is None:
    LOG_LEVEL_CONSOLE = 'INFO'

PORT = os.environ.get('PORT')
if PORT is None:
    PORT = 5000

__PORT_REGISTRY__ = os.environ.get('PORT_REGISTRY')
if __PORT_REGISTRY__ is None:
    __PORT_REGISTRY__ = 5002

__PORT_PREDICT__ = os.environ.get('PORT_PREDICT')
if __PORT_PREDICT__ is None:
    __PORT_PREDICT__ = 5001

__REGISTRY_URL__ = os.environ.get('REGISTRY_URL')
__PREDICT_URL__ = os.environ.get('PREDICT_URL')
if __REGISTRY_URL__ is None:
    if platform.system() == 'Windows':
        __REGISTRY_URL__ = 'http://localhost:' + str(__PORT_REGISTRY__)
        __PREDICT_URL__ = 'http://localhost:' + str(__PORT_PREDICT__)
    else:
        __REGISTRY_URL__ = 'http://register:' + str(__PORT_REGISTRY__)
        __PREDICT_URL__ = 'http://predict:' + str(__PORT_PREDICT__)

ASNEF_PREDICTION_ENDPOINT = __PREDICT_URL__ + '/model/asnef/predict'
ASNEF_REGISTER_ENDPOINT = __REGISTRY_URL__ + '/asnef/register'
