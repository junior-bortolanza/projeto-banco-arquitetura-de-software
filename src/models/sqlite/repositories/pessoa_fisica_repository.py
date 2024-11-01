'''
REPOSITORIE RESPONSAVEL DAS AÇÕES COM O BANCO DE DADOS

EX: INSERIR NO DB, SELEÇÃO

'''
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_pessoa_fisica(self, nome_completo: str, idade: int, saldo: float) -> None:

        with self.__db_connection as database:
            try:
                dados_pessoa_fisica = PessoaFisicaTable(
                    nome_completo=nome_completo,
                    idade=idade,
                    saldo=saldo
                )
                database.session.add(dados_pessoa_fisica)
                database.session.commit()
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

    def delete_pessoa_fisica(self, nome_completo: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                    .query(PessoaFisicaTable)
                    .filter(PessoaFisicaTable.nome_completo == nome_completo)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
