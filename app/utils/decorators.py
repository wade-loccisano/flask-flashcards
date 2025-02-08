from flask import request
from functools import wraps
from werkzeug.exceptions import BadRequest
from app.utils.exceptions import BadRequestException
from app.utils.validators.deck import validate_create_deck


def validate_json(ignore_methods=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if ignore_methods is not None:
                for method in ignore_methods:
                    if request.method == method:
                        return f(*args, **kwargs)
            try:
                data = request.form
                if data is None:
                    raise BadRequest
            except BadRequest:
                raise BadRequestException("Invalid JSON.")
            if request.method == "POST":
                validate_create_deck(data)
            return f(*args, **kwargs)

        return wrapper

    return decorator
