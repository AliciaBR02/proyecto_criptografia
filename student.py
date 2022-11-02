"""This file will contain the functions of the user 'Student'"""
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
        # save the data in the student database
        database = json_manager.JsonManager('database/students_database.json')
        database.add_item(self)
