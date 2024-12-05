from abc import ABC, abstractmethod

class ClientePessoaFisicaInterface(ABC):

    @abstractmethod
    def create_pessoa_fisica(
                self, 
                renda_mensal: str, 
                idade: int, 
                nome_completo: str,
                celular: str, 
                email: str, 
                categoria: str, 
                saldo
            ) -> None:
        pass

    @abstractmethod
    def sacar_dinheiro(self, quantia: float, pessoa_fisica: str) -> None:
        pass

    def list_pessoa_fisica(self) -> list:
        pass
