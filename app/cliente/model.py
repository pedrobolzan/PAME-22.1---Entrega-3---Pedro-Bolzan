from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):
    __tablename__ = "cliente"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    contatoCliente = db.Column(db.String(11))
    enderecoCliente = db.Column(db.String(100))

    entrega = db.relationship("Entrega", backref = "cliente")
    suporte = db.relationship("Suporte", backref = "cliente")