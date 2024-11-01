import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoa_fisica()
    print(response)

def test_delete_pessoa_fisica():
    nome_completo = "Pedro Santos"
    repo = PessoaFisicaRepository(db_connection_handler)
    repo.delete_pessoa_fisica(nome_completo)
