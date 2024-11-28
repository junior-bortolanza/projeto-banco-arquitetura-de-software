from abc import ABC, abstractmethod

class PessoaJuridicaListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> dict:
        pass
