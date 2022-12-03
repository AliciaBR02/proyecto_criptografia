from marks import Marks
import base64
import sign_verification



def show_marks(self, email_student,password,  subject):
        file_name = "database/" + email_student + "_" + subject + ".txt"
        with open(file_name, "rb") as file:
            marks = file.read()[:-256]
        marks = base64.b64decode(marks)
        marks = self.decrypt_marks(marks, email_student, password)
        return marks

print(show_marks(Marks.Marks(), "val@email.com", "1234", "Math"))