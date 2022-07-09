from email import parser
from fastapi import FastAPI, Depends, status, HTTPException
from yaml import parse
from database.database import engine, SessionLocal
import tabela.tabela as tabela
from sqlalchemy.orm import Session
import schema.schema as schema

tabela.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return "API CRUD(Ainda não está completa"

@app.post('/criar_usuario', status_code=status.HTTP_201_CREATED)
def cria_usuario(request: schema.Usuario, db: Session = Depends(get_db)):
    novo_usuario = tabela.Usuario(nome=request.nome, idade=request.idade)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.get("/usuarios")
def todos_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(tabela.Usuario).all()
    return usuarios

@app.get("/usuario/{id}")
def usuario(id,db: Session = Depends(get_db)):
    usuario = db.query(tabela.Usuario).filter(tabela.Usuario.id == id).first()
    return usuario

@app.delete("/usuario/{id}")
def deleta_usuario(id,db: Session = Depends(get_db)):
    db.query(tabela.Usuario).filter(tabela.Usuario.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Usuario removido com sucesso!'

@app.put("/usuario/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_usuario(id, request: schema.Usuario, db: Session = Depends(get_db)):
    usuario = db.query(tabela.Usuario).filter(tabela.Usuario.id == id)
    if not usuario.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Usuario com id {id} não foi encontrado")
    usuario.update(vars(request))
    db.commit()
    return "Os dados do usuario foram atualizados"