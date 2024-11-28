from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_lister_controller import PessoaJuridicaListerControlle

class MockPessoaJuridicaRepository:
    def list_pessoa_juridica(self):
        return [
            PessoaJuridicaTable(nome_fantasia="Academy", id=1),
        ]

def test_list_pessoa_juridica():
    controller = PessoaJuridicaListerControlle(MockPessoaJuridicaRepository())
    response = controller.list()

    expected_response =  {
        "data": {
            "type": "Pessoa Juridica",
            "count": 1,
            "attributes": [
                { "nome_fantasia": "Academy", "id": 1}
            ]
        }
    }

    assert response == expected_response
