#Criando a tabela do banco de dados

from database import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    idade = Column(Integer)