from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def get_amigo(db: Session, amigo_id: int):
    return db.query(models.Amigo).filter(models.Amigo.id == amigo_id).first()

def get_amigos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Amigo).offset(skip).limit(limit).all()

def create_amigo(db: Session, amigo: schemas.AmigoCreate):

    db_amigo = models.Amigo(nome=amigo.nome, telefone=amigo.telefone)
    db.add(db_amigo)
    db.commit()
    db.refresh(db_amigo)
    return db_amigo

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_itens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def create_emprestimo(db: Session, emprestimo: schemas.EmprestimoCreate):
    db_emprestimo = models.Emprestimo(**emprestimo.model_dump())
    db.add(db_emprestimo)
    db.commit()
    db.refresh(db_emprestimo)
    return db_emprestimo

def update_emprestimo_status(db: Session, emprestimo_id: int):
    db_emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == emprestimo_id).first()

    if db_emprestimo and db_emprestimo.status == models.StatusEmprestimo.ATIVO:
        db_emprestimo.status = models.StatusEmprestimo.DEVOLVIDO
        db_emprestimo.data_devolucao = date.today()
        db.commit()
        db.refresh(db_emprestimo)

    return db_emprestimo

def get_emprestimos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Emprestimo).offset(skip).limit(limit).all()