import mariadb
import sys
import registry.config.app_config as config


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
    except Exception as e:
        print(f"Error connecting to MariaDB Platform: {str(e)}")
        sys.exit(1)
