"""This file will contain the functions to register a new user and to login an existing user"""
import hashlib
import json_manager


class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.subjects = subjects
        # self.json_file = "students_database.json"
        self.hash = hashlib.sha256(password.encode()).hexdigest()
        # salt = b'1234567890123456' # tiene que ser aleatorio para cada usuario
    
    
    
    
    def register(self):
        database = json_manager.JsonManager('database/students_database.json')
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
            hash = hashlib.sha256(password.encode()).hexdigest()
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