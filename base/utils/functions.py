import json
import re
import requests


def string_validation(s, rgx, exc):
    """

    :param str s:
    :param str rgx:
    :param ApzmException exc:
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
    :param param_type:
    :param list param_range:
    :param ApzmException exc:
    :return: 
    """
    try:
        check_param_type = type(num_value) == param_type
        check_param_value = min(param_range) <= num_value <= max(param_range)

        if not check_param_type or not check_param_value:
            raise exc("Invalid value.")

    except Exception as e:
        raise exc(e)


def request_prediction(endpoint, df):
    """

    :param str endpoint:
    :param pd.Dataframe df:
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": df.to_json()})

    response = requests.request('post', endpoint, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()['prediction']
    else:
        raise Exception


def request_registry(endpoint):
    """

    :param str endpoint:
    """

    response = requests.request('get', endpoint)
    if response.status_code == 200:

        return response.json()['records']
    else:
        raise Exception


def request_new_record(endpoint, data):
    """

    :param endpoint:
    :param Client data:
    :return:
    """
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"data": data.build_predict_payload()})
    url = '/'.join((endpoint, data.__id__))
    response = requests.request('post', url, headers=headers, data=payload)
    if response.status_code == 200:
        pass
    else:
        raise Exception
