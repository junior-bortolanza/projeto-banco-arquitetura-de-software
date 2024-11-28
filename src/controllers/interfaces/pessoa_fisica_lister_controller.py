from abc import ABC, abstractmethod

class PessoaFisicaListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> dict:
        pass
