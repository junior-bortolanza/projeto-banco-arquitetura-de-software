#pylint: disable=unused-argument
from .pessoa_juridica_consulta_saldo_controller import PessoaJuridicaConsultarSaldoController

class MockPessoaJuridica:
    def __init__(self, nome_fantasia, saldo):
        self.nome_fantasia = nome_fantasia
        self.saldo = saldo

class MockPessoaJuridicaRepository:
    def consultar_saldo(self, nome_pessoa_fantasia: str):
        return MockPessoaJuridica(nome_fantasia="Academy", saldo=50000.0)

def test_consultar_saldo():
    nome_pessoa_juridica = {
                "nome_fantasia":"Academy",
                "saldo": 50000.0
            }
    controller = PessoaJuridicaConsultarSaldoController(MockPessoaJuridicaRepository())
    response = controller.consultar_saldo(nome_pessoa_juridica)

    expected_response = {
        "data":{
                "type": "PessoaFisica",
                "count": 1,
                "attributes": {
                    "nome_fantasia":"Academy",
                    "saldo": 50000.0
            }
        }
    }

    assert response == expected_response
   
