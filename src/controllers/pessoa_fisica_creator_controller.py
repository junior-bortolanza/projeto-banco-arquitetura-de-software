from src.models.sqlite.interfaces.cliente_repository import ClienteInterface

class PessoaFisicaController:
    def __init__(self, pessoa_fisica_repository: ClienteInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float  )-> dict:
        self.__pessoa_fisica_repository.create(
            renda_mensal=renda_mensal,
            idade=idade,
            nome_completo=nome_completo,
            celular=celular,
            email=email,
            categoria=categoria,
            saldo=saldo

        )
    def consultar_saldo(self, nome_pessoa_fisica: str) -> None:
        try:
            saldo = self.__pessoa_fisica_repository.consultar_saldo(nome_pessoa_fisica)
            return saldo
        except Exception as exception:
            raise exception
    
    def realizar_saque(self, quantia: float, nome_pessoa_fisica: str) -> None:
        try:
            mensagem_saque = self.__pessoa_fisica_repository.realizar_saque(quantia, nome_pessoa_fisica)
            return mensagem_saque
        except Exception as exception:
            raise exception
    
    def extrato_bancario(self, nome_pessoa_fisica: str) -> None:
        try:
            extrato = self.__pessoa_fisica_repository.extrato_bancario(nome_pessoa_fisica)
            return extrato
        except Exception as exception:
            raise exception
