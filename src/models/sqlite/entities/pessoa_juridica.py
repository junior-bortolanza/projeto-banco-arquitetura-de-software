from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_fantasia = Column(String(100), nullable=False)
    celular = Column(String(11), nullable=False)
    email_corporativo = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self) -> None:
        return f" Nome: {self.nome_fantasia}, Faturamento: {self.faturamento}, Saldo: {self.saldo}"
