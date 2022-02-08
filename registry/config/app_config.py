import os
import platform

import gunicorn

gunicorn.SERVER_SOFTWARE = 'evil'

# SQL Server Config Database
DB_CONFIG = os.environ.get('DB_CONFIG')
if DB_CONFIG is None:
    DB_CONFIG = 'apzm'

DB_CONFIG_USER = os.environ.get('DB_CONFIG_USER')
if DB_CONFIG_USER is None:
    DB_CONFIG_USER = 'root'

DB_CONFIG_PWD = os.environ.get('DB_CONFIG_PWD')
if DB_CONFIG_PWD is None:
    DB_CONFIG_PWD = 'pwd1234'

LOG_LEVEL_CONSOLE = os.environ.get('LOG_LEVEL_CONSOLE')
if LOG_LEVEL_CONSOLE is None:
    LOG_LEVEL_CONSOLE = 'INFO'

PORT = os.environ.get('PORT')
if PORT is None:
    PORT = 5000

PORT_REGISTRY = os.environ.get('PORT_REGISTRY')
if PORT_REGISTRY is None:
    PORT_REGISTRY = 5002

DB_PORT = os.environ.get('DB_PORT')
if DB_PORT is None:
    DB_PORT = 3306

DB_IP = os.environ.get('DB_IP')
if DB_IP is None:
    if platform.system() == 'Windows':
        DB_IP = 'localhost'
    else:
        DB_IP = 'database'



ASNEF_PREDICTION_ENDPOINT = '/model/asnef/predict'
ASNEF_REGISTER_ENDPOINT = '/asnef/register'