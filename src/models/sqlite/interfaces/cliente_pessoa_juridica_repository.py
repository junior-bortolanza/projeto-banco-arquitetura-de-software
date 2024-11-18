from abc import ABC, abstractmethod

class ClientePessoaJuridicaInteface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia: float, pessoa_juridica: str) -> None:
        pass

    @abstractmethod
    def consulta_saldo(self, pessoa_juridica: str) -> dict: 
        pass
