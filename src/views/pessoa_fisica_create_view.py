from src.controllers.interfaces.pessoa_fisica_create_controller import PessoaFisicaControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaFisicaCreateView(ViewInterface):
    def __init__(self, controller: PessoaFisicaControllerInterface):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_info = http_request.body
        body_response = self.__controller.create(pessoa_fisica_info)
        
        return HttpResponse(status_code=201, body=body_response)
