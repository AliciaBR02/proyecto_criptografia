"""Log a user in the system"""
from json_manager import JsonManager
import binascii
import hashlib

class Login:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._data = []
        self.load_data()
        
    def load_data(self):
        self._data = JsonManager("database/students_database.json").data
        
    def login(self):
        database = JsonManager('database/students_database.json')
        for student in database.data:
            if student['email'] == self._email:
                # check that the password is correct
                result = self.check_password(self._password, student['password'])
                if result:
                    return 'User logged in successfully'
                    
                return 'Incorrect password'
        return 'User not registered'
            
    def check_password(self, password_input, password_real):
        password_database = JsonManager('database/secure_passwords.json').data
        our_salt = ""
        for salt in password_database:
            if salt['hashed_password'] == password_real:
                our_salt = salt['salt']
        undo = binascii.unhexlify(our_salt)
        input_try = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), undo, 200000)).decode()
        return(input_try == password_real)
