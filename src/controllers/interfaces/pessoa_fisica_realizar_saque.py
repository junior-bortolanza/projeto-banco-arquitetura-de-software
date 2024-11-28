from abc import ABC, abstractmethod

class PessoaFisicaRealizarSaqueControllerInterface(ABC):
    
    @abstractmethod
    def realizar_saque(self, pessoa_fisica_info: dict) -> dict:
        pass
