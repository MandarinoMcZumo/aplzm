import re


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
