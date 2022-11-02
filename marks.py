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
        self.email = Encryption(email).encrypt(Email(email).value, "database/emails_encrypted.json") # validate email
        self.subject = Subjects(subject).value # validate subject
        self.exam = Exam(exam).value # validate exam
        if mark <= 10 and mark >= 0:
            self.mark = Encryption(email).encrypt(str(mark), "database/marks_encrypted.json") # validate mark
            mark_data.add_item(self)
            return "Mark added successfully"
        else:
            raise Exception("Mark must be between 0 and 10")
    
    # function to get marks from a student
    def get_marks(self, email):
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
    
    
mark_manager = MarksManager()
# mark_manager.add_mark("dd@email.com","Física", "Parcial 1", 3)
# mark_manager.add_mark("dd@email.com", "Química", "Parcial 1", 8)
# mark_manager.add_mark("dd@email.com", "Lengua", "Parcial 1", 5)
result = mark_manager.get_marks("dd@email.com")
print("OUR RESULT: ", result)
