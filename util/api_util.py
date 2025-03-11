import datetime
from calendar import monthrange
from dateutil.relativedelta import relativedelta
from fastapi import HTTPException


def success():
    return {"response_code": 200, "response_message": "Success"}


def delete():
    return {"response_code": 200, "response_message": "Delete"}


def failure():
    return {"response_code": 400, "response_message": "Failure"}


def unknown_failure():
    return {"response_code": 400, "response_message": "Unknown Failure"}


def param_missing():
    return {"response_code": 400, "response_message": "Parameter Missing"}


def session_timeout():
    return {
        "response_code": 400,
        "response_message": "Session Timeout",
        "custom_message": "Session Timeout. Please login again!",
    }


def internal_error():
    return {
        "response_code": 500,
        "response_message": "Internal server error",
        "custom_message": "Internal server error. Please contact Admin!",
    }


def database_error():
    return {"response_code": 109, "response_message": "Database error"}


def object_as_array_map(data_object=None):
    try:
        if isinstance(data_object, list):
            return [object_as_array_map(item) for item in data_object if item is not None]
        elif hasattr(data_object, "getPublicValue"):
            return data_object.getPublicValue()
        else:
            return data_object
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to construct object to map: {str(e)}")


def get_value(json_object=None, key=""):
    return json_object.get(key, None) if json_object else None


def get_date_range(since=None, till=None):
    try:
        if not till:
            till = datetime.datetime.today()
        else:
            till = datetime.datetime.strptime(till, "%Y-%m-%d")

        if not since:
            since = till - relativedelta(days=6)
        else:
            since = datetime.datetime.strptime(since, "%Y-%m-%d")

        till = till + relativedelta(days=1, seconds=-1)
        return since, till
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")


def get_date_range_by_month(year=None, month=None):
    today = datetime.date.today()
    year = year or today.year
    month = month or today.month

    if month <= 0:
        year -= 1
        month = 12 - abs(month)

    _, num_days = monthrange(year, month)
    since = datetime.datetime(year, month, 1)
    till = datetime.datetime(year, month, num_days, 23, 59, 59)

    return since, till
