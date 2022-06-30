from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

entregador_api = Blueprint("entregador_api", __name__)

class Entregador(BaseModel):
    __tablename__ = "entregador"
    
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    entrega = db.Column(db.String(100), db.ForeignKey("produto.nome"))
    veiculo = db.Column(db.String(100))
    contatoEntregador = db.Column(db.String(11))
    pagamento = db.Column(db.String(100), db.ForeignKey("entrega.formaPagamento"))
    observacoes = db.Column(db.String(100), db.ForeignKey("entrega.observacoes"))

    nomeEntregador = db.relationship("Entrega", backref = "entregador")
    contato = db.relationship("Suporte", backref = "entregador")