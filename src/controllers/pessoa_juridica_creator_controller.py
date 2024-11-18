from src.models.sqlite.interfaces.cliente_pessoa_juridica_repository import ClientePessoaJuridicaInteface

class PessoaJuridicaController:
    def __init__(self, pessoa_juridica_repository: ClientePessoaJuridicaInteface ):
        self.__pessoa_juridica_repository = pessoa_juridica_repository
    
    def create(self,faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float ):
        self.__pessoa_juridica_repository.create(
            faturamento=faturamento, 
            idade=idade,
            nome_fantasia=nome_fantasia, 
            celular=celular,
            email_corporativo=email_corporativo, 
            categoria=categoria,
            saldo=saldo
        )
    
    def consultar_saldo(self, nome_pessoa_juridica: str) -> None:
        try: 
            saldo = self.__pessoa_juridica_repository.consulta_saldo(nome_pessoa_juridica)
            return saldo
        except Exception as exception:
            raise exception

    def realizar_saque(self, quantia: float, nome_pessoa_juridica: str) -> None:
        try:
            mensagem_saque = self.__pessoa_juridica_repository.sacar_dinheiro(quantia, nome_pessoa_juridica)
            return mensagem_saque
        except Exception as exception:
            raise exception
