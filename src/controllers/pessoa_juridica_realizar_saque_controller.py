from src.models.sqlite.interfaces.cliente_pessoa_juridica_repository import ClientePessoaJuridicaInteface
from src.controllers.interfaces.pessoa_juridica_realizar_saque_controller import PessoaJuridicaRealizarSaqueControllerInterface

class PessoaJuridicaRealizarSaqueController(PessoaJuridicaRealizarSaqueControllerInterface):
    def __init__(self, pessoa_juridica_repository: ClientePessoaJuridicaInteface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository
        
    def realizar_saque(self, pessoa_juridica_info: dict) -> dict:
        nome_fantasia = pessoa_juridica_info["nome_fantasia"]
        quantia = pessoa_juridica_info["quantia"]

        self.__validate_input(nome_fantasia, quantia)

        self.__sacar_dinheiro_in_db(nome_fantasia, quantia)
        formated_response = self.__format_response(pessoa_juridica_info)
        return formated_response



    def __validate_input(self, nome_fantasia: str, quantia: float) ->None:
        if not nome_fantasia or not quantia:
            raise Exception("Invalid input")

    def __sacar_dinheiro_in_db(self, quantia: float, pessoa_juridica: str) -> None:
        try:
            mensagem_saque = self.__pessoa_juridica_repository.sacar_dinheiro(quantia, pessoa_juridica)
            return mensagem_saque
        except Exception as exception:
            raise exception

    def __format_response(self, pessoa_juridica_info: dict) -> dict:
        return {
            "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": pessoa_juridica_info
            }
        }
