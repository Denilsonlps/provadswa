from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

class Ocorrencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    disciplina = db.Column(db.String(100), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Ocorrencia {self.id}>'