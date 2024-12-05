from abc import ABC, abstractmethod

class ClientePessoaJuridicaInteface(ABC):

    @abstractmethod
    def create_pessoa_juridica(self, 
                    faturamento: float, 
                    idade: int, 
                    nome_fantasia: str, 
                    celular: str, 
                    email_corporativo: str, 
                    categoria: str, 
                    saldo: float 
                ) -> None:
        pass

    @abstractmethod
    def sacar_dinheiro(self, quantia: float, pessoa_juridica: str) -> None:
        pass
    
    def list_pessoa_juridica(self) -> list:
        pass
