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

    def add_mark(self, email, subject, exam, mark):
        mark_data = json_manager.JsonManager("database/marks_database.json")
        # check the values entered
        self.email = Encryption(email).encrypt(Email(email).value, "database/emails_encrypted.json")
        self.subject = Subjects(subject).value
        self.exam = Exam(exam).value
        if mark <= 10 and mark >= 0: # if everything is okay, add the mark
            self.mark = Encryption(email).encrypt(str(mark), "database/marks_encrypted.json") # validate mark
            mark_data.add_item(self)
            return "Mark added successfully"
        return "Mark must be between 0 and 10"
    
    def get_marks(self, email):
        # get the marks of the student
        student_marks = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        for mark in mark_data:
            email_dec = Encryption(email).decrypt(mark["email"], "database/emails_encrypted.json")
            if email_dec == email:
                mark_dec = Encryption(email).decrypt(mark["mark"], "database/marks_encrypted.json")
                student_marks.append({"subject": mark["subject"], "exam": mark["exam"], "mark": mark_dec})
        return student_marks

    def get_average(self, email):
        marks = self.get_marks(email)
        sum = 0
        for mark in marks:
            sum += float(mark)
        return sum/len(marks)
