from src.models.sqlite.interfaces.cliente_pessoa_fisica_repository import ClientePessoaFisicaInterface
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.controllers.interfaces.pessoa_fisica_consulta_saldo_controller import PessoaFisicaConsultarSaldoControllerInterface

class PessoaFisicaConsultarSaldoController(PessoaFisicaConsultarSaldoControllerInterface):
    def __init__(self, pessoa_fisica_repository: ClientePessoaFisicaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
    
    def consultar_saldo(self, nome_pessoa_fisica: dict) -> dict :
        consulta_saldo = self.__consultar_saldo_in_db(nome_pessoa_fisica)
        response = self.__format_response(consulta_saldo)
        return response

    def __consultar_saldo_in_db(self, pessoa_fisica: str) -> PessoaFisicaTable:
        try:
            saldo = self.__pessoa_fisica_repository.consultar_saldo(pessoa_fisica)
            return saldo
        except Exception as exception:
            raise exception
        
    def __format_response(self, pessoa_fisica: PessoaFisicaTable ) -> dict:
        return {
            "data": {
                "type": "PessoaFisica",
                "count": 1,
                "attributes": {
                    "nome_completo": pessoa_fisica.nome_completo,
                    "saldo": pessoa_fisica.saldo
                }
            }
         }
