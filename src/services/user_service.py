from datetime import timedelta
from src.models.user_model import Usuario
from flask import  Response
from flask_jwt_extended import create_access_token
import json
class User_service():
    def login(body):
        identificador = body["identificador"]
        usuario_objeto = Usuario.query.filter_by(email=identificador).first()
        if not usuario_objeto:
            usuario_objeto = Usuario.query.filter_by(cpf=identificador).first()
        elif not usuario_objeto:
            usuario_objeto = Usuario.query.filter_by(pis=identificador).first()
        
        senha = body["senha"]
        if usuario_objeto.verify_password(senha):
            access_token = create_access_token(identity=usuario_objeto.cpf, expires_delta=timedelta(days=7))
            token = {"access_token": access_token, "id": usuario_objeto.id}
            return Response(json.dumps(token))
        else:
            return envia_erro(400, "A senha esta errada")
        
    def seleciona_todos_usuarios():
        usuarios_classe = Usuario.query.all()
        usuarios_json =[usuario.para_json() for usuario in usuarios_classe]
        return gera_response(200, "usuarios", usuarios_json, "ok")
        
    
    def cadastra_usuario(body, db):

        try:
            usuario = Usuario(
                nome=body["nome"], 
                email=body["email"],
                pais=body["pais"], 
                estado=body["estado"],  
                municipio=body["municipio"],
                cep=body["cep"],
                rua=body["rua"],
                numero=body["numero"],
                complemento=body["complemento"],
                cpf=body["cpf"],
                pis=body["pis"],
                password=body["senha"]
                )
            db.session.add(usuario)
            db.session.commit()
            return  "usuarios"
        except Exception as e:
            print(e)
            return envia_erro(500, "Nao foi possivel cadastrar esse usuario")

    def seleciona_usuario(id):
        usuario_objeto = Usuario.query.filter_by(id=id).first()
        try:
            usuario_json = usuario_objeto.para_json()
            return gera_response(200, "usuarios", usuario_json, "ok")
        except Exception as e:
            if(usuario_objeto):
                return envia_erro(404, "Nao foi possivel encontrar esse usuario")
            else:
                return envia_erro(500, "Nao foi possivel recuperar os dados desse usuario")

    def edita_usuario(id,body,db):
        usuario_objeto = Usuario.query.filter_by(id=id).first()
        try:
            usuario_objeto.nome=body["nome"], 
            usuario_objeto.email=body["email"],
            usuario_objeto.pais=body["pais"], 
            usuario_objeto.estado=body["estado"],  
            usuario_objeto.municipio=body["municipio"],
            usuario_objeto.cep=body["cep"],
            usuario_objeto.rua=body["rua"],
            usuario_objeto.numero=body["numero"],
            usuario_objeto.complemento=body["complemento"],
            usuario_objeto.cpf=body["cpf"],
            usuario_objeto.pis=body["pis"],
            usuario_objeto.assword=body["senha"]
            db.session.add(usuario_objeto)
            db.session.commit()
            usuario_json = usuario_objeto.para_json()
            return gera_response(200, "usuarios", usuario_json, "ok")
            
        except Exception as e:
            if(usuario_objeto):
                return envia_erro(404, "Nao foi possivel encontrar esse usuario")
            else:
                return envia_erro(500, "Nao foi possivel editar esse usuario")

    def deleta_usuario(id,db):
        usuario_objeto = Usuario.query.filter_by(id=id).first()
        try:
            db.session.delete(usuario_objeto)
            db.session.commit()
            return "deletado com sucesso"
        except Exception as e:
            print(e)
            if(usuario_objeto):
                return envia_erro(404, "Nao foi possivel encontrar esse usuario")
            else:
                return envia_erro(500, "Nao foi possivel deletar esse usuario")

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
        body={}
        body[nome_do_conteudo] = conteudo
        if(mensagem):
            body["mensagem"] = mensagem
        
        return Response(json.dumps(body),status=status, mimetype="application/json")
def envia_erro(status, mensagem):
    body={}
    body["mensagem"] = mensagem
    return Response(json.dumps(body),status=status)
