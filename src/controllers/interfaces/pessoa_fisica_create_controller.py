from abc import ABC, abstractmethod

class PessoaFisicaControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_fisica_info: dict )-> dict:
        pass
