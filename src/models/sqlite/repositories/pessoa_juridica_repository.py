from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridica import PessoaJuridicaTable

class PessoaJuridicaRepository:
    def __init__(self, db_connection ) -> None:
        self.__db_connection = db_connection

    def create_pessoa_juridica(self, 
                    faturamento: float, 
                    idade: int, 
                    nome_fantasia: str, 
                    celular: str, 
                    email_corporativo: str, 
                    categoria: str, 
                    saldo: float 
                ) -> list[PessoaJuridicaTable]:
        with self.__db_connection as database:
            try:
                dados_pessoa_juridica = PessoaJuridicaTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(dados_pessoa_juridica)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def list_pessoa_juridica(self) -> list[PessoaJuridicaTable]:
        with self.__db_connection as database:
            try:
                pessoa_juridica = database.session.query(PessoaJuridicaTable).all()
                return pessoa_juridica
            except NoResultFound:
                return []
    
    def consultar_saldo(self, pessoa_juridica: str) -> PessoaJuridicaTable:
        with self.__db_connection as database:
            try:
                consultar = (database.session
                .query(PessoaJuridicaTable)
                .filter_by(pessoa_juridica.nome)
                .first()
            )
                return consultar.saldo
            
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def sacar_dinheiro(self, quantia: float, pessoa_juridica: str) -> None:
        limite_saque = 20000.00

        saldo = self.consultar_saldo(pessoa_juridica)
        if quantia <= limite_saque and quantia <= saldo:

            saldo -= quantia
            return f"Saque de R${quantia}, realizado com sucesso. Saldo atual: R${saldo}"
        else:   
            return "Error: Valor de saque excede o limite ou saldo insuficiente!"
        
    def extrato_bancario(self, pessoa_juridica: str) -> dict:
        with self.__db_connection as database:
            try:

                extrato_pessoa_fisica = (database.session
                .query(PessoaJuridicaTable)
                .filter_by(PessoaJuridicaTable.nome_fantasia == pessoa_juridica)
                .first()
            )
                return {
                    "Nome": extrato_pessoa_fisica.nome_fantasia,
                    "Saldo": extrato_pessoa_fisica.saldo,
                    "Categoria": extrato_pessoa_fisica.categoria
                }
            
            except Exception as exception:
                database.ssesion.rollback()
                raise exception    
    
    def get_pessoa_juridica(self, pessoa_juridica_id: str) -> None:
        with self.__db_connection as database:
            try:
                nome_pessoa_juridica = (database.session
                .query(PessoaJuridicaTable)
                .filter(PessoaJuridicaTable.id== pessoa_juridica_id)
                .one()
            )
                return nome_pessoa_juridica
            except Exception as exception:
                database.session.rollback()
                raise exception
