from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaFisicaView(ViewInterface):
    def __init__(self, controller):
        self.controller = controller
        

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
        
