from SysEyeId import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Clinica(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    endereco = database.Column(database.String, nullable=False)
    medico = database.Relationship("Medico", backref="Clinica", lazy=True)
    usuario = database.Relationship("Usuario", backref="Clinica", lazy=True)

class Medico(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    clinica = database.Column(database.Integer, database.ForeignKey("clinica.id"), nullable=False)
    usuario = database.Relationship("Usuario", backref="Medico", lazy=True)

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    endereco = database.Column(database.String, nullable=False)
    medico = database.Column(database.Integer, database.ForeignKey("medico.id"), nullable=False)
    clinica = database.Column(database.Integer, database.ForeignKey("clinica.id"), nullable=False)
    exame = database.Relationship("Exame", backref="Usuario", lazy=True)

class Exame(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)

class Mensagem(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    mensagem = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
