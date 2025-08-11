from pydantic import BaseModel, ConfigDict
from datetime import date
from .models import StatusEmprestimo

class ItemBase(BaseModel):
    nome: str
    descricao: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class AmigoBase(BaseModel):
    nome: str
    telefone: str

class AmigoCreate(AmigoBase):
    pass

class Amigo(AmigoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class EmprestimoBase(BaseModel):
    amigo_id: int
    item_id: int
    data_emprestimo: date

class EmprestimoCreate(EmprestimoBase):
    pass

class Emprestimo(EmprestimoBase):
    id: int
    status: StatusEmprestimo
    data_devolucao: date | None = None

    amigo: Amigo
    item: Item

    model_config = ConfigDict(from_attributes=True)