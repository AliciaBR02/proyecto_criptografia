"""Manage the marks to be stored in the database"""
import json_manager
from attribute.email import Email
from attribute.subjects import Subjects
from attribute.exam import Exam
from encryption import Encryption
from sign_verification import SignVerification
import base64
import json

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
        # check if the user is registered in the subject
        for user in users_data:
            if user["email"] == email and subject in user["subjects"]:
                return True
        return False
    
    def write_marks(self, email_teacher, password, email_student, subject):
        """Get the marks of the student"""
        student_marks = {}
        student_mark = []
        mark_data = json_manager.JsonManager("database/marks_database.json").data
        #create a json file with the marks of the student
        with open("database/" + email_student + "_" + subject + ".json", "w") as f:
            json.dump("[]", f)
            f.close()

        for mark in mark_data:
            # decrypt the entered email and look for the marks of the student
            try:
                email_dec = Encryption(email_teacher, password).decrypt(mark["email"])
                if email_dec == email_student and mark["subject"] == subject:
                # if the student is found, decrypt the marks and add them to the list
                    mark_dec = Encryption(email_teacher, password).decrypt(mark["mark"])
                    with open("database/" + email_student + "_" + subject + ".json") as f:
                        enc_marks = self.encrypt_marks(mark_dec, email_student)
                    student_marks["exam"] =  mark["exam"]
                    student_marks["mark"] = base64.b64encode(enc_marks).decode('utf-8')
                    student_mark.append(student_marks)
                    
            except:
                pass
        print(student_mark)
        return student_mark    
    
    def encrypt_marks(self, marks, email_student):
        # encrypt the marks with the public key of the student
        s = SignVerification()
        public_key = self.search_public_key(email_student)
        return s.encrypt_message( base64.b64encode(marks.encode('utf-8')), public_key)

    def decrypt_marks(self, marks, email_student, password):
        # decrypt the marks with the private key of the student
        s = SignVerification()
        private_key = self.search_private_key(email_student, password)
        return base64.b64decode(s.decrypt_message(private_key, marks)).decode('utf-8')


    def sign_marks(self, email_teacher, password, email_student, subject):
        """Sign the marks of the student"""
        written = self.write_marks(email_teacher, password, email_student, subject)
        if written == []:
            return "The student has no marks yet"
        file_name = "database/" + email_student + "_" + subject + ".json"
        for mark in written:
            # encrypt the marks with the private key of the teacher
            s = SignVerification()
            private_key = self.search_private_key(email_teacher, password)
            mark["signature"] = s.sign_message(private_key, file_name)
        # write the marks in the json file
        with open("database/" + email_student + "_" + subject + ".json", 'w') as f:
            json.dump(written, f)
            f.close()
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
        return s.verify_signature(public_key, "database/" + email_student + "_" + subject + ".json")

    def show_marks(self, email_teacher, email_student, password,  subject):
        """Show the marks of the student"""
        verification = self.verify_signed_marks(email_teacher, email_student, subject)
        # check if the marks are signed by the teacher
        if verification == "The signature is not valid" or verification == "No marks were uploaded":
            return "No marks to show"
        file_name = "database/" + email_student + "_" + subject + ".json"
        marks = json_manager.JsonManager(file_name).data
        marks_shown = ""
        for mark in marks:
            # decrypt the marks with the private key of the student
            mark['mark'] = self.decrypt_marks(base64.b64decode(mark['mark'].encode('utf-8')), email_student, password)
            marks_shown += mark["exam"] + ": " + mark["mark"] + "\n"
        return marks_shown
    