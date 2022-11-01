"""This file will contain the functions to register a new user and to login an existing user"""
import hashlib
import json_manager
import os
from password import Password

class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        self.__password = password
        self.subjects = subjects
        # self.json_file = "students_database.json"
        self.salt = os.urandom(16)
        self.hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), self.salt, 100000)
        # self.hash = hashlib.sha512(password.encode()).hexdigest()
    
    def save_secure_password(self):
        password = Password(self.__password)
        database = json_manager.JsonManager('database/secure_passwords.json')
        database.add_item([self.hash, self.salt])
    
    def register(self):
        database = json_manager.JsonManager('database/students_database.json')
        print(self)
        database.add_item(self)
        print("User registered successfully")
            
                    
    @staticmethod
    # Function to login an existing user
    def login(email, password):
        # Open the JSON file and read the data
        with open('database/students_database.json','r') as file:
            data = file.read()
        if email in data:
            # Check if the password is correct
            hash = hashlib.sha512(password.encode()).hexdigest()
            if hash in data:
                # Print a success message
                print('User logged in successfully')
            else:
                # Print an error message
                print('Incorrect password')
        else:
            # Print an error message
            print('User does not exist')

    def setSubjects(self, subjects):
        self.subjects = subjects