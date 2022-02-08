import registry.database.db_connection as db_conn
import registry.utils.classes as c


def initialize_db():
    conn = None
    cursor = None
    try:
        conn = db_conn.connect_db()
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute('CREATE DATABASE IF NOT EXISTS apzm;')
        cursor.execute('CREATE SCHEMA IF NOT EXISTS historic;')
        cursor.execute("""CREATE TABLE IF NOT EXISTS historic.ratings (
id VARCHAR(70) DEFAULT UUID(), 
registered_at DATETIME,
asnef_score INT,
client_id VARCHAR(50),
experian_score SMALLINT,
experian_score_probability_default FLOAT,
experian_score_percentile TINYINT,
experian_mark VARCHAR(10));""")
    except Exception as e:
        raise c.DBException("The DB could not be initialized - " + str(e))

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
