import hashlib
import os
from encryptation import Encryptation
from json_manager import JsonManager
import binascii

class PasswordSecure:
    def __init__(self, password):
        # bytes -> 64 -> string
        self.salt = os.urandom(32)
        self.hashed_password = binascii.hexlify(self.hash_password(password, self.salt)).decode()
        self.save_password()
        
    def save_password(self):
        # save salt and hashed password        
        self.salt = binascii.hexlify(self.salt).decode()
        JsonManager("database/secure_passwords.json").add_item(self)
    @staticmethod
    def hash_password(password, salt):
        print("real salt: ", salt)
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


# password = "contraseña" 
# hash = PasswordSecure(password)
# print(hash.hashed_password)
# try1 = input("Introduce la contraseña: ")
# # h1 = hmac.new(key=salt, msg=try1.encode(), digestmod=md5).hexdigest()

# if (try1 != password):
#    print("OLA K ASE") #funsiona porque el hash es distinto
# else:
#    print("MISMA CONTRASEÑA NINIO")  