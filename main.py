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
salt = b'1234567890123456'
password = "contraseña"
hashed_key = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend()).derive(password.encode())
# hash the key with cryptography library

hashed = hmac_md5(key, password.encode('utf-8')).hexdigest()

# hash key with salt
hashed2 = hmac_md5(hashed_key, password.encode('utf-8')).hexdigest()

print("Hashed key: ", hashed2)
with open('hashed.txt','w') as file:
    file.write(hashed2)

# from hash to key
with open('hashed.txt','r') as file:
      hashed = file.read()
      print("Hashed key: ", hashed)
      key = hashed.encode('utf-8')
      print("Key: ", key)
      # with open('nota.json','rb') as file:
      #    data = file.read()
      #    print("Data: ", data)
      #    encrypted = fernet.encrypt(data)
      #    print("Encrypted data: ", encrypted)
      #    with open('encrypt.txt','wb') as f:
      #          f.write(encrypted)
      # with open('encrypt.txt', 'rb') as enc_file:
      #    encrypted = enc_file.read()
      #    print("Encrypted data: ", encrypted)
      #    # decrypting the file
      #    decrypted = fernet.decrypt(encrypted)
      #    print("Decrypted data: ", decrypted)
      #    # opening the file in write mode and writing the decrypted data
      #    with open('decrypt.json', 'wb') as dec_file:
      #          dec_file.write(decrypted)
      #    with open('decrypt.json','rb') as file:
      #          decrypted = file.read()
      #          print("Decrypted data: ", decrypted.decode('utf-8'))
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"')))
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["titulo"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["texto"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["fecha"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["autor"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["tags"])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["tags"][0])
               # print("Decrypted data: ", json.loads(decrypted.decode('utf-8').replace("'", '"'))["nota"]["tags"][1])

# hash key with Fernet library
# fernet2 = Fernet(key2)
# hashed2 = fernet2.__hash__()
#with open('hashed.txt', 'wb') as file:
#   file.write(hashed2)
# print the hashed message
#with open('hashed.txt', 'rb') as file:
#   hashed_file = file.read()
#   print(hashed_file)