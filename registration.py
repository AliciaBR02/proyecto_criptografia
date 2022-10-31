import student
import json_manager
import hashlib
import re
from attribute.email import Email
from attribute.password import Password
from attribute.name import Name
from attribute.surname import Surname
from attribute.subjects import Subjects

 
# Creamos una instancia para 
class Registration:
    def __init__(self, name, surname, email, password, subjects):
        self._name = Name(name).value
        self._surname = Surname(surname).value
        self._email = Email(email).value
        self._password = Password(password).value
        self._subject_list = []
        for i in subjects:
            subject = Subjects(i).value
            self._subject_list.append(subject)
        self.data = []
        self.load_data()
        self.register_student()
        
    def load_data(self):
        self.data = json_manager.JsonManager("database/students_database.json").data
    def register_student(self):
        # check if the email is already registered
        for i in range(len(self.data)):
            if self._email == self.data[i]["email"]:
                #raise error message
                raise Exception("Email already registered")
        st = student.Student(self._name, self._surname, self._email, self._password, self._subject_list)
        st.register()
    
    # Setters of the attributes of the student
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):  
        self._name = value
    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self, value):  
        self._surname = value
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

s = Registration("Joe", "Doe", "d@emdail.com", "T9dbfjbfjbj@", ["Matemáticas", "Física", "Química"])
# s = user_reg.Student("Joe", "Doe", "ola@quetal.com", "123456")
# s.login()
