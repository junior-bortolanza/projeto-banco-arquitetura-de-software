from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController

class MockPessoaFisicaRepository:
    def list_pessoa_fisica(self):
        return [
            PessoaFisicaTable(id=32, nome_completo="Gelson Bortolanza Junior", saldo=50000.0),
        ]

def test_list_pessoa_fisica():
    controller = PessoaFisicaListerController(MockPessoaFisicaRepository())
    response = controller.list()

    expected_response =  {
        "data": {
            "type": "Pessoa Fisica",
            "count": 1,
            "attributes": [
                { "id": 32, "nome_completo": "Gelson Bortolanza Junior", "saldo": 50000.0}
            ]
        }
    }

    assert response == expected_response
