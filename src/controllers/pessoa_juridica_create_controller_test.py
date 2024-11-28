import pytest
from .pessoa_juridica_create_controller import PessoaJuridicaController

class MockPessoaJuridicaRepository:
    def create_pessoa_juridica(self, faturamento: float, idade: int, nome_fantasia, celular, email_corporativo, categoria, saldo):
        pass

def test_create():
    pessoa_juridica_info = {
        "faturamento": 500000,
        "idade": 50,
        "nome_fantasia": "Junior Academy",
        "celular": "1599785215",
        "email_corporativo": "academy@gmail.com",
        "categoria": "Empresa",
        "saldo": 100000
    }
    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    response = controller.create(pessoa_juridica_info)

    print(response)
    assert response["data"]["type"] == "Pessoa Juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_juridica_info

def test_create_error():
    pessoa_juridica_info = {
        "faturamento": 5000000,
        "celular": "1599785215",
        "email": "academy@gmail.com",
        "categoria": "Empresa",

    }

    controller = PessoaJuridicaController(MockPessoaJuridicaRepository())
    
    with pytest.raises(Exception):
        controller.create(pessoa_juridica_info)
