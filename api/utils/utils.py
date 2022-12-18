"""Contains common used util functions.
"""

import time

def current_milli_time():
    return int(round(time.time() * 1000))

def verify_contain_all_fields(obj, fields):
    """Verify a dict object contain all the fields.
    Args:
        obj: A dict object. 
        fields: Fields to be checked.
    """
    assert isinstance(obj, dict)
    assert isinstance(fields, list)

    for field in fields:
        if field not in obj:
            return False
    return True

def verify_contain_some_fields(obj, fields):
    """Verify a dict object contain at lest one of the fields.
    Args:
        obj: A dict object. 
        fields: Fields to be checked.
    """
    assert isinstance(obj, dict)
    assert isinstance(fields, list)

    for field in fields:
        if field in obj:
            return True
    return False