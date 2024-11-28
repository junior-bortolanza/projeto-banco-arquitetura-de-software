from src.controllers.pessoa_juridica_realizar_saque_controller import PessoaJuridicaRealizarSaqueController

class MockPessoaJuridicaSaqueRepository:
    
    def sacar_dinheiro(self, pessoa_juridica_info:dict):
        pass


def test_sacar_dinheiro():
    pessoa_juridica_info = {
        "nome_fantasia": "Academy Company",
        "quantia": 4500
    }
    controller = PessoaJuridicaRealizarSaqueController(MockPessoaJuridicaSaqueRepository)
    response = controller.realizar_saque(pessoa_juridica_info)
    expected_response = {
            "data": {
                "type": "Pessoa Juridica",
                "count": 1,
                "attributes": {
                        "nome_fantasia": "Academy Company",
                        "quantia": 4500
                }
            }
        }
    print(response)
    assert response == expected_response
