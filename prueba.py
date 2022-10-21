###################################
#      ======= MAIN =======       #
###################################
""" Este módulo contendrá las funciones básicas para el funcionamiento criptográfico de nuestro programa. """
# la libreríad de cryptography solo sirve para cifrar y descifrar, no para firmar y verificar firmas
# tampoco sirve para generar claves hash
# y solo se puede usar con claves de 64 bytes. Si me ponen una contraseña normal, nada

#----------- SYMMETRIC CIPHERS -----------
### Importamos las librerias necesarias
from cryptography.fernet import Fernet

# we create a key
key = Fernet.generate_key()
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
# fernet guarantees that a message encrypted using it cannot be manipulated or read without the key


with open('filekey.key', 'rb') as filekey:
   key = filekey.read()


fernet = Fernet(key)

# encrypt the message
encrypted = fernet.encrypt(key)

# we write the encrypted message in a file
with open('enc.txt', 'wb') as file:
   file.write(encrypted)


# we read the encrypted message
with open('enc.txt', 'rb') as file:
    encrypted_file = file.read()

# decrypt the message
decrypted_message = fernet.decrypt(encrypted)

# open file in write mode and write decrypted message
with open('dec.txt', 'wb') as file:
   file.write(decrypted_message)

# print the decrypted message
with open('dec.txt', 'rb') as file:
   decrypted_file = file.read()
   print(decrypted_file)
   
   
#----------- HASH KEYS-----------
print("-------------------HASH KEYS-------------------")   
key2 = "hellothisisme"
hashed = hash(key2)
print(hashed)
print(key2)
# hash key with Fernet library
fernet2 = Fernet(key2)
hashed2 = fernet2.__hash__()
with open('hashed.txt', 'wb') as file:
   file.write(hashed2)
# print the hashed message
with open('hashed.txt', 'rb') as file:
   hashed_file = file.read()
   print(hashed_file)