from json_manager import JsonManager
from attribute.email import Email
from attribute.password import Password
from attribute.name import Name
from attribute.surname import Surname
from attribute.subjects import Subjects
from attribute.role import Role
from student import Student
from teacher import Teacher
 
class Registration:
    def __init__(self, name, surname, email, password, subjects, role):
        # check that all the attributes are valid
        self.name = Name(name).value
        self.surname = Surname(surname).value
        self.email = Email(email).value
        self.password = Password(password).value
        self.subjects_list = self.subject_list(subjects)
        self.role = Role(role).value
        # save all the data in the database
        self.data = self.load_data(role)
        
    def load_data(self, role):
        if role == 's':
            return JsonManager("database/students_database.json").data
        else:
            return JsonManager("database/teachers_database.json").data

    def subject_list(self, subjects):
        """check that all the entered subjects are valid"""
        subjects_list = []
        for i in subjects:
            subject = Subjects(i).value
            if subject != "subject is not valid":
                subjects_list.append(subject)
        return subjects_list

    def register_student(self):
        """register the student in the database"""
        # check if the email is already registered
        for i in range(len(self.data)):
            if self.email == self.data[i]["email"]:
                return "The email is already registered"
        # if not registered, register the student
        if self.name == "name is not valid" or self.surname == "surname is not valid" or self.email == "email is not valid" or self.password == "password is not valid" or self.subjects_list == []:
            return "Invalid input"
        st = Student(self.name, self.surname, self.email, self.password, self.subjects_list)
        st.register()
        return "You have been registered successfully"

    def register_teacher(self):
        """register the teacher in the database"""
        # check if the email is already registered
        for i in range(len(self.data)):
            if self.email == self.data[i]["email"]:
                return "The email is already registered"
        # if not registered, register the student
        if self.name == "name is not valid" or self.surname == "surname is not valid" or self.email == "email is not valid" or self.password == "password is not valid" or self.subjects_list == []:
            return "Invalid input"
        t = Teacher(self.name, self.surname, self.email, self.password, self.subjects_list)
        t.register()
        return "You have been registered successfully"