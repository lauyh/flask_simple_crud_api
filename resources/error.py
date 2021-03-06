class InternalServerError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class UpdatingUserError(Exception):
    pass


class DeletingUserError(Exception):
    pass


class UserNotExistsError(Exception):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "UserAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UpdatingUserError": {
        "message": "Updating user added by other is forbidden",
        "status": 403
    },
    "DeletingUserError": {
        "message": "Deleting user added by other is forbidden",
        "status": 403
    },
    "UserNotExistsError": {
        "message": "User with given id doesn't exists",
        "status": 400
    },
}
