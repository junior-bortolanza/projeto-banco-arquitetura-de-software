from src.models.sqlite.interfaces.cliente_pessoa_juridica_repository import ClientePessoaJuridicaInteface
from src.controllers.interfaces.pessoa_juridica_create_controller import PessoaJuridicaControllerInterface

class PessoaJuridicaController(PessoaJuridicaControllerInterface):
    def __init__(self, pessoa_juridica_repository: ClientePessoaJuridicaInteface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, pessoa_juridica_info: dict )-> dict:
        faturamento = pessoa_juridica_info["faturamento"]
        idade = pessoa_juridica_info["idade"]
        nome_fantasia =  pessoa_juridica_info["nome_fantasia"]
        celular = pessoa_juridica_info["celular"]
        email_corporativo = pessoa_juridica_info["email_corporativo"]
        categoria = pessoa_juridica_info["categoria"]
        saldo = pessoa_juridica_info["saldo"]

        self.__validate_nome_pessoa_juridica(nome_fantasia, idade, saldo)
        self.__create_pessoa_juridica_in_db( faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        formated_response = self.__format_response(pessoa_juridica_info)
        return formated_response

    def __validate_nome_pessoa_juridica(self, nome_fantasia: str, idade: int, saldo: float ) -> None:
        
        if not nome_fantasia and idade and saldo:
            raise Exception("Nome pessoa juridica inválida!")
    
    def __create_pessoa_juridica_in_db(self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo) -> None:
        self.__pessoa_juridica_repository.create_pessoa_juridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)

    def __format_response(self, pessoa_juridica_info: dict ) -> dict:
        return {
            "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": pessoa_juridica_info
              }
         }
