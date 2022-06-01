from src.configurations.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    pais = db.Column(db.String(50))
    estado = db.Column(db.String(50))
    municipio = db.Column(db.String(70))
    cep = db.Column(db.String(8))
    rua = db.Column(db.String(150))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(50))
    cpf = db.Column(db.String(11))
    pis = db.Column(db.String(11))
    senha_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not readble atributte')
    
    @password.setter
    def password(self, password):
        self.senha_hash = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.senha_hash, password)
    
    def para_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "pais": self.pais,
            "estado": self.estado,
            "municipio": self.municipio,
            "cep": self.cep,
            "rua": self.rua,
            "numero": self.numero,
            "complemento": self.complemento,
            "cpf": self.cpf,
            "pis": self.pis
             
        }
    


