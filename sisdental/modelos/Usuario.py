import hashlib
from sisdental import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    administrador = db.Column(db.Boolean, default=False)
    doctor = db.Column(db.Boolean, default=False)
    asistente = db.Column(db.Boolean, default=False)
    persona_id = db.Column(db.Integer, db.ForeignKey('personas.id'), unique=True, nullable=True)
    persona = db.relationship('Persona', backref='usuario', uselist=False)

    def set_password(self, password: str):

        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password: str) -> bool:
        hash_intento = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return self.password == hash_intento
#♥