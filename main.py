###################################
#      ======= MAIN =======       #
###################################
""" Este módulo contendrá las funciones básicas para el funcionamiento criptográfico de nuestro programa. """
# la libreríad de cryptography solo sirve para cifrar y descifrar, no para firmar y verificar firmas
# tampoco sirve para generar claves hash
# cif sim, hash/hmac
#----------- SYMMETRIC CIPHERS -----------
### Importamos las librerias necesarias
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import hmac
from hashlib import md5
import json


#----------------- Cifrado simétrico -----------------#
#--------------------ENCRYPT--------------------#
print("--------------------ENCRYPT--------------------")
# Generate key and store it in a file
key = Fernet.generate_key()
with open('key.key','wb') as file:
    file.write(key)

#this just opens your 'key.key' and assings the key stored there as 'key'
with open('key.key','rb') as file:
    key = file.read()

#this opens your json and reads its data into a new variable called 'data'
with open('nota.json','rb') as file:
    data = file.read()

#this encrypts the data read from your json and stores it in 'encrypted'
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

#this writes your new, encrypted data into a new JSON file
with open('encrypt.txt','wb') as f:
    f.write(encrypted)






#--------------------DECRYPT--------------------#
print("--------------------DECRYPT--------------------")
fernet = Fernet(key)

with open('encrypt.txt', 'rb') as enc_file:
   encrypted = enc_file.read()
# decrypting the file
decrypted = fernet.decrypt(encrypted)
# opening the file in write mode and writing the decrypted data
with open('decrypt.json', 'wb') as dec_file:
   dec_file.write(decrypted)
with open('decrypt.json','rb') as file:
      decrypted = file.read()
      print(decrypted)


   
#----------- HASH KEYS-----------#
print("-------------------HASH KEYS-------------------")   


def hmac_md5(key, msg):
    return hmac.HMAC(key, msg, md5)

#key2 = fernet.generate_key()
# generar salt aleatorio


salt = b'1234567890123456' # tiene que ser aleatorio para cada usuario
password = "contraseña"
# esto nos hace bien el hash
hashed_key = hmac.new(key=salt, msg=password.encode(), digestmod=md5).hexdigest()
print("HI HELLOE: ", hashed_key)
# hash the key with cryptography library


print("Hashed key: ", hashed_key)
with open('hashed.txt','w') as file:
    file.write(hashed_key)


# from hash to key
with open('hashed.txt','r') as file:
      hashed = file.read()
      print("Hashed key: ", hashed)
      key = hashed.encode('utf-8')
      print("Key: ", key)
      
try1 = input("Introduce la contraseña: ")
h1 = hmac.new(key=salt, msg=try1.encode(), digestmod=md5).hexdigest()
if (try1 != password):
   print("OLA K ASE") #funsiona porque el hash es distinto
else:
   print("MISMA CONTRASEÑA NINIO")
