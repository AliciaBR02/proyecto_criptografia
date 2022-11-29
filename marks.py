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

# base de datos - cif sim
# usuario pide algo -> se genera archivo y se pone la vaina de firma y verificación

    # funcion para el profesor
    def add_mark(self, email_teacher, password, email_student, subject, exam, mark):
        """Add a mark to the database"""
        mark_data = json_manager.JsonManager("database/marks_database.json")
        # check the values entered and check that the student is registered
        self.email = Encryption(email_teacher, password).encrypt(Email(email_student).value)
        self.subject = Subjects(subject).value
        self.exam = Exam(exam).value
        if mark <= 10 and mark >= 0 and self.check_subjects(email_student, subject): # if everything is okay, add the mark into the marks database
            self.mark = Encryption(email_teacher, password).encrypt(str(mark)) # validate mark
            mark_data.add_item(self)
            return "Mark added successfully"
        return "Some of the parameters are not valid"
    
    def check_subjects(self, email, subject):
        """Check if the student is registered in the subject"""
        students_data = json_manager.JsonManager("database/students_database.json").data
    
        for student in students_data:
            if student["email"] == email and subject in student["subjects"]:
                return True
    
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
    
    def sign_marks(self, email_teacher, password, email_student, subject):
        """Sign the marks of the student"""
        marks = self.get_marks(email_teacher, password, email_student, subject)
        # write marks in a file
        # create the file if it does not exist, and write it if it does
        file_name = "database/" + email_student + "_" + subject + ".txt"
        with open(file_name, "w") as file:
            file.write(str(marks))
        # sign the marks
        s = SignVerification()
        private_key = s.generate_private_key()
        s.generate_certificate(private_key)
        s.sign_message(private_key, file_name)
        public_key = s.generate_public_key(private_key)
        s.verify_signature(public_key, 'input_signed.txt')
        return marks

# CÓMO FUNCIONA LA FIRMAR Y VERIFICAR
# 1. (add_mark) El profesor genera un archivo con las notas del estudiante
# 2. El profesor firma el archivo con su clave privada -> ARCHIVO FIRMADO = mensaje + firma al final
# 3. (database) El profesor envía el archivo firmado al estudiante 
# 4. (get_mark) El estudiante verifica la firma con la clave pública del profesor
# 5. Si la firma es correcta, el estudiante puede ver las notas
# 6. Si la firma es incorrecta, el estudiante no puede ver las notas

# 7. El profesor puede ver las notas de todos los estudiantes
# 8. El estudiante puede ver sus notas
# 9. El estudiante no puede ver las notas de otros estudiantes

mark = MarksManager()
result = (mark.add_mark("profesor@mail.com", "123456", "estudiante@mail.com", "Mathematics", "Primer parcial", 10))
print(result)
print(mark.get_marks("profesor@mail.com", "123456", "estudiante@mail.com", "Mathematics"))
