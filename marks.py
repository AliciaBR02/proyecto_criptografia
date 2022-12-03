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
                    enc_marks = self.encrypt_marks(mark_dec, email_student)
                    print('MArk: ', mark_dec)
                    # vaina de firma y verificación
                    # nos van a dar la clave publica del profe, y si está bien, todo chachi
                    print(enc_marks.decode('utf-8'))
                    student_marks.append({"exam": mark["exam"], "mark": enc_marks.decode('utf-8')})
                    print('apendeado: ', student_marks)
            except:
                pass
        # print(student_marks)
        return student_marks
    
    def encrypt_marks(self, marks, email_student):
        s = SignVerification()
        # marks = base64.b64encode(marks.encode('utf-8'))
        public_key = self.search_public_key(email_student)
        return s.encrypt_message( base64.b64encode(bytes(marks.encode('utf-8'))), public_key)
    # bytes(x) = x.encode(utf-8)
    def decrypt_marks(self, marks, email_student, password):
        s = SignVerification()
        private_key = self.search_private_key(email_student, password)
        return s.decrypt_message(private_key, marks).decode('utf-8')
    
    def write_marks(self, email_teacher, password, email_student, subject):
        """Write the marks of the student"""
        marks = self.get_marks(email_teacher, password, email_student, subject)
        if len(marks) == 0:
            return "The student has no marks yet"
        # json convert string into dictionary
        # marks_write = ""
        # marks = str(marks).split("[")
        # marks.pop(0)
        # marks = marks[0].split("}]")
        # marks.pop(-1)
        # try:
        #     marks = marks[0].split("},")
        # except:
        #     pass

        # for mark in marks:
        #     marks_write += mark + "}"
        # for m in marks_write:
        #     if m == '"':
        #         marks_write = marks_write.replace(m, "")
        #     elif m == ":":
        #         marks_write = marks_write.replace(m, "=")
        # reemplazar la nota por la nota encriptada
        # create a file with the marks of the student
        # print(marks)
              
        with open("database/" + email_student + "_" + subject + ".json", "w") as file:
            # json.dump(marks, file)
            jsonstring = json.dumps(marks)
            file.write(jsonstring)
            file.close()
        
        database = json_manager.JsonManager("database/" + email_student + "_" + subject + ".json")
        database.add_item(marks)
        # file_name = "database/" + email_student + "_" + subject + ".json"
        # database = json_manager.JsonManager(file_name)
        # database.add_item(marks)
        # with open(file_name, "w") as file:
        #     file.write(marks_write)
        return  "Marks written successfully"

    def sign_marks(self, email_teacher, password, email_student, subject):
        """Sign the marks of the student"""
        written = self.write_marks(email_teacher, password, email_student, subject)
        if written == "The student has no marks yet":
            return written
        s = SignVerification()  
        private_key = self.search_private_key(email_teacher, password)
        s.sign_message(private_key, "database/" + email_student + "_" + subject + ".json")
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
        if verification == "The signature is not valid" or verification == "No marks were uploaded":
            # print(verification)
            return "No marks to show"
        file_name = "database/" + email_student + "_" + subject + ".json"
        with open(file_name, "r") as file:
            marks = file.read()[:-256]
            file.close()
        # de marks sacar la nota encriptada
        
        
        marks = base64.b64decode(marks)
        # print(len(marks))
        marks = self.decrypt_marks(marks[:-1], email_student, password)
        return marks
    
marks = MarksManager()
(marks.add_mark("alibr@email.com", "Alibrum12$", "val@email.com", "Mathematics", "1", 10))
(marks.sign_marks("alibr@email.com", "Alibrum12$", "val@email.com", "Mathematics"))
print(marks.show_marks("alibr@email.com", "val@email.com", "password", "Mathematics"))

