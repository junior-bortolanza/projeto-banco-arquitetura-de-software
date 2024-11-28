from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable
from .pessoa_juridica_repository import PessoaJuridicaRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PessoaJuridicaTable)],
                    [
                        PessoaJuridicaTable( faturamento= 100000.00, 
                                            idade=10, 
                                            nome_fantasia='Empresa XYZ', 
                                            celular='1111-2222', 
                                            email_corporativo='contato@empresa.com', 
                                            categoria='Categoria A',
                                            saldo=50000.00
                                        ),
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

def test_consultar_saldo():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    pessoa_juridica = "Empresa XYZ"
    response = repo.consultar_saldo(pessoa_juridica)

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.filter_by.assert_called_once()
    mock_connection.session.first.assert_called_once()

    assert response == 50000.00    

def test_sacar_dinheiro():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    quantia = 20000.0
    pessoa_juridica = 'Empresa XYZ'
    repo.consultar_saldo(pessoa_juridica)

    response = repo.sacar_dinheiro(quantia, pessoa_juridica)
    
    assert response == "Saque de R$20000.0, realizado com sucesso. Saldo atual: R$30000.0"
    
def test_list_pessoa_juridica():
    mock_connection = MockConnection()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.list_pessoa_juridica()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_fantasia == "Empresa XYZ"
    assert response[0].idade == 10
    assert response[0].saldo == 50000.00

def test_list_pessoa_juridica_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJuridicaRepository(mock_connection)
    response = repo.list_pessoa_juridica()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []
