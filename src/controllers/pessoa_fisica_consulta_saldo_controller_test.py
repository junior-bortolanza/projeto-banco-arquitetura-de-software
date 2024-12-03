#pylint: disable=unused-argument
from .pessoa_fisica_consulta_saldo_controller import PessoaFisicaConsultarSaldoController

class MockPessoaFisica:
    def __init__(self, nome_completo, saldo):
        self.nome_completo = nome_completo
        self.saldo = saldo

class MockPessoaFisicaRepository:
    def consultar_saldo(self, nome_pessoa_fisica: str):
        pass

def test_consultar_saldo():
    nome_pessoa_fisica = {
        "nome_completo": "Junior Bortolanza",
        "saldo": 50000.0
    }
    controller = PessoaFisicaConsultarSaldoController(MockPessoaFisicaRepository())
    response = controller.consultar_saldo(nome_pessoa_fisica)

    expected_response = {
        "data":{
                "type": "PessoaFisica",
                "count": 1,
                "attributes": {
                    "nome_completo": "Junior Bortolanza",
                    "saldo": 50000.0
                    
                }
            }
        }

    assert response == expected_response
   
