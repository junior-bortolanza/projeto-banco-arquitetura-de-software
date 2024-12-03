from src.controllers.interfaces.pessoa_fisica_consulta_saldo_controller import PessoaFisicaConsultarSaldoControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PessoaFisicaConsultaSaldoView(ViewInterface):
    def __init__(self, controller: PessoaFisicaConsultarSaldoControllerInterface):
        self.__controller = controller
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response =  self.__controller.consultar_saldo()
        return HttpResponse(status_code=201, body=body_response)
