from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

supermercado_api = Blueprint("supermercado_api", __name__)

class Supermercado(BaseModel):
    __tablename__ = "supermercado"
    
    id = db.Column(db.Integer, primary_key = True)
    razaoSocial = db.Column(db.String(100))
    cnpj = db.Column(db.String(14))
    enderecoSupermercado = db.Column(db.String(100))
    contatoSupermercado = db.Column(db.String(100))

    contato = db.relationship("Suporte", backref = "supermercado")