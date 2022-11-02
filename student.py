"""This file will contain the functions to register a new user and to login an existing user"""
import hashlib
import json_manager
import os
from password_secure import PasswordSecure
# from encryption import encryption
import binascii


class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
    
    def register(self):
        database = json_manager.JsonManager('database/students_database.json')
        database.add_item(self)
        print('You have been registered successfully')
    
   
     
      
# s = Student("Pepe", "Perez", "hola@isaac.agresivo", "contraseña", ["Matemáticas", "Física"])
# s.register()
# s.login("hola@isaac.agresivo", "contraseña")