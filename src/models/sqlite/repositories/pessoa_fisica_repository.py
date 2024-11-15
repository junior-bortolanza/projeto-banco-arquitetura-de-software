'''
REPOSITORIE RESPONSAVEL DAS AÇÕES COM O BANCO DE DADOS

EX: INSERIR NO DB, SELEÇÃO

'''

from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.cliente_repository import ClienteInterface

class PessoaFisicaRepository(ClienteInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_pessoa_fisica(
                self, 
                renda_mensal: str, 
                idade: int, 
                nome_completo: str,
                celular: str, 
                email: str, 
                categoria: str, 
                saldo
            ) -> None:

        with self.__db_connection as database:
            try:
                pessoa_fisica = PessoaFisicaTable(                 
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_fisica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def consultar_saldo(self, pessoa_fisica: str) -> PessoaFisicaTable:
        with self.__db_connection as database:
            try:
                consultar = (database.session
                .query(PessoaFisicaTable)
                .filter_by(nome_completo=pessoa_fisica)
                .first()
            )
                return consultar.saldo
            
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def sacar_dinheiro(self, quantia: float, pessoa_fisica: str) -> None:
        limite_saque = 8000.00

        saldo = self.consultar_saldo(pessoa_fisica)

        if quantia > limite_saque:
            raise Exception("Error :(: Valor excede o limite para saque!")
        
        elif quantia > saldo:
            raise Exception("Error: Saldo Insuficiente!")       
        else:
            saldo -= quantia
            return f"Saque de R${quantia}, realizado com sucesso. Saldo atual: R${saldo}"
    
        
    def extrato_bancario(self, pessoa_fisica: str) -> dict:
        with self.__db_connection as database:
            try:

                extrato_pessoa_fisica = (database.session
                .query(PessoaFisicaTable)
                .filter_by(nome_completo=pessoa_fisica)
                .first()
            )
                return {
                    "Nome": extrato_pessoa_fisica.nome_completo,
                    "Saldo": extrato_pessoa_fisica.saldo,
                    "Categoria": extrato_pessoa_fisica.categoria
                }
            
            except Exception as exception:
                database.session.rollback()
                raise exception    

    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(PessoaFisicaTable).all()
                return pessoa_fisica
            except NoResultFound:
                return []

    def get_pessoa_fisica(self, pessoa_fisica_id: int) -> PessoaFisicaTable:
        with self.__db_connection as database:
            try:
                pessoa_fisica = (
                    database.session
                    .query(PessoaFisicaTable)
                    .filter(PessoaFisicaTable.id == pessoa_fisica_id)
                    .one()
                )
                return pessoa_fisica
            except NoResultFound:
                return "Pessoa fisica nao cadastrada"
