from src.models.sqlite.interfaces.cliente_pessoa_fisica_repository import ClientePessoaFisicaInterface
from src.controllers.interfaces.pessoa_fisica_lister_controller import PessoaFisicaListerControllerInterface

class PessoaFisicaListerController(PessoaFisicaListerControllerInterface):
    def __init__(self, pessoa_fisica_repository: ClientePessoaFisicaInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def list(self) -> dict:
        pessoa_fisica = self.__get_pessoa_fisica_in_db()
        response = self.__format_response(pessoa_fisica)
        return response

    def __get_pessoa_fisica_in_db(self) -> list:
        pessoa_fisica = self.__pessoa_fisica_repository.list_pessoa_fisica()
        return pessoa_fisica

    def __format_response(self, pessoa_fisica: dict) -> dict:
        formated_pessoa_fisica = []
        
        for pessoa in pessoa_fisica:
            formated_pessoa_fisica.append({ 
                "nome_completo": pessoa.nome_completo, 
                "id": pessoa.id 
            })

        return {
            "data": {
                "type": "PessoaFisica",
                "count": len(formated_pessoa_fisica),
                "attributes": formated_pessoa_fisica
            }
        }
