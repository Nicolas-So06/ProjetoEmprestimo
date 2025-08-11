import enum
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class StatusEmprestimo(str, enum.Enum):
    ATIVO = "ativo"
    DEVOLVIDO = "devolvido"


class Amigo(Base):
    __tablename__ = "amigos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String, unique=True, index=True, nullable=False)

    emprestimos = relationship("Emprestimo", back_populates="amigo")


class Item(Base):
    __tablename__ = "itens"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    descricao = Column(String, nullable=True)

    emprestimos = relationship("Emprestimo", back_populates="item")


class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id = Column(Integer, primary_key=True, index=True)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    status = Column(Enum(StatusEmprestimo), nullable=False, default=StatusEmprestimo.ATIVO)

    amigo_id = Column(Integer, ForeignKey("amigos.id"), nullable=False)
    item_id = Column(Integer, ForeignKey("itens.id"), nullable=False)

    amigo = relationship("Amigo", back_populates="emprestimos")
    item = relationship("Item", back_populates="emprestimos")