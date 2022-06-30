from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entrega_api = Blueprint("entrega_api", __name__)

class Entrega(BaseModel):
    __tablename__ = "entrega"
    
    id = db.Column(db.Integer, primary_key = True)
    pedido = db.Column(db.String(100), db.ForeignKey("produto.nome"))
    entregador = db.Column(db.String(100), db.ForeignKey("entregador.nome"))
    enderecoEntrega = db.Column(db.String(100), db.ForeignKey('cliente.enderecoCliente'))
    formaPagamento = db.Column(db.String(100))
    observacoes = db.Column(db.String(100))

    pagamento = db.relationship("Entregador", uselist=False, backref = 'entrega')
    obs = db.relationship("Suporte", uselist=False, backref = 'entrega')