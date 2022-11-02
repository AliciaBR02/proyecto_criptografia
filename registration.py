import student
from json_manager import JsonManager
from attribute.email import Email
from attribute.password import Password
from attribute.name import Name
from attribute.surname import Surname
from attribute.subjects import Subjects
from hashlib import md5, scrypt
 
class Registration:
    def __init__(self, name, surname, email, password, subjects):
        self.name = Name(name).value
        self.surname = Surname(surname).value
        self.email = Email(email).value
        self.password = Password(password).value
        self.subjects_list = self.subject_list(subjects)
        print(self.subjects_list)
            
       
        self.data = self.load_data()
        
    def load_data(self):
        return JsonManager("database/students_database.json").data

    def subject_list(self, subjects):
        subjects_list = []
        for i in subjects:
            subject = Subjects(i).value
            print(subject)
            if subject != "subject is not valid":
                subjects_list.append(subject)
        return subjects_list

    def register_student(self):
        # check if the email is already registered
        for i in range(len(self.data)):
            if self.email == self.data[i]["email"]:
                return "The email is already registered"
        # if not registered, register the student
        name = self.name
        surname = self.surname
        email = self.email
        password = self.password
        subjects_list = self.subjects_list
        if name == "name is not valid" or surname == "surname is not valid" or email == "email is not valid" or password == "password is not valid" or subjects_list == []:
            return "Invalid input"
        st = student.Student(self.name, self.surname, self.email, self.password, self.subjects_list)
        st.register()
        return "You have been registered successfully"

