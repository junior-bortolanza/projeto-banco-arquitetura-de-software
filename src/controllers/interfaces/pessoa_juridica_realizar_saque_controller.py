from abc import ABC, abstractmethod

class PessoaJuridicaRealizarSaqueControllerInterface(ABC):
    
    @abstractmethod
    def realizar_saque(self, pessoa_juridica_info: dict) -> dict:
        pass
