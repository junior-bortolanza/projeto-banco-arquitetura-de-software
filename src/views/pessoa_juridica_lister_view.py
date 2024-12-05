from src.controllers.interfaces.pessoa_juridica_lister_controller import PessoaJuridicaListerControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaJuridicaListerView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaListerControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)
