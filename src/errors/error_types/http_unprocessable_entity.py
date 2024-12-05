class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str) -> None:
        self.status_code = 422
        self.name = 'UnprocessableEntity'
        self.message = message
