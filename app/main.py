from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from . import crud, models, schemas
from .database import SessionLocal, engine
from datetime import date

app = FastAPI(title="API de Empréstimos", version="0.1.0")


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/amigos/", response_model=schemas.Amigo, tags=["Amigos"])
def create_amigo(amigo: schemas.AmigoCreate, db: Session = Depends(get_db)):

    db_amigo = db.query(models.Amigo).filter(models.Amigo.telefone == amigo.telefone).first()
    if db_amigo:
        raise HTTPException(status_code=400, detail="Telefone já cadastrado")
    return crud.create_amigo(db=db, amigo=amigo)

@app.get("/amigos/", response_model=list[schemas.Amigo], tags=["Amigos"])
def read_amigos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    amigos = crud.get_amigos(db, skip=skip, limit=limit)
    return amigos

@app.get("/amigos/{amigo_id}", response_model=schemas.Amigo, tags=["Amigos"])
def read_amigo(amigo_id: int, db: Session = Depends(get_db)):

    db_amigo = crud.get_amigo(db, amigo_id=amigo_id)
    if db_amigo is None:
        raise HTTPException(status_code=404, detail="Amigo não encontrado")
    return db_amigo

@app.post("/itens/", response_model=schemas.Item, tags=["Itens"])
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.get("/itens/", response_model=list[schemas.Item], tags=["Itens"])
def read_itens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    itens = crud.get_itens(db, skip=skip, limit=limit)
    return itens

@app.post("/emprestimos/", response_model=schemas.Emprestimo, tags=["Empréstimos"])
def create_emprestimo(emprestimo: schemas.EmprestimoCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_emprestimo(db=db, emprestimo=emprestimo)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Erro de integridade: verifique se o amigo e o item existem.")


@app.patch("/emprestimos/{emprestimo_id}/devolver", response_model=schemas.Emprestimo, tags=["Empréstimos"])
def devolver_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    emprestimo_devolvido = crud.update_emprestimo_status(db, emprestimo_id=emprestimo_id)

    if not emprestimo_devolvido:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado ou já devolvido.")

    return emprestimo_devolvido

@app.get("/emprestimos/", response_model=list[schemas.Emprestimo], tags=["Empréstimos"])
def read_emprestimos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emprestimos = crud.get_emprestimos(db, skip=skip, limit=limit)
    return emprestimos