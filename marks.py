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
        # print(email_teacher, password, email_student, subject, exam, mark)
        """Add a mark to the database"""
        mark_data = json_manager.JsonManager("database/marks_database.json")
        # check the values entered and check that the student is registered
        self.email = Encryption(email_teacher, password).encrypt(Email(email_student).value)
        self.subject = Subjects(subject).value
        self.exam = Exam(exam).value
        if self.check_teacher_subject(email_teacher, password, self.subject):
            if mark <= 10 and mark >= 0 and self.check_st_subjects(email_student, subject): # if everything is okay, add the mark into the marks database
                self.mark = Encryption(email_teacher, password).encrypt(str(mark)) # validate mark
                mark_data.add_item(self)
                return "Mark added successfully"
            return "Some of the parameters are not valid"
        return "The teacher is not registered in the subject"
    
    def check_st_subjects(self, email, subject):
        """Check if the student is registered in the subject"""
        students_data = json_manager.JsonManager("database/students_database.json").data
    
        for student in students_data:
            if student["email"] == email and subject in student["subjects"]:
                return True
        return False
    
    #check teacher subject
    def check_teacher_subject(self, email_teacher, password, subject):
        """Check if the teacher is registered in the subject"""
        teachers_data = json_manager.JsonManager("database/teachers_database.json").data
        for teacher in teachers_data:
            if teacher["email"] == email_teacher and subject in teacher["subjects"]:
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
        # write marks in a file
        # create the file if it does not exist, and write it if it does
        file_name = "database/" + email_student + "_" + subject + ".txt"
        with open(file_name, "w") as file:
            file.write(str(marks))
        return  "Marks written successfully"


# primero escribir las notas -> para decriptarlas, necesitamos que el profesor diga "quiero subirlas"
# para ello, el estudiante lo solicita, y el profesor lo acepta
# ahora el estudiante recibirá el archivo con las notas decriptadas -> tendrá que verificar la firma con su clave privada
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
        """Search the private key of the teacher"""
        teachers_data = json_manager.JsonManager("database/teachers_database.json").data
        for teacher in teachers_data:
            if teacher["email"] == email:
                return SignVerification().decrypt_private_key(teacher["private_key"].encode('utf-8'), password)
                
        return "The teacher is not registered"
    # verify with publick key of teacher
    def search_public_key(self, email):
        """Search the public key of the teacher"""
        teachers_data = json_manager.JsonManager("database/teachers_database.json").data
        for teacher in teachers_data:
            if teacher["email"] == email:
                return SignVerification().deserialize_public_key(teacher["public_key"].encode('utf-8'))

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
        # read file without reading signature (last 256 bytes)
        with open(file_name, "rb") as file:
            data = file.read()[:-256]
        print(data.decode('utf-8'))
        #add data to list
        return data.decode('utf-8')

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

# mark = MarksManager()
# result = (mark.add_mark("profesor@mail.com", "1234", "estudiante@mail.com", "Mathematics", "parcial", 10))
# print('///////////////////////////////////////////')
# print(result)
# print('///////////////////////////////////////////')
# mark.sign_marks("profesor@mail.com", "1234", "estudiante@mail.com", "Mathematics")
# print(mark.show_marks("profesor@mail.com", "estudiate@mail.com", "Mathematics"))
