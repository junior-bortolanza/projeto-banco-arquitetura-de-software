import pytest
from .pessoa_fisica_create_controller import PessoaFisicaCreateController

class MockPessoaFisicaRepository:
    def create_pessoa_fisica(self, renda_mensal: float, idade: int, nome_completo, celular, email, categoria, saldo):
        pass

def test_create():
    pessoa_fisica_info = {
        "renda_mensal": 150000,
        "idade": 31,
        "nome_completo": "Junior Bortolanza",
        "celular": "1599785215",
        "email": "junior@gmail.com",
        "categoria": "Categoria A",
        "saldo": 30000.0
    }
    controller = PessoaFisicaCreateController(MockPessoaFisicaRepository())
    response = controller.create(pessoa_fisica_info)

    print(response)
    assert response["data"]["type"] == "Pessoa Fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_fisica_info

def test_create_error():
    pessoa_fisica_info = {
        "renda_mensal": 150000,
        "celular": "1599785215",
        "email": "junior@gmail.com",
        "categoria": "Categoria A",

    }

    controller = PessoaFisicaCreateController(MockPessoaFisicaRepository())
    
    with pytest.raises(Exception):
        controller.create(pessoa_fisica_info)
