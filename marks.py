import json_manager
from attribute.email import Email
from attribute.subjects import Subjects
from attribute.exam import Exam
from encryptation import Encryptation

class MarksManager:
    def __init__(self):
        self.subject = ""
        self.email = ""
        self.exam = ""
        self.mark = ""
        pass

    def add_mark(self, email, subject, exam, mark):
        mark_data = json_manager.JsonManager("database/marks_database.json")
        self.email = Encryptation().encrypt(Email(email).value, "database/emails_encrypted.json") # validate email
        self.subject = Subjects(subject).value # validate subject
        self.exam = Exam(exam).value # validate exam
        if mark <= 10 and mark >= 0:
            self.mark = Encryptation().encrypt(str(mark), "database/marks_encrypted.json") # validate mark
            mark_data.add_item(self)
        else:
            raise Exception("Mark must be between 0 and 10")
    
    # function to get marks from a student
    def get_marks(self, email):
        # email_input = Encryptation().encrypt(Email(email).value, "emails_encrypted.json").decode('utf-8')
        # print(email_input)
        student_marks = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        for mark in mark_data:
            # print(mark["email"])
            email_dec = Encryptation().decrypt(mark["email"].encode('utf-8'), "database/emails_encrypted.json")
            if email_dec == email:
                mark_dec = Encryptation().decrypt(mark, "database/marks_encrypted.json")
                student_marks.append(mark_dec)
        return student_marks


mark_manager = MarksManager()
mark_manager.add_mark("hola@email.com","Matemáticas", "exam", 10)
# print(mark_manager.get_marks("hola@email.com"))