from flask import Blueprint,request,make_response
from app.modules.login.login_controller import LoginController
from app.security.security_controller import SecurityController

login_routes = Blueprint("login",__name__)

@login_routes.route("/api/v1/login", methods=["POST"])
def logar():
    print("Metodo Login foi invocado")
    if request.json:
        if ('email' in request.json \
        and 'senha' in request.json ):
            
            loginBC = LoginController()
            
            login = loginBC.logar(request.json['email'],request.json['senha'])

            if login:
                securityBC = SecurityController()

                token = securityBC.criarToken(request.json['email'])

                response = make_response('Login bem-sucedido')
                
                response.set_cookie('token', token)

                return response
            
            return {"msg":"Falha no login"},401
        
        return {"msg":"Algo deu errado, faltando parametros ou incorretos"},400
    
    return {"msg":"Nenhum parametro informado "},400