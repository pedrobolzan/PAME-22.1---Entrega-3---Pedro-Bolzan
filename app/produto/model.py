from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

produto_api = Blueprint("produto_api", __name__)

class Produto(BaseModel):
    __tablename__ = "produto"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    valor = db.Column(db.Float)
    caracteristicaProduto = db.Column(db.String(100))
    feedback = db.Column(db.String(150), db.ForeignKey('suporte.feedback'))

    produto1 = db.relationship("Entrega", backref = 'produto')
    produto2 = db.relationship("Entregador", backref = 'produto')
    produto3 = db.relationship("Suporte", backref = 'produto')
    caracteristica = db.relationship("Suporte", uselist=False, backref = 'produto')
