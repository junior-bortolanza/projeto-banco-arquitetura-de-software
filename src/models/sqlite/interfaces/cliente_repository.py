from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, quantia: float, pessoa_fisica: str) -> None:
        pass

    @abstractmethod    
    def extrato_bancario(self, pessoa_fisica: str) -> dict: 
        pass
