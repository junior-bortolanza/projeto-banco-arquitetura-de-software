from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_repository import PessoaFisicaRepository


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaFisicaTable)],
                    [
                        PessoaFisicaTable(nome_completo="Pedro Santos", idade=28, saldo=8000.00),
                        PessoaFisicaTable(nome_completo="Maria Oliveira", idade=45, saldo=4000.00)
                    ]
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No results found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass



def test_list_pessoa_fisica():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoa_fisica()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[1].nome_completo == "Maria Oliveira"
    assert response[1].idade == 45
    assert response[1].saldo == 4000.00

def test_delete_pessoa_fisica():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)

    repo.delete_pessoa_fisica("PessoaFisica")

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter.assert_called_once_with(
                PessoaFisicaTable.nome_completo == "PessoaFisica"
            )
    mock_connection.session.delete.assert_called_once()

def test_list_pessoa_fisica_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoa_fisica()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []
