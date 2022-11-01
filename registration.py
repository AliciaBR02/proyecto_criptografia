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
        self.name = Name(name).value
        self.surname = Surname(surname).value
        self.email = Email(email).value
        self.password = Password(password).value
        self.subject_list = []
        for i in subjects:
            subject = Subjects(i).value
            self.subject_list.append(subject)
        # self.data = []
        self.data = self.load_data()
        self.register_student()
        
    def load_data(self):
        return json_manager.JsonManager("database/students_database.json").data
    def register_student(self):
        # check if the email is already registered
        for i in range(len(self.data)):
            if self.email == self.data[i]["email"]:
                #raise error message
                raise Exception("Email already registered")
        # if not registered, register the student
        
        st = student.Student(self.name, self.surname, self.email, self.password, self.subject_list)
        st.register()
    

s = Registration("Joe", "Doe", "d@emdail.com", "T9dbfjbfjbj@", ["Matemáticas", "Física", "Química"])
# s = user_reg.Student("Joe", "Doe", "ola@quetal.com", "123456")
# s.login()
