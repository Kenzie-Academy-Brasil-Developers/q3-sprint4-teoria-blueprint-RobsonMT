from http import HTTPStatus

def return_hello():
    return {"data": "hello"}, HTTPStatus.OK
