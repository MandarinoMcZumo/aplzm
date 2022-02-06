import app.utils.classes as c
import re
import joblib
from flask_restful import abort
from app.database.db_connection import connect_db


def string_validation(s, rgx, exc):
    """

    :param str s:
    :param str rgx:
    :return:
    """
    try:
        type_check = type(s) == str
        value_check = re.search(rgx, s)

        if not type_check or value_check is None:
            raise exc("Invalid mark value.")
    except Exception as e:
        raise exc(e)


def numeric_validation(num_value, param_type, param_range, exc):
    """

    :param num_value:
    :param class param_type:
    :param list param_range:
    :param  exc:
    :return: 
    """
    try:
        check_param_type = type(num_value) == param_type
        check_param_value = min(param_range) <= num_value <= max(param_range)

        if not check_param_type or not check_param_value:
            raise exc("Invalid value.")

    except Exception as e:
        raise exc(e)


def apply_prediction(df, model):
    """

    :param df:
    :param model:
    :return:
    """
    try:
        m = joblib.load(model)
        prediction = m.predict(df)[0]
        r_pred = round(prediction)
        return r_pred
    except Exception as e:
        return c.PredictException(e)


def register_prediction(client, prediction):
    conn = None
    cursor = None
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
        , {prediction}
        , '{client.__id__}'
        , {client.__experian_score__}
        , {client.__experian_score_probability_default__}
        , {client.__experian_score_percentile__}
        , '{client.__experian_mark__}'
        )
        """)
        # conn.commit()

    except Exception as e:
        raise c.RegisterException(e)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def exception_handler(exc):
    if isinstance(exc, c.ExpMarkException):
        err_code = "ERR901"
        description = "Paramater Experian Mark - " + str(exc.__error__)
    elif isinstance(exc, c.ExpScoreException):
        err_code = "ERR902"
        description = "Parameter Experian Score - " + str(exc.__error__)
    elif isinstance(exc, c.ExpScoreProbabilityException):
        err_code = "ERR903"
        description = "Parameter Experian Score Probability - " + str(exc.__error__)
    elif isinstance(exc, c.ExpPercentileException):
        err_code = "ERR904"
        description = "Parameter Experian Percentile - " + str(exc.__error__)
    elif isinstance(exc, c.PredictException):
        err_code = "ERR905"
        description = "Something went wrong applying the prediction - " + str(exc.__error__)
    elif isinstance(exc, c.ClientIdException):
        err_code = "ERR906"
        description = "Paramter ID - " + str(exc.__error__)
    else:
        err_code = "ERR999"
        description = "Something went wrong - " + str(exc)

    return abort(403, success=False, message=err_code, description=description)
