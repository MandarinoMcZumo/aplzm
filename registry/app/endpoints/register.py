import datetime

from flask_restful import Resource
from flask_restful import request
from registry.database.db_connection import connect_db
import registry.utils.classes as c
import json


class ClientPredictions(Resource):
    def get(self, user_id):
        conn = None
        cursor = None
        try:
            conn = connect_db()
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

            return {"records": result}

        except Exception as e:
            raise c.RegisterException(e)

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
            conn = connect_db()
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

            return {"success": True}

        except Exception as e:
            print(str(e))

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
