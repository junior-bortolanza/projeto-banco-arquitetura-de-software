'''
REPOSITORIE RESPONSAVEL DAS AÇÕES COM O BANCO DE DADOS

EX: INSERIR NO DB, SELEÇÃO

'''
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pessoa_fisica(self) -> list:
        with self.__db_connection as database:
            try:
                pessoa_fisica = database.session.query(PessoaFisicaTable).all()
                return pessoa_fisica
            except NoResultFound:
                return []
