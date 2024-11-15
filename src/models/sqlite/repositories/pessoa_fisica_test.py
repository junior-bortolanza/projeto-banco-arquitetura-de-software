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
                        PessoaFisicaTable(renda_mensal=5000.00, 
                                          idade=35, 
                                          nome_completo="João da Silva",
                                          celular="9999-8888", 
                                          email="joao@example.com",
                                          categoria="Categoria A", 
                                          saldo=10000.00
                                        ),
                        PessoaFisicaTable(renda_mensal=4000.00, 
                                          idade=45, 
                                          nome_completo="Maria Oliveira",
                                          celular="7777-6666", 
                                          email="maria@example.com",
                                          categoria="Categoria B", 
                                          saldo=15000.00)
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
    assert response[1].saldo == 15000.00

def test_list_pessoa_fisica_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoa_fisica()

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_consultar_saldo():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    pessoa_fisica = 'João da Silva'
    response = repo.consultar_saldo(pessoa_fisica)

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_once()
    mock_connection.session.first.assert_called_once()

    assert response == 10000.00

def test_sacar_dinheiro():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    quantia = 5000
    pessoa_fisica = "Maria Oliveira"
    repo.consultar_saldo(pessoa_fisica)
    response = repo.sacar_dinheiro(quantia, pessoa_fisica)

    assert response == "Saque de R$5000, realizado com sucesso. Saldo atual: R$5000.0"

def test_extrato_bancario():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    pessoa_fisica = "João da Silva"
    saldo = 10000.00
    categoria = "Categoria A"
    response = repo.extrato_bancario(pessoa_fisica)

    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    mock_connection.session.filter_by.assert_called_once()
    mock_connection.session.first.assert_called_once()
    
    assert response == {"Nome": pessoa_fisica, "Saldo": saldo, "Categoria": categoria}
