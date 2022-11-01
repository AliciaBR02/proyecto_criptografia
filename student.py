"""This file will contain the functions to register a new user and to login an existing user"""
import hashlib
import json_manager
import os
from password_secure import PasswordSecure

class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = PasswordSecure(password).__hashed_password
        self.subjects = subjects
        # # self.json_file = "students_database.json"
        # self.salt = os.urandom(16)
        # self.hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)
        # self.hash = hashlib.sha512(password.encode()).hexdigest()
    
    # def save_secure_password(self):
    #     password = PasswordSecure(self.password)
    #     database = json_manager.JsonManager('database/secure_passwords.json')
    #     database.add_item([self.hash, self.salt])
    
    def register(self):
        database = json_manager.JsonManager('database/students_database.json')
        database.add_item(self)
            
                    
    # Function to login an existing user
    # def login(email, password):
    #     # Open the JSON file and read the data
    #     with open('database/students_database.json','r') as file:
    #         data = file.read()
    #     if email in data:
    #         # Check if the password is correct
    #         hash = hashlib.sha512(password.encode()).hexdigest()
    #         if hash in data:
    #             # Print a success message
    #             print('User logged in successfully')
    #         else:
    #             # Print an error message
    #             print('Incorrect password')
    #     else:
    #         # Print an error message
    #         print('User does not exist')
    # def check_password(self, password):
    #     # buscar y desciptar el salt
    #     with open('database/secure_passwords.json','r') as file:
    #         data = file.read()
    #         # key = hashed.encode('utf-8')
        
    #     salt = Encryptation().decrypt(self.encrypted_salt, "salt_database.json")
    #     input_try = self.hash_password(password, salt.encode('utf-8'))
    #     return(input_try == self.__hashed_password)
        
    #     # from hash to key
    #     with open('hashed.txt','r') as file:
    #         hashed = file.read()
    #         print("Hashed key: ", hashed)
    #         key = hashed.encode('utf-8')
    #         print("Key: ", key)
            
    #     try1 = input("Introduce la contraseña: ")
    #     h1 = hmac.new(key=salt, msg=try1.encode(), digestmod=md5).hexdigest()
    #     if (try1 != password):
    #     print("OLA K ASE") #funsiona porque el hash es distinto
    #     else:
    #     print("MISMA CONTRASEÑA NINIO")