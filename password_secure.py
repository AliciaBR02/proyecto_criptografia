import hashlib
import os
from encryptation import Encryptation
from json_manager import JsonManager

class PasswordSecure:
    def __init__(self, password):
        # self.__password = password
        salt = os.urandom(32)
        self.__hashed_password = self.hash_password(password, salt)
        self.encrypted_salt = self.encrypt_salt(salt)
        self.save_password()

    def hash_password(self, password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    def save_password(self):
        with open('database/secure_passwords.json', 'a') as file:
            JsonManager(file).add_item(self)
    
    def encrypt_salt(self, salt):
        return Encryptation().encrypt(str(salt), "database/salt_database.json")
        # encriptar con la clase de encriptación
    
    
        
        
        
        
        

# with open('hashed.txt','r') as file:
#       hashed = file.read()
#       print("Hashed key: ", hashed)
#       key = hashed.encode('utf-8')
#       print("Key: ", key)
 

password = "contraseña" 
hash = PasswordSecure(password).__hashed_password
# try1 = input("Introduce la contraseña: ")
# # h1 = hmac.new(key=salt, msg=try1.encode(), digestmod=md5).hexdigest()

# if (try1 != password):
#    print("OLA K ASE") #funsiona porque el hash es distinto
# else:
#    print("MISMA CONTRASEÑA NINIO")  