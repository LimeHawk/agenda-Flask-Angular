from functools import wraps
from flask import request, make_response
import jwt
#Json Web Token
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv('JWT_ENCRYPTION_KEY')

user = os.getenv('LOGINACESS')

class SecurityController:

    def criarToken(self,email):
        return jwt.encode({"email":email},key,algorithm="HS256")
    
    def decodificarToken(self,token):
        return jwt.decode(token,key,algorithm="HS256")
        

