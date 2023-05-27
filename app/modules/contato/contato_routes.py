from flask import Blueprint, jsonify, request
from app.modules.contato.contato_dao import ContatoDAO
from app.security.autenticacao import verificar_token_jwt 

contato_routes = Blueprint("contato",__name__)
contato_dao = ContatoDAO()

@contato_routes.route("/api/v1/contato", methods=["POST"])
@verificar_token_jwt
def salvar():
    print("Metodo Salvar foi invocado")
    if request.json:
        if ('nome' in request.json \
        and 'email' in request.json \
        and 'telefone' in request.json):
            contato_dao.save(request.json)
            return {"msg":"Contato salvo com sucesso."},200
    return {"msg":"O contato não foi informado"},400

@contato_routes.route("/api/v1/contato", methods=["GET"])
@verificar_token_jwt
def obterTodosContatos():
    print("Metodo obterTodosContatos foi invocado")
    contacts = contato_dao.getAll()
    contactsList = []
    if len(contacts) > 0:
        for contact in contacts:
            contactOBJ = {}
            contactOBJ["id"] = contact[0]
            contactOBJ["nome"] = contact[1]
            contactOBJ["email"] = contact[2]
            contactOBJ["telefone"] = contact[3]
            contactsList.append(contactOBJ)
    return jsonify(contactsList),200

@contato_routes.route("/api/v1/contato", methods=["PUT"])
@verificar_token_jwt
def update():
    print("Metodo update foi invocado")
    if request.json:
        if ('id' in request.json \
        and 'nome' in request.json \
        and 'email' in request.json \
        and 'telefone' in request.json):
            colunas = contato_dao.update(request.json)
            if colunas > 0:
                return {"msg":"O contato foi atualizado"},200
            else:
                return {"msg": "erro durante o update no banco"},500
    return {"msg":"O contato não foi informado"},400

@contato_routes.route("/api/v1/contato/<string:id>", methods=["DELETE"])
@verificar_token_jwt
def delete(id):
    print("Metodo delete foi invocado")
    
    if contato_dao.delete(id) == 1:
        return {"msg":"O contato foi deletado"},200
    else:
        return {"msg": "erro durante o delete no banco"},500
    
    return {"msg":"O contato não foi informado"},400