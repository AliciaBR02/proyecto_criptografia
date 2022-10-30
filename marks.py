import json_manager
from attribute.email import Email
from attribute.subjects import Subjects
from attribute.exam import Exam

class MarksManager:
    def __init__(self):
        self.subject = ""
        self.email = ""
        self.exam = ""
        self.marks = 0
        self._load_marks()
    
    def _load_marks(self):
        # load marks from file
        self._marks = json_manager.JsonManager("database/marks_database.json").data

    def _store_marks(self):
        # store marks into file
        json_manager.JsonManager("database/marks_database.json").store(self._marks)
    
    def add_mark(self, email, subject, exam, mark):
        # self._marks.append(mark.__dict__)
        # self._store_marks()
        mark_data = json_manager.JsonManager("database/marks_database.json")
        self.email = Email(email).value # validate email
        self.subject = Subjects(subject).value # validate subject
        self.exam = Exam(exam).value # validate exam
        if mark <= 10 and mark >= 0:
            self._marks = mark
        else:
            raise Exception("Mark must be between 0 and 10")
        mark_data.add_item(self)
    
    # function to get marks from a student
    def get_marks(self, email):
        student_marks = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        for mark in mark_data:
            if mark["email"] == email:
                student_marks.append(mark)
        return student_marks

mark_manager = MarksManager()
mark_manager.add_mark("hola@email.com","Matemáticas", "exam", 10)
print(mark_manager.get_marks("hola@email.com"))