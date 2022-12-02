"""Manage the marks to be stored in the database"""
import json_manager
from attribute.email import Email
from attribute.subjects import Subjects
from attribute.exam import Exam
from encryption import Encryption
from sign_verification import SignVerification

class MarksManager:
    def __init__(self):
        self.subject = ""
        self.email = ""
        self.exam = ""
        self.mark = ""
        pass

    def add_mark(self, email_teacher, password, email_student, subject, exam, mark):
        """Add a mark to the database"""
        mark_data = json_manager.JsonManager("database/marks_database.json")
        # check the values entered and check that the student is registered
        self.email = Encryption(email_teacher, password).encrypt(Email(email_student).value)
        self.subject = Subjects(subject).value
        self.exam = Exam(exam).value
        if self.check_subjects(email_teacher, self.subject):
            if mark <= 10 and mark >= 0 and self.check_subjects(email_student, subject): # if everything is okay, add the mark into the marks database
                self.mark = Encryption(email_teacher, password).encrypt(str(mark)) # validate mark
                mark_data.add_item(self)
                return "Mark added successfully"
            return "Some of the parameters are not valid"
        return "The teacher is not registered in the subject"
    
    def check_subjects(self, email, subject):
        """Check if the user is registered in the subject"""
        users_data = json_manager.JsonManager("database/users_database.json").data
    
        for user in users_data:
            if user["email"] == email and subject in user["subjects"]:
                return True
        return False
    
    def get_marks(self, email_teacher, password, email_student, subject):
        """Get the marks of the student"""
        student_marks = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        for mark in mark_data:
            # decrypt the entered email and look for the marks of the student
            try:
                email_dec = Encryption(email_teacher, password).decrypt(mark["email"])
                if email_dec == email_student and mark["subject"] == subject:
                # if the student is found, decrypt the marks and add them to the list
                    mark_dec = Encryption(email_teacher, password).decrypt(mark["mark"])
                    # vaina de firma y verificación
                    # nos van a dar la clave publica del profe, y si está bien, todo chachi
                    student_marks.append({"subject": mark["subject"], "exam": mark["exam"], "mark": mark_dec})
            except:
                pass
        return student_marks
    
    def write_marks(self, email_teacher, password, email_student, subject):
        """Write the marks of the student"""
        marks = self.get_marks(email_teacher, password, email_student, subject)
        if len(marks) == 0:
            return "The student has no marks yet"
        file_name = "database/" + email_student + "_" + subject + ".txt"
        with open(file_name, "w") as file:
            file.write(str(marks))
        return  "Marks written successfully"

    def sign_marks(self, email_teacher, password, email_student, subject):
        """Sign the marks of the student"""
        written = self.write_marks(email_teacher, password, email_student, subject)
        if written == "The student has no marks yet":
            return written
        s = SignVerification()  
        private_key = self.search_private_key(email_teacher, password)
        s.sign_message(private_key, "database/" + email_student + "_" + subject + ".txt")
        return "Marks uploaded successfully"

    def search_private_key(self, email, password):
        """Search the private key of the user"""
        users_data = json_manager.JsonManager("database/users_database.json").data
        for user in users_data:
            if user["email"] == email:
                return SignVerification().decrypt_private_key(user["private_key"].encode('utf-8'), password)
        return "The teacher is not registered"

    def search_public_key(self, email):
        """Search the public key of the user"""
        users_data = json_manager.JsonManager("database/users_database.json").data
        for user in users_data:
            if user["email"] == email:
                return SignVerification().deserialize_public_key(user["public_key"].encode('utf-8'))
        return "The teacher is not registered"

    def verify_signed_marks(self, email_teacher, email_student, subject):
        """Verify the marks of the student"""
        s = SignVerification()
        public_key = self.search_public_key(email_teacher)
        return s.verify_signature(public_key, "database/" + email_student + "_" + subject + ".txt")

    def show_marks(self, email_teacher, email_student, subject):
        """Show the marks of the student"""
        verification = self.verify_signed_marks(email_teacher, email_student, subject)
        if verification == "The signature is not valid" or verification == "No marks were uploaded":
            print(verification)
            return "No marks to show"
        file_name = "database/" + email_student + "_" + subject + ".txt"
        with open(file_name, "rb") as file:
            data = file.read()[:-256]
        data = data.decode('utf-8')
        marks = []
        data = data.split("[")
        data.pop(0)
        data = data[0].split("}]")
        data.pop(-1)
        data = data[0].split("},")
        for mark in data:
            marks.append(mark + "}")
        mark_show = []
        for mark in marks:
            mark_show.append(mark[(16+len(subject)):-1] )
        return mark_show
