from .pessoa_fisica_controller import PessoaFisicaController

class MockPessoaFisica:
    def __init__(self, pessoa_fisica):
        self.pessoa_fisica = pessoa_fisica

    def consultar_saldo(self, pessoa_fisica):
        self.pessoa_fisica = pessoa_fisica
        saldo = 30000
        return saldo

def test_consultar_saldo():
    pessoa_fisica = "Junior"
    controller = PessoaFisicaController(MockPessoaFisica("Junior"))
    response = controller.consultar_saldo(pessoa_fisica)

    assert response ==  30000
    assert response is not None
