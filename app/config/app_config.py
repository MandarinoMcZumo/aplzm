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
    PORT = 5005

DB_PORT = os.environ.get('DB_PORT')
if DB_PORT is None:
    DB_PORT = 3306

DB_IP = os.environ.get('DB_IP')
if DB_IP is None:
    DB_IP = '127.0.0.1'

MODEL_PATH = os.environ.get('MODEL_PATH')
if MODEL_PATH is None:
    if platform.system() == 'Windows':
        MODEL_PATH = 'app\\resources\\models\\asnef_inference.pkl'
    else:
        MODEL_PATH = 'app/resources/models/asnef_inference.pkl'
