import time

def current_milli_time():
    return int(round(time.time() * 1000))

def verify_contain_all_fields(obj, fields):
    assert isinstance(obj, dict)
    for field in fields:
        if field not in obj:
            return False
    return True

def verify_contain_some_fields(obj, fields):
    assert isinstance(obj, dict)
    for field in fields:
        if field in obj:
            return True
    return False
