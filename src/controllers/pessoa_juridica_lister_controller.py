from src.models.sqlite.interfaces.cliente_pessoa_juridica_repository import ClientePessoaJuridicaInteface
from src.controllers.interfaces.pessoa_juridica_lister_controller import PessoaJuridicaListerControllerInterface

class PessoaJuridicaListerControlle(PessoaJuridicaListerControllerInterface):
    def __init__(self, pessoa_juridica_repository: ClientePessoaJuridicaInteface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def list(self) -> dict:
        pessoa_juridica = self.__get_pessoa_juridica_in_db()
        response = self.__format_response(pessoa_juridica)
        return response

    def __get_pessoa_juridica_in_db(self) -> list:
        pessoa_juridica = self.__pessoa_juridica_repository.list_pessoa_juridica()
        return pessoa_juridica

    def __format_response(self, pessoa_juridica: dict) -> dict:
        formated_pessoa_juridica = []
        
        for pj in pessoa_juridica:
            formated_pessoa_juridica.append({ 
                "nome_fantasia": pj.nome_fantasia, 
                "id": pj.id 
            })

        return {
            "data": {
                "type": "Pessoa Juridica",
                "count": len(formated_pessoa_juridica),
                "attributes": formated_pessoa_juridica
            }
        }
