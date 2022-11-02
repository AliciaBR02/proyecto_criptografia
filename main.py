from tkinter import *
import tkinter as tk
from tkinter import ttk
from registration import Registration
from login import Login
from marks import MarksManager
from tkinter import messagebox

def register():
    window_register.pack()
    if window_login:
        window_login.forget()

def sign_up():
    name = name_enter.get()
    surname = surname_enter.get()
    email = email_enter.get()
    password = password_enter.get()
    subjects_selected = []
    selected_indices = subjects.curselection()
    subjects_selected = [str(subjects.get(i)) for i in selected_indices]
    print(subjects_selected)
    register = Registration(name, surname, email, password, subjects_selected).register_student()
    messagebox.showinfo("Register", register)
    if register == "You have been registered successfully":
        window_student.pack()
        window_home.forget()
        window_register.forget()

def login_function():
    mail = email_enter.get()
    password = password_enter.get()
    l = Login(mail, password).login()
    messagebox.showinfo("Log In", l)
    if l == "User logged in successfully":
        window_student.pack()
        window_home.forget()
        window_login.forget()


def login():
    window_login.pack()
    if window_register:
        window_register.forget()

def add_nota():
    window_add_mark.pack()

def add_mark():
    email = email_enter.get()
    exam = exam_enter.get()
    mark = mark_enter.get()
    subject_add = subjects.get(ACTIVE)
    mark_manager = MarksManager()
    mark = mark_manager.add_mark(email, subject_add, exam, int(mark))
    messagebox.showinfo("Marks", mark )
    if mark == "Mark added successfully":
        window_student.pack()
        window_add_mark.forget()

    
def page_search():
    window_search.pack()
    
def search():
    email = email_enter.get()
    password = password_enter.get()
    l = Login(email, password).login()
    if (l == "User logged in successfully"):
        mark_manager = MarksManager()
        result = mark_manager.get_marks(email)
        marks_result = ''
        if len(result) != 0:
            for i in result:
                marks_result += i["subject"] + "->" + i["exam"] + ": " + str(i["mark"]) + "\n\n"
        else:
            marks_result = "No marks available"
        messagebox.showinfo("Marks", marks_result)
    else:        
        messagebox.showinfo("Error", "Incorrect data")

# -------------------- MAIN ----------------------

global window_principal
pestas_color = "#76D7C4"
accept_color = "#6666FF"
window_principal = tk.Tk()
global name
global surname
global email
global password
global subjects
global exam
global mark
name = StringVar()
surname = StringVar()
email = StringVar()
password = StringVar()
resultado_notas = StringVar()
exam = StringVar()
mark = IntVar()

window_principal.geometry("1500x800")
window_principal.title("Face2Learn")

global ventana_inicio
window_home = Frame(window_principal)
window_home.pack()
Label(window_home, text="Pick an option", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(window_home,text="").pack()
Button(window_home, text="Sign in", height="2", width="30", bg=pestas_color, command=login).pack()
Label(window_home, text="").pack()
Button(window_home, text="Sign up", height="2", width="30", bg=pestas_color, command=register).pack()
Label(window_home, text="").pack()



# -------------------- LOGIN ----------------------

global ventana_login
window_login = Frame(window_principal)

Label(window_login, text="Please enter details below to login").pack()
Label(window_login, text="").pack()
etiqueta_email = Label(window_login, text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_login, textvariable=email)
email_enter.pack()

etiqueta_password = Label(window_login, text="Password * ")
etiqueta_password.pack()
password_enter = Entry(window_login, textvariable=password, show='*')
password_enter.pack()

Label(window_login, text="").pack()
Button(window_login, text="Enter", width=10, height=1, bg=accept_color, command=login_function).pack()



# -------------------- REGISTER ----------------------

global ventana_registro
window_register = Frame(window_principal)
window_register.config(width=300, height=250)
subjects = Listbox(window_register, selectmode=MULTIPLE)
lists_subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Language", "English", "French", "German", "History", "Geography", "Philosophy", "Economics", "Technical Drawing", "Computer Science", "Physical Education", "Religion"]
for i in lists_subjects:
    subjects.insert(END, i)

Label(window_register, text="Please enter details below to register").pack()
Label(window_register, text="").pack()
etiqueta_nombre = Label(window_register, text="Name * ")
etiqueta_nombre.pack()
name_enter = Entry(window_register, textvariable=name)
name_enter.pack()

etiqueta_apellido = Label(window_register, text="Surname * ")
etiqueta_apellido.pack()
surname_enter = Entry(window_register, textvariable=surname)
surname_enter.pack()

etiqueta_email = Label(window_register, text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_register, textvariable=email)
email_enter.pack()

etiqueta_password = Label(window_register, text="Password * ")
etiqueta_password.pack()
password_enter = Entry(window_register, textvariable=password, show='*')
password_enter.pack()

etiqueta_subjects = Label(window_register, text="Subject * ")
etiqueta_subjects.pack()
subjects.pack()

Label(window_register, text="").pack()

Button(window_register, text="Sign up", height="2", width="20", bg=accept_color, command=sign_up).pack()

# --------------------- STUDENT ----------------------
global ventana_student
window_student = Frame(window_principal)
window_student.config(width=300, height=250)

Label(window_student, text="Welcome").pack()

Label(window_student, text="").pack()

Button(window_student, text="Search", height="2", width="20", bg=accept_color, command=page_search).pack()

Button(window_student, text = 'Add mark', height="2", width="20", bg=accept_color, command=add_nota).pack()

#--------------------- SEARCH ----------------------
global ventana_buscar
window_search = Frame(window_principal)
window_search.config(width=300, height=250)

Label(window_search, text="For security reasons, enter your email and password again, please").pack()
Label(window_search, text="").pack()

etiqueta_email = Label(window_search, text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_search, textvariable=email)
email_enter.pack()
etiqueta_password = Label(window_search, text="Password * ")
etiqueta_password.pack()
password_enter = Entry(window_search, textvariable=password, show='*')
password_enter.pack()
Label(window_search, text="").pack()
Button(window_search, text = 'Search', height="2", width="20", bg=accept_color, command=search).pack()



#--------------------- ADD NOTA ----------------------
global ventana_add_mark
window_add_mark = Frame(window_principal)
window_add_mark.config(width=300, height=250)
subjects_mark = Listbox(window_add_mark, selectmode=SINGLE)

lists_subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Language", "English", "French", "German", "History", "Geography", "Philosophy", "Economics", "Technical Drawing", "Computer Science", "Physical Education", "Religion"]
for i in lists_subjects:
    subjects_mark.insert(END, i)

Label(window_add_mark, text="Please enter the mark below").pack()
Label(window_add_mark, text="").pack()

etiqueta_email = Label(window_add_mark, text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_add_mark, textvariable=email)
email_enter.pack()


etiqueta_subjects = Label(window_add_mark, text="Subject * ")
etiqueta_subjects.pack()
subjects_mark.pack()


etiqueta_exam = Label(window_add_mark, text="Exam * ")
etiqueta_exam.pack()
exam_enter = Entry(window_add_mark, textvariable=exam)
exam_enter.pack()

etiqueta_mark = Label(window_add_mark, text="Mark * ")
etiqueta_mark.pack()
mark_enter = Entry(window_add_mark, textvariable=mark)
mark_enter.pack()

Label(window_add_mark, text="").pack()

Button(window_add_mark, text = 'Add', height="2", width="20", bg=accept_color, command=add_mark).pack()



window_principal.mainloop()

