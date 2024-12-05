from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_lister_controller import PessoaJuridicaListerController

class MockPessoaJuridicaRepository:
    def list_pessoa_juridica(self):
        return [
            PessoaJuridicaTable(id=1, nome_fantasia="Academy", saldo=15000.0 ),
        ]

def test_list_pessoa_juridica():
    controller = PessoaJuridicaListerController(MockPessoaJuridicaRepository())
    response = controller.list()

    expected_response =  {
        "data": {
            "type": "Pessoa Juridica",
            "count": 1,
            "attributes": [{
                "id": 1,
                "nome_fantasia": "Academy",
                "saldo": 15000.0  
            }]
        }
    }

    assert response == expected_response
