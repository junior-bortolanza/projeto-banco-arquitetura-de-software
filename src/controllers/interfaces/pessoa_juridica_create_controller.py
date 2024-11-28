from abc import ABC, abstractmethod

class PessoaJuridicaControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_juridica_info: dict )-> dict:
        pass
