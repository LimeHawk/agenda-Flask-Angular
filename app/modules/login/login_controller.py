from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('LOGINACESS')
password = os.getenv('PASSWORD')


class LoginController:

    def logar(self,email,senha):
        
        if not email:
            return False
        
        if not senha:
            return False
        
        if email == user and senha == password:
            return True
        
        return False
            
    

    