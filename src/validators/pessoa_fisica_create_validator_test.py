from .pessoa_fisica_create_validator import pessoa_fisica_create_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_pessoa_fisica_create_validator():
    request = MockRequest({
        "renda_mensal": 30000.0,
        "idade": 32,
        "nome_completo": "Junior Bortolanza",
        "celular": "15-45455454",
        "email": "junior@gmail.com",
        "categoria": "Categoria A",
        "saldo": 1500.0
    })
    
    pessoa_fisica_create_validator(request)
