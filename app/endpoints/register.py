import datetime

from flask_restful import Resource
from app.database.db_connection import connect_db
import app.utils.classes as c


class ClientPredictions(Resource):
    def get(self, user_id):
        conn = connect_db()
        cursor = conn.cursor()
        try:
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
                # row = [str(i) for i in row if type(i)==datetime.datetime else i]
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
