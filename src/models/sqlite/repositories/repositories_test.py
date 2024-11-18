import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJuridicaRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoa_fisica()
    print(response)


@pytest.mark.skip(reason="interacao com o banco")
def test_create_pessoa_fisica(): 
    renda_mensal = 15000
    idade = 31
    nome_completo = "Gelson Bortolanza Junior"
    celular = "15-997378512"
    email = "junior@gmail.com"
    categoria = "Categoria A"
    saldo = 30000.00


    repo = PessoaFisicaRepository(db_connection_handler)
    
    repo.create_pessoa_fisica(renda_mensal,idade,nome_completo, celular, email, categoria, saldo )

@pytest.mark.skip(reason="interacao com o banco")
def test_get_pessoa_fisica():
    pessoa_fisica = 1

    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.get_pessoa_fisica(pessoa_fisica)
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_consulta_saldo_pessoa_fisica():
    pessoa_fisica = "Gelson Bortolanza Junior"

    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.consultar_saldo(pessoa_fisica)
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pessoa_juridica():
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.list_pessoa_juridica()
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_get_pessoa_juridica():
    nome_fantasia = 1

    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.get_pessoa_juridica(nome_fantasia)
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_create_pessoa_juridica():
    faturamento = 100000.00
    idade = 15
    nome_fantasia = "Junior Service"
    celular =  "15-981320321"
    email_corporativo = "junior@juniorservice.com"
    categoria =  "Categoria C"
    saldo = 30000.00
    
    repo = PessoaJuridicaRepository(db_connection_handler)
    response = repo.create_pessoa_juridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
    print()
    print(response)
