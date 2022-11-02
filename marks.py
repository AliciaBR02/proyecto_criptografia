"""Manage the marks to be stored in the database"""
import json_manager
from attribute.email import Email
from attribute.subjects import Subjects
from attribute.exam import Exam
from encryption import Encryption


class MarksManager:
    def __init__(self):
        self.subject = ""
        self.email = ""
        self.exam = ""
        self.mark = ""
        pass

    def add_mark(self, email, password, subject, exam, mark):
        """Add a mark to the database"""
        mark_data = json_manager.JsonManager("database/marks_database.json")
        # check the values entered and check that the student is registered
        self.email = Encryption(email, password).encrypt(Email(email).value)
        self.subject = Subjects(subject).value
        self.exam = Exam(exam).value
        if mark <= 10 and mark >= 0 and self.check_subjects(email, subject): # if everything is okay, add the mark into the marks database
            self.mark = Encryption(email, password).encrypt(str(mark)) # validate mark
            mark_data.add_item(self)
            return "Mark added successfully"
        return "Some of the parameters are not valid"
    
    def check_subjects(self, email, subject):
        """Check if the student is registered in the subject"""
        students_data = json_manager.JsonManager("database/students_database.json").data
        for student in students_data:
            if student["email"] == email and subject in student["subjects"]:
                return True
    
    
    def get_marks(self, email, password):
        """Get the marks of the student"""
        student_marks = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        for mark in mark_data:
            # decrypt the entered email and look for the marks of the student
            try:
                email_dec = Encryption(email, password).decrypt(mark["email"])
                if email_dec == email:
                # if the student is found, decrypt the marks and add them to the list
                    mark_dec = Encryption(email, password).decrypt(mark["mark"])
                    student_marks.append({"subject": mark["subject"], "exam": mark["exam"], "mark": mark_dec})
            except:
                pass
                
            
        return student_marks
