from src.models.sqlite.interfaces.cliente_pessoa_juridica_repository import ClientePessoaJuridicaInteface
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from src.controllers.interfaces.pessoa_juridica_consulta_saldo_controller import PessoaJuridicaConsultarSaldoControllerInterface

class PessoaJuridicaConsultarSaldoController(PessoaJuridicaConsultarSaldoControllerInterface):
    def __init__(self, pessoa_juridica_repository: ClientePessoaJuridicaInteface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository
    
    def consultar_saldo(self, nome_pessoa_juridica: dict) -> dict :
        consulta_saldo = self.__consultar_saldo_in_db(nome_pessoa_juridica)
        response = self.__format_response(consulta_saldo)
        return response

    def __consultar_saldo_in_db(self, nome_pessoa_juridica: str) -> PessoaJuridicaTable:
        try:
            saldo = self.__pessoa_juridica_repository.consultar_saldo(nome_pessoa_juridica)
            return saldo
        except Exception as exception:
            raise exception
        
    def __format_response(self, pessoa_juridica: PessoaJuridicaTable ) -> dict:
        return {
            "data": {
                "type": "PessoaFisica",
                "count": 1,
                "attributes": {
                    "nome_fantasia": pessoa_juridica.nome_fantasia,
                    "saldo": pessoa_juridica.saldo
                }
            }
         }
