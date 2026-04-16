from datetime import datetime

class TaskError(Exception):
    pass

class InvalidPriorityError(TaskError):
    pass

class InvalidDateError(TaskError):
    pass

class InvalidNameError(TaskError):
    pass

def validate_name_task(name):
    if not name:
        raise InvalidNameError("Name can't be empty")

def validate_priority(priority):
    if priority not in("low", "medium", "high"):
        raise InvalidPriorityError("Priority must be low, medium or high")

def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise InvalidDateError("Invalid date format")
