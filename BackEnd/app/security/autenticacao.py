from functools import wraps
from flask import request, make_response

import jwt
#Json Web Token

from dotenv import load_dotenv

import os

load_dotenv()

key = os.getenv('JWT_ENCRYPTION_KEY')

user = os.getenv('LOGINACESS')

def verificar_token_jwt(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        token = request.cookies.get('token')
        
        if token:
            try:
                
                decoded_token = jwt.decode(token, key, algorithms="HS256")
                
                print(f"{decoded_token}")
                email = decoded_token['email']

                if email == user:
                    return f(*args, **kwargs)
                
            except jwt.ExpiredSignatureError:
                return {'Token expirado. Faça login novamente.'},401
            except jwt.InvalidTokenError:
                return {'Token inválido. Faça login novamente.'},401
        else:
            return make_response('Token não encontrado. Faça login novamente.', 401)

    return decorator
