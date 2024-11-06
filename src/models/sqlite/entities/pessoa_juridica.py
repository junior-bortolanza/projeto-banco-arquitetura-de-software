from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=True)
    idade = Column(BIGINT, nullable=True)
    nome_fantasia = Column(String, nullable=True)
    celular = Column(String, nullable=True)
    email_corporativo = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    saldo = Column(REAL, nullable=True)

    def __repr__(self) -> None:
        return f"Nome: {self.nome_fantasia}, Faturamento: {self.faturamento}, Saldo: {self.saldo}"
