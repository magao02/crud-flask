
from datetime import timedelta
from flask import Flask, request, Response
import json
from src.models.user_model import Usuario
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from src.configurations import database
from src.configurations.database import db
from src.services.user_service import User_service
from src.configurations import authetication_jwt
from config import config_selector


app = Flask(__name__)
app.config.from_object(config_selector["development"])
JWT = JWTManager(app) 
database.init_app(app)

@app.route("/login", methods=["POST"])
def login():
    body = request.get_json()
    login_response = User_service.login(body)
    return login_response

@app.route("/usuarios", methods=["GET"] )
@jwt_required()
def selecionaTodos():
    usuarios_response = User_service.seleciona_todos_usuarios()
    return usuarios_response

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    body = request.get_json()
    cadastro_response = User_service.cadastra_usuario(body,db)
    return cadastro_response
    
@app.route("/usuario/<id>", methods=["GET"])
@jwt_required()
def seleciona_usuario(id):
    usuario_response = User_service.seleciona_usuario(id)
    return usuario_response

@app.route("/usuario/<id>" ,methods=["PUT"])
@jwt_required
def atualizar(id):
    body = request.get_json()
    usuario_response = User_service.edita_usuario(id,body,db)
    return usuario_response

@app.route("/usuario/<id>" ,methods=["DELETE"])
@jwt_required()
def delete(id):
    usuario_response = User_service.deleta_usuario(id,db)
    return usuario_response



