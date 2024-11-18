from abc import ABC, abstractmethod

class ClientePessoaFisicaInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia: float, pessoa_fisica: str) -> None:
        pass

    @abstractmethod    
    def consultar_saldo(self, pessoa_fisica: str) -> dict: 
        pass
