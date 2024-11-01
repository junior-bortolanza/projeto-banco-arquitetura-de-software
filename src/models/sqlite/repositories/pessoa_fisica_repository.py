'''
REPOSITORIE RESPONSAVEL DAS AÇÕES COM O BANCO DE DADOS

EX: INSERIR NO DB, SELEÇÃO

'''
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoa_fisica(self) -> list[PessoaFisicaTable]:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(PessoaFisicaTable).all()
                return pessoa_fisica
            except NoResultFound:
                return []

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
