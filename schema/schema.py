import string
from tokenize import String


from pydantic import BaseModel
#Criando um corpo para a entrada de dados na rota /criar_usuario

from sqlalchemy import Integer

class Usuario(BaseModel):
    nome:str
    idade:int