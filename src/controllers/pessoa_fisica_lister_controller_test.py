from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController

class MockPessoaFisicaRepository:
    def list_pessoa_fisica(self):
        return [
            PessoaFisicaTable(nome_completo="Junior Bortolanza", id=1),
        ]

def test_list_pessoa_fisica():
    controller = PessoaFisicaListerController(MockPessoaFisicaRepository())
    response = controller.list()

    expected_response =  {
        "data": {
            "type": "PessoaFisica",
            "count": 1,
            "attributes": [
                { "nome_completo": "Junior Bortolanza", "id": 1}
            ]
        }
    }

    assert response == expected_response
