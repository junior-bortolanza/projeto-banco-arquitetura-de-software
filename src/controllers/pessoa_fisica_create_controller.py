from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.cliente_pessoa_fisica_repository import ClientePessoaFisicaInterface
from src.controllers.interfaces.pessoa_fisica_create_controller import PessoaFisicaControllerInterface

class PessoaFisicaCreateController(PessoaFisicaControllerInterface):
    def __init__(self, pessoa_fisica_repository: ClientePessoaFisicaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def create(self, pessoa_fisica_info: dict )-> dict:
        renda_mensal = pessoa_fisica_info["renda_mensal"]
        idade = pessoa_fisica_info["idade"]
        nome_completo =  pessoa_fisica_info["nome_completo"]
        celular = pessoa_fisica_info["celular"]
        email = pessoa_fisica_info["email"]
        categoria = pessoa_fisica_info["categoria"]
        saldo = pessoa_fisica_info["saldo"]

        self.__validate_nome_pessoa_fisica(idade, nome_completo, saldo)
        self.__create_pessoa_fisica_in_db( renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        formated_response = self.__format_response(pessoa_fisica_info)
        return formated_response

    def __validate_nome_pessoa_fisica(self, idade: int, nome_completo: str, saldo: float ) -> None:
        
        if not nome_completo and idade and saldo:
            raise HttpBadRequestError("Nome da pessoa fisica inválida!")
    
    def __create_pessoa_fisica_in_db(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo) -> None:
        self.__pessoa_fisica_repository.create_pessoa_fisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    def __format_response(self, pessoa_fisica_info: dict ) -> dict:
        return {
            "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": pessoa_fisica_info
              }
         }
