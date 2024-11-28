from src.controllers.pessoa_fisica_realizar_saque import PessoaFisicaRealizarSaqueController

class MockPessoaFisicaSaqueRepository:
    
    def sacar_dinheiro(self, pessoa_fisica_info:dict):
        pass


def test_sacar_dinheiro():
    pessoa_fisica_info = {
        "nome_completo": "Junior Bortolanza",
        "quantia": 40.0
    }
    controller = PessoaFisicaRealizarSaqueController(MockPessoaFisicaSaqueRepository)
    response = controller.realizar_saque(pessoa_fisica_info)
    expected_response = {
            "data": {
                "type": "Pessoa Fisica",
                "count": 1,
                "attributes": {
                    "nome_completo": "Junior Bortolanza",
                    "quantia": 40.0
                }
            }
        }
    print(response)
    assert response == expected_response
   
