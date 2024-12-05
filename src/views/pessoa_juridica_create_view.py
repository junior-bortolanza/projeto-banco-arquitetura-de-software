from src.controllers.interfaces.pessoa_juridica_create_controller import PessoaJuridicaControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaJuridicaCreateView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaControllerInterface):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_info = http_request.body
        body_response = self.__controller.create(pessoa_juridica_info)
        
        return HttpResponse(status_code=201, body=body_response)
