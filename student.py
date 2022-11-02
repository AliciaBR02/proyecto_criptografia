"""This file will contain the functions to register a new user and to login an existing user"""
import json_manager
from password_secure import PasswordSecure

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
