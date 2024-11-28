from src.models.sqlite.interfaces.cliente_pessoa_fisica_repository import ClientePessoaFisicaInterface
from src.controllers.interfaces.pessoa_fisica_realizar_saque import PessoaFisicaRealizarSaqueControllerInterface

class PessoaFisicaRealizarSaqueController(PessoaFisicaRealizarSaqueControllerInterface):
    def __init__(self, pessoa_fisica_repository: ClientePessoaFisicaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository
        
    def realizar_saque(self, pessoa_fisica_info: dict) -> dict:
        nome_completo = pessoa_fisica_info["nome_completo"]
        quantia = pessoa_fisica_info["quantia"]

        self.__validate_input(nome_completo, quantia)

        self.__sacar_dinheiro_in_db(nome_completo, quantia)
        formated_response = self.__format_response(pessoa_fisica_info)
        return formated_response



    def __validate_input(self, nome_completo: str, quantia: float) ->None:
        if not nome_completo or not quantia:
            raise Exception("Invalid input")

    def __sacar_dinheiro_in_db(self, quantia: float, pessoa_fisica: str) -> None:
        try:
            mensagem_saque = self.__pessoa_fisica_repository.sacar_dinheiro(quantia, pessoa_fisica)
            return mensagem_saque
        except Exception as exception:
            raise exception

    def __format_response(self, pessoa_fisica_info: dict) -> dict:
        return {
            "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": pessoa_fisica_info
            }
        }
