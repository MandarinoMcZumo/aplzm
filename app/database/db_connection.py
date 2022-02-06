import mariadb
import sys
import app.config.app_config as config


# Connect to MariaDB Platform
def connect_db():
    """
    Standard db connection
    :return:
    """
    try:
        conn = mariadb.connect(

            user=config.DB_CONFIG_USER,
            password=config.DB_CONFIG_PWD,
            host=config.DB_IP,
            port=config.DB_PORT,
            database=config.DB_CONFIG

        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
