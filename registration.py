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
    def __init__(self, name, surname, email, password, role, subjects):
        # check that all the attributes are valid
        self.name = Name(name).value
        self.surname = Surname(surname).value
        self.email = Email(email).value
        self.password = Password(password).value
        self.subjects_list = self.subject_list(subjects)
        self.role = Role(role).value
        

    def subject_list(self, subjects):
        """check that all the entered subjects are valid"""
        subjects_list = []
        for i in subjects:
            subject = Subjects(i).value
            if subject != "subject is not valid":
                subjects_list.append(subject)
        return subjects_list

    def register(self):
        """register the student in the database"""
        # check if the email is already registered
        data = JsonManager("database/users_database.json").data
        for i in range(len(data)):
            if self.email == data[i]["email"]:
                return "The email is already registered"
        if self.name == "name is not valid":
            return "name is not valid"
        if self.surname == "surname is not valid":
            return "surname is not valid"
        if self.email == "email is not valid":
            return "Invalid email"
        if self.password == "password is not valid":
            return "Invalid password"
        if self.subjects_list == []:
            return "Invalid subjects"
        if self.role == "Student":
            Student(self.name, self.surname, self.email, self.password, self.subjects_list).register()
        elif self.role == "Teacher":
            Teacher(self.name, self.surname, self.email, self.password, self.subjects_list).register()
        return "You have been registered successfully"
