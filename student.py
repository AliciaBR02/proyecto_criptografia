"""This file will contain the functions of the user 'Student'"""
import json_manager
from password_secure import PasswordSecure
from sign_verification import SignVerification
from encryption import Encryption

class Student:
    def __init__(self, name, surname, email, password, subjects):
        self.name = name
        self.surname = surname
        self.email = email
        p = PasswordSecure(password)
        self.password = p.hashed_password
        self.subjects = subjects
        self.role = "Student"
        s = SignVerification()
        private_key = s.generate_private_key()
        # we encrypt the keys to save them later into the database
        self.private_key = s.encrypt_private_key(private_key, password).decode('utf-8')
        public_key = s.generate_public_key(private_key)
        self.public_key = s.encrypt_public_key(public_key).decode('utf-8')
        s.generate_certificate(private_key, email)
        
    def register(self):
        # save the data in the student database
        database = json_manager.JsonManager('database/users_database.json')
        database.add_item(self)

st = Student("Val", "Cataldo", "val@email.com", "password", ["Mathematics", "Physics"])
st.register()