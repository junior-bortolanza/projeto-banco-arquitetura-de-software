class HttpBadRequestError(Exception):

    def __init__(self, message: str) -> None:
        self.status_code = 400
        self.name = "BadRequest"
        self.message = message
