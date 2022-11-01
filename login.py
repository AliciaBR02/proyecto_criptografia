""""""
from json_manager import JsonManager
import student
from encryptation import Encryptation

class Login:
    def __init__(self, email, password):
        self._email = email
        self._password = password
        self._data = []
        self.load_data()
        self.login_student()
        
    def load_data(self):
        self._data = JsonManager("students_database").data
        
    # def login_student(self):
    #     s = student.Student.login(self._email, self._password)
        
    
                

# student = Login("ola@qugdagetal.com", "123456")
# student.login()

# email, asignatura, examen de la asignatura, nota del examen
# cifrar email, nota