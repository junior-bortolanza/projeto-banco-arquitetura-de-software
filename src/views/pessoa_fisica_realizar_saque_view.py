from src.controllers.interfaces.pessoa_fisica_realizar_saque import PessoaFisicaRealizarSaqueControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaFisicaCreateView(ViewInterface):
    def __init__(self, controller: PessoaFisicaRealizarSaqueControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_info = http_request.param["pessoa_fisica_info"]
        body_response = self.__controller.realizar_saque(pessoa_fisica_info)

        return HttpResponse(status_code=200, body=body_response)
