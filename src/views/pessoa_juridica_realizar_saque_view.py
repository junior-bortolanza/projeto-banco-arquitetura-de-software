from src.controllers.interfaces.pessoa_juridica_realizar_saque_controller import PessoaJuridicaRealizarSaqueControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaJuridicaRealizarSaqueView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaRealizarSaqueControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_info = http_request.body
        body_response = self.__controller.realizar_saque(pessoa_juridica_info)

        return HttpResponse(status_code=200, body=body_response)
