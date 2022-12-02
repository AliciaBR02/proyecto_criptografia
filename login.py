"""Log a user in the system"""
from json_manager import JsonManager
import binascii
import hashlib

class Login:
    def __init__(self, email, password, role):
        self._email = email
        self._password = password
        self._data = []
        self.role = role

    def login(self):
        """Log a user in the system"""
        if self.role == 'Student':
            database = JsonManager('database/students_database.json')
        else:
            database = JsonManager('database/teachers_database.json')
        for user in database.data:
            # look for the entered email
            if user['email'] == self._email:
                # check if the password is correct (true or false)
                result = self.check_password(self._password, user['password'])
                if result:
                    return 'User logged in successfully'
                return 'Incorrect password'
        return 'User not registered'
            
    def check_password(self, password_input, password_real):
        """Check if the password is correct"""
        password_database = JsonManager('database/secure_passwords.json').data
        our_salt = ""
        # look for the hashed password in the database
        for dic in password_database:
            if dic['hashed_password'] == password_real:
                # get the salt of the coincident password
                our_salt = dic['salt']
        # hash the password entered by the user
        undo = binascii.unhexlify(our_salt)
        input_try = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), undo, 200000)).decode()
        # return if they are the equal or not
        return(input_try == password_real)
