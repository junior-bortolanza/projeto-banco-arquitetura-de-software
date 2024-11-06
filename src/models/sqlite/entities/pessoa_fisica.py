from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable=True)
    idade = Column(BIGINT, nullable=True)
    nome_completo = Column(String, nullable=True)
    celular = Column(String, nullable=True)
    email = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    saldo = Column(REAL, nullable=True)

    def __repr__(self):
        return f"Nome: {self.nome_completo}, Idade: {self.idade}, Saldo: {self.saldo}"
