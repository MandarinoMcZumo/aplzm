import datetime

from flask_restful import Resource
from flask_restful import request
import registry.database.db_connection as db_conn
import registry.utils.classes as c
import registry.utils.functions as f
from registry.log.log_console import logger
import json


class ClientPredictions(Resource):
    def get(self, user_id):
        conn = None
        cursor = None
        try:
            logger.info(f"Getting records for user {user_id}")
            f.initialize_db()
            conn = db_conn.connect_db()
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT 
                registered_at
                , asnef_score
            FROM historic.ratings
            WHERE client_id = '{user_id}'
            ORDER BY registered_at DESC
            """)
            result = []
            for row in cursor:
                row = list(map(lambda x: str(x) if type(x) == datetime.datetime else x, row))
                result.append((dict(zip(['registered_at', 'asnef_score'], row))))

            logger.info(f"Records user {user_id} - SUCCESS")
            return {"records": result}

        except Exception as e:
            c.exception_handler(e)

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def post(self, user_id):
        conn = None
        cursor = None
        payload = json.loads(request.get_json()['data'])
        r = c.NewRecord(payload)

        try:
            logger.info(f"New registry request for user {user_id}")
            f.initialize_db()
            conn = db_conn.connect_db()
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO historic.ratings (registered_at
            , asnef_score
            , client_id
            , experian_score
            , experian_score_probability_default
            , experian_score_percentile
            , experian_mark) 
            VALUES (
            UTC_TIMESTAMP()
            , {r.predict_value}
            , '{r.id}'
            , {r.experian_score}
            , {r.experian_score_probability_default}
            , {r.experian_score_percentile}
            , '{r.experian_mark}'
            )
            """)
            logger.info(f"New record for user {user_id} - SUCCESS")
            return {"success": True}

        except Exception as e:
            c.exception_handler(e)

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
