from abc import ABC, abstractmethod

class PessoaFisicaConsultarSaldoControllerInterface(ABC):

    @abstractmethod
    def consultar_saldo(self, nome_pessoa_fisica: dict) -> dict :
        pass
