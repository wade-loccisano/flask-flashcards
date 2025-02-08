from flask import Response
from werkzeug.wrappers import Response as ResponseType


class BadRequestException(Exception):
    def __init__(self, message):
        super().__init__(message)


def bad_request(exception) -> ResponseType:
    print("bad request")
    return Response(response=str(exception), status=400)
