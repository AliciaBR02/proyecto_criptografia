import student
from json_manager import JsonManager
import hashlib
import re
import binascii
from attribute.email import Email
from attribute.password import Password
from attribute.name import Name
from attribute.surname import Surname
from attribute.subjects import Subjects
from hashlib import md5, scrypt
 
# Creamos una instancia para 
class Registration:
    def __init__(self, name, surname, email, password, subjects):
        self.name = Name(name).value
        self.surname = Surname(surname).value
        self.email = Email(email).value
        self.password = Password(password).value
        self.subject_list = []
        for i in subjects:
            print(i)
            print(len(i))
            #depurar el texto de i solo a letras
            subject = Subjects(i).value
            print('agregado')
            self.subject_list.append(subject)
        # self.data = []
        print(self.subject_list)
        self.data = self.load_data()
        # self.register_student()
        
    def load_data(self):
        return JsonManager("database/students_database.json").data
    def register_student(self):
        # check if the email is already registered
        for i in range(len(self.data)):
            if self.email == self.data[i]["email"]:
                #raise error message
                raise Exception("Email already registered")
        # if not registered, register the student
        
        st = student.Student(self.name, self.surname, self.email, self.password, self.subject_list)
        st.register()
        return "You have been registered successfully"
        
    # def create_key(self, password):
    #     password_database = JsonManager('database/secure_passwords.json').data
    #     our_salt = ""
    #     for salt in password_database:
    #         if salt['hashed_password'] == password_real:
    #             our_salt = salt['salt']
    #     undo = binascii.unhexlify(our_salt)
    #     input_try = binascii.hexlify(hashlib.pbkdf2_hmac('sha256', password_input.encode('utf-8'), undo, 100000)).decode()
        
    #     for salt in password_database:
    #         print(salt['hashed_password'])
    #         print(password)
    #         print()
    #         if salt['hashed_password'] == password:
    #             print("hi")
    #             our_salt = salt['salt']
    #             print("prev", our_salt)
    #             our_salt = binascii.unhexlify(our_salt)
    #             print("post", our_salt)
    #             key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), our_salt, 100000)
    #             return key
    #     return
                # key = scrypt(password, our_salt, 16, N=2**14, r=8, p=1) #p, n ,r = parámetros de coste computacional
        
                
                

# s = Registration("Joe", "Doe", "dd@email.com", "T9dbfjbfjbj@", ["Matemáticas", "Física", "Química"]).register_student()
# print(s)
# s.login()
