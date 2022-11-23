"""This file will contain the functions of the user 'teacher'"""
import json_manager
from password_secure import PasswordSecure

class Teacher:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
    
    def register(self):
        # save the data in the teacher database
        database = json_manager.JsonManager('database/teachers_database.json')
        database.add_item(self)
