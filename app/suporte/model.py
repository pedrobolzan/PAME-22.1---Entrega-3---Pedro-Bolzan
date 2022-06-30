from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

suporte_api = Blueprint("suporte_api", __name__)

class Suporte(BaseModel):
    __tablename__ = "suporte"
    
    id = db.Column(db.Integer, primary_key = True)
    contatoSupermercado = db.Column(db.String(100), db.ForeignKey('supermercado.contatoSupermercado'))
    contatoCliente = db.Column(db.String(11), db.ForeignKey('cliente.enderecoCliente'))
    produto = db.Column(db.String(100), db.ForeignKey('produto.nome'))
    caracteristicas = db.Column(db.String(100), db.ForeignKey('produto.caracteristicaProduto'))
    feedback = db.Column(db.String(150))
    contatoEntregador = db.Column(db.String(11), db.ForeignKey('entregador.contatoEntregador'))

    feedbackProduto = db.relationship("Produto", backref = "suporte")