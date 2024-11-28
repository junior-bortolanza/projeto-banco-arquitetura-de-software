class HttpRequest:
    def __init__(self, body: dict = None, param: dict = None, headers: dict = None, url: dict = None) -> None:
        self.body = body
        self.parmm = param
        self.headers = headers
        self.url = url
