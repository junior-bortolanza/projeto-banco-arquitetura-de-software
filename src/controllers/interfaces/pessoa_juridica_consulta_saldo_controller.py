from abc import ABC, abstractmethod

class PessoaJuridicaConsultarSaldoControllerInterface(ABC):
    
    @abstractmethod
    def consultar_saldo(self, nome_pessoa_juridica: dict) -> dict :
        pass
