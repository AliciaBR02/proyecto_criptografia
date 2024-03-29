from tkinter import * #type: ignore
import tkinter as tk
from tkinter import ttk
from registration import Registration
from login import Login
from marks import MarksManager
from tkinter import messagebox

#---------------------------------FUNCTIONS FOR EACH WINDOW---------------------------------#

# Register
def register():
    """Sign up window"""
    window_register.pack()
    # Hide log in window
    if window_login:
        window_login.forget()

def sign_up_st():
    """Sign up function"""
    # Get data from entry fields
    name = name_enter.get()
    surname = surname_enter.get()
    email = email_enter.get()
    password = password_enter.get()
    subjects_selected = []
    # Get selected subjects
    selected_indices = subjects.curselection()
    subjects_selected = [str(subjects.get(i)) for i in selected_indices]
    # Register user
    register = Registration(name, surname, email, password, "Student", subjects_selected).register()
    # Show message
    messagebox.showinfo("Register", register)
    if register == "You have been registered successfully":
        window_student.pack()
        window_home.forget()
        window_register.forget()

def sign_up_teacher():
    """Sign up function"""
    # Get data from entry fields
    name = name_enter.get()
    surname = surname_enter.get()
    email = email_enter.get()
    password = password_enter.get()
    subjects_selected = []
    # Get selected subjects
    selected_indices = subjects.curselection()
    subjects_selected = [str(subjects.get(i)) for i in selected_indices]
    # Register user
    register = Registration(name, surname, email, password, "Teacher", subjects_selected).register()
    # Show message
    messagebox.showinfo("Register", register)
    if register == "You have been registered successfully":
        window_teacher.pack()
        window_home.forget()
        window_register.forget()

# Log in
def login_function():
    """Log in function"""
    mail = email_enter.get()
    password = password_enter.get()
    # Login user
    l, role = Login(mail, password).login()
    messagebox.showinfo("Log In", l)
    if l == "User logged in successfully" and role == "Student":
        window_student.pack()
        window_home.forget()
        window_login.forget()
    elif l == "User logged in successfully" and role == "Teacher":
        window_teacher.pack()
        window_home.forget()
        window_login.forget()

def login():
    """Log in window"""
    window_login.pack()
    if window_register:
        window_register.forget()

# Añadir nota
def add_nota():
    """Add mark window"""
    window_add_mark.pack()
    if window_upload_mark:
        window_upload_mark.forget()

def add_mark():
    """Add mark function"""
    email = email_teacher_to_mark_enter.get()
    password = password_teacher_to_mark_enter.get()
    email_student = email_student_to_mark_enter.get()
    subject = subjects_mark.get(subjects_mark.curselection())
    exam = exam_enter.get()
    mark = mark_enter.get()
    # Check that user is logged in
    l, role = Login(email, password).login()
    if (l == "User logged in successfully" and role == "Teacher"):
        # Add mark
        mark_manager = MarksManager()
        result = mark_manager.add_mark(email, password, email_student, subject, exam, int(mark))
        messagebox.showinfo("Marks", result)
        window_add_mark.forget()

    else:        
        messagebox.showinfo("Error", "Incorrect data")

def upload_mark():
    """Upload marks window"""
    window_upload_mark.pack()
    if window_add_mark:
        window_add_mark.forget()
    
def upload_marks():
    """Upload marks function"""
    email = email_teacher_to_upload_enter.get()
    password = password_teacher_to_upload_enter.get()
    email_student = email_student_to_upload_enter.get()
    subject = subjects_upload.get(subjects_upload.curselection())

    # Check that user is logged in
    l, role = Login(email, password).login()
    if (l == "User logged in successfully"and role == "Teacher"):
        # Add mark
        mark_manager = MarksManager()
        message = mark_manager.sign_marks(email, password, email_student, subject)
        messagebox.showinfo("Marks", message)
        window_upload_mark.forget()
    else:        
        messagebox.showinfo("Error", "Incorrect data")

# Buscar nota
def page_search():
    """Search marks window"""
    window_search.pack()

def show_marks():
    """Search marks function"""
    teacher = teacher_enter.get()
    email_st = email_search_enter.get()
    password = password_search_enter.get()
    subject_to_search = subject_search.get(subject_search.curselection())
    # Check that user is logged in
    l, role = Login(email_st, password).login()
    if (l == "User logged in successfully" and role == "Student"):
        # Add mark
        mark_manager = MarksManager()
        message = mark_manager.show_marks(teacher, email_st, password, subject_to_search)
        messagebox.showinfo("Marks", message)
    else:        
        messagebox.showinfo("Error", "Incorrect data")
    


# -------------------- MAIN ----------------------

# Create window
global window_principal
pestas_color = "#F9BE35"
accept_color = "#24373C"
background_color = "#2D2D2D"
window_principal = tk.Tk()
window_principal.config(bg=background_color)
window_principal.geometry("1500x800")
window_principal.title("Face2Learn")

# Set global variables
global name
global surname
global email
global password
global subjects
global exam
global mark
global role
name = StringVar()
surname = StringVar()
email = StringVar()
password = StringVar()
resultado_notas = StringVar()
exam = StringVar()
mark = IntVar()
role = StringVar()


# ------------------ HOME -----------------------
# Create home window
global window_home
window_home = Frame(window_principal)
window_home.config(width=300, height=250, bg=background_color)
window_home.pack()
# Select between log in and sign up
Label(window_home, text="Pick an option", bg=background_color, fg='#ffF', width="300", height="2", font=("Calibri", 13)).pack()
Label(window_home,text="", bg=background_color, fg='#ffF').pack()
Button(window_home, text="Log in", height="2", width="30", bg=pestas_color, command=login).pack()
Label(window_home, text="", bg=background_color, fg='#ffF').pack()
Button(window_home, text="Sign up", height="2", width="30", bg=pestas_color, command=register).pack()
Label(window_home, text="", bg=background_color, fg='#ffF').pack()



# -------------------- LOGIN ----------------------
# Create log in window
global window_login
window_login = Frame(window_principal)
window_login.config(width=300, height=250, bg=background_color)


# Log in form
Label(window_login, text="Please enter details below to login", fg='#ffF', bg=background_color).pack()
Label(window_login, text="", bg=background_color).pack()

etiqueta_email = Label(window_login, bg=background_color, fg='#ffF', text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_login, textvariable=email)
email_enter.pack()

etiqueta_password = Label(window_login, bg=background_color, fg='#ffF', text="Password * ")
etiqueta_password.pack()
password_enter = Entry(window_login, textvariable=password, show='*')
password_enter.pack()

Label(window_login, text="", bg=background_color).pack()

# Log in button
Button(window_login, text="Log In", width=20, height=2, bg=accept_color, fg='#ffF', command=login_function).pack()



# -------------------- SIGN UP ----------------------
# Create sign up window
global window_register
window_register = Frame(window_principal)
window_register.config(width=300, height=250, bg=background_color)

# Subjects list
subjects = Listbox(window_register, selectmode=MULTIPLE)
lists_subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "Language", "English", "French", "German", "History", "Geography", "Philosophy", "Economics", "Technical Drawing", "Computer Science", "Physical Education", "Religion"]
for i in lists_subjects:
    subjects.insert(END, i)

# Sign up form
Label(window_register, text="Please enter details below to register", fg='#ffF', bg=background_color).pack()
Label(window_register, text="", bg=background_color).pack()
etiqueta_nombre = Label(window_register, bg=background_color, fg='#ffF', text="Name * ")
etiqueta_nombre.pack()
name_enter = Entry(window_register, textvariable=name)
name_enter.pack()

etiqueta_apellido = Label(window_register, bg=background_color, fg='#ffF', text="Surname * ")
etiqueta_apellido.pack()
surname_enter = Entry(window_register, textvariable=surname)
surname_enter.pack()

etiqueta_email = Label(window_register, bg=background_color, fg='#ffF', text="Email * ")
etiqueta_email.pack()
email_enter = Entry(window_register, textvariable=email)
email_enter.pack()

etiqueta_password = Label(window_register, bg=background_color, fg='#ffF', text="Password * ")
etiqueta_password.pack()
password_enter = Entry(window_register, textvariable=password, show='*')
password_enter.pack()

etiqueta_subjects = Label(window_register, bg=background_color, fg='#ffF', text="Subject * ")
etiqueta_subjects.pack()
subjects.pack()

Label(window_register, text="", bg=background_color).pack()

# Sign up button
Button(window_register, text="Student", fg='#ffF', height="2", width="20", bg=accept_color, command=sign_up_st).pack()
Button(window_register, text="Teacher", fg='#ffF', height="2", width="20", bg=accept_color, command=sign_up_teacher).pack()


# --------------------- STUDENT ----------------------
# Create student window
global window_student
window_student = Frame(window_principal)
window_student.config(width=300, height=250, bg=background_color)

Label(window_student, text="Welcome", fg='#ffF', bg=background_color).pack()

Label(window_student, text="", bg=background_color).pack()

# Select between add mark and search marks
Button(window_student, text="Search", fg='#ffF', height="2", width="20", bg=accept_color, command=page_search).pack()

# --------------------- TEACHER ----------------------
global window_teacher
window_teacher = Frame(window_principal)
window_teacher.config(width=300, height=250, bg=background_color)

Label(window_teacher, text="Welcome", fg='#ffF', bg=background_color).pack()

Label(window_teacher, text="", bg=background_color).pack()

# Select between add mark,  search marks and upload marks
Button(window_teacher, text="Add mark", height="2", width="20", bg=accept_color, command=add_nota).pack()
Button(window_teacher, text = 'Upload marks', height="2", width="20", bg=accept_color, command=upload_mark).pack()

#--------------------- SEARCH ----------------------
# Create search window
global window_search
window_search = Frame(window_principal)
window_search.config(width=300, height=250, bg=background_color)

Label(window_search, bg=background_color, fg='#ffF', text="Enter the following information").pack()
Label(window_search, bg=background_color, text="").pack()

subject_search = Listbox(window_search, selectmode=SINGLE)
for i in lists_subjects:
    subject_search.insert(END, i)

# Add mark form
Label(window_search, bg=background_color, fg='#ffF', text="Please enter the mark below").pack()
Label(window_search, bg=background_color, text="").pack()

etiqueta_subjects = Label(window_search, fg='#ffF', bg=background_color, text="Subject * ")
etiqueta_subjects.pack()
subject_search.pack()

global teacher_search
teacher_search = StringVar()
etiqueta_teacher = Label(window_search, fg='#ffF', bg=background_color, text="Teacher * ")
etiqueta_teacher.pack()
teacher_enter = Entry(window_search, textvariable=teacher_search)
teacher_enter.pack()
Label(window_search, bg=background_color, text="").pack()

Label(window_search, bg=background_color, fg='#ffF', text="For security reasons, enter your email and password again, please").pack()
Label(window_search, bg=background_color, text="").pack()

# Enter email and password for security reasons
global email_search
email_search = StringVar()
etiqueta_email_search = Label(window_search, fg='#ffF', bg=background_color, text="Email * ")
etiqueta_email_search.pack()
email_search_enter = Entry(window_search, textvariable=email_search)
email_search_enter.pack()

global password_search
password_search = StringVar()
etiqueta_password_search = Label(window_search, fg='#ffF', bg=background_color, text="Password * ")
etiqueta_password_search.pack()
password_search_enter = Entry(window_search, textvariable=password_search, show='*')
password_search_enter.pack()

Label(window_search, text="", bg=background_color).pack()

# Search button
Button(window_search, text = 'Show Marks', fg='#ffF', height="2", width="20", bg=accept_color, command=show_marks).pack()



#--------------------- ADD NOTA ----------------------
# Create add mark window
global window_add_mark
window_add_mark = Frame(window_principal)
window_add_mark.config(width=300, height=250, bg=background_color)
subjects_mark = Listbox(window_add_mark, selectmode=SINGLE)

# list of subjects
for i in lists_subjects:
    subjects_mark.insert(END, i)

# Add mark form
Label(window_add_mark, fg='#ffF', bg=background_color, text="Please enter the mark below").pack()
Label(window_add_mark, bg=background_color, text="").pack()

etiqueta_subjects = Label(window_add_mark, bg=background_color, text="Subject * ")
etiqueta_subjects.pack()
subjects_mark.pack()

global email_student_to_mark
email_student_to_mark = StringVar()
email_student_to_mark_exam = Label(window_add_mark, fg='#ffF', bg=background_color, text="Student * ")
email_student_to_mark_exam.pack()
email_student_to_mark_enter = Entry(window_add_mark, textvariable=email_student_to_mark)
email_student_to_mark_enter.pack()

etiqueta_exam = Label(window_add_mark, fg='#ffF', bg=background_color, text="Exam * ")
etiqueta_exam.pack()
exam_enter = Entry(window_add_mark, textvariable=exam)
exam_enter.pack()

etiqueta_mark = Label(window_add_mark, fg='#ffF', bg=background_color, text="Mark * ")
etiqueta_mark.pack()
mark_enter = Entry(window_add_mark, textvariable=mark)
mark_enter.pack()

Label(window_add_mark, bg=background_color, text="").pack()
Label(window_add_mark, fg='#ffF', bg=background_color, text="Comfirm identity").pack()

global email_teacher_to_mark
email_teacher_to_mark = StringVar()
etiqueta_email_teacher_to_mark = Label(window_add_mark, fg='#ffF', bg=background_color, text="Email * ")
etiqueta_email_teacher_to_mark.pack()
email_teacher_to_mark_enter = Entry(window_add_mark, textvariable=email_teacher_to_mark)
email_teacher_to_mark_enter.pack()

global password_teacher_to_mark
password_teacher_to_mark = StringVar()
etiqueta_password_teacher_to_mark = Label(window_add_mark, fg='#ffF', bg=background_color, text="Password * ")
etiqueta_password_teacher_to_mark.pack()
password_teacher_to_mark_enter = Entry(window_add_mark, textvariable=password_teacher_to_mark, show='*')
password_teacher_to_mark_enter.pack()

Label(window_add_mark, bg=background_color, text="").pack()

# Add mark button
Button(window_add_mark, text = 'Add', fg='#ffF', height="2", width="20", bg=accept_color, command=add_mark).pack()

#--------------------- UPLOAD MARK ----------------------
# Create upload mark window
global window_upload_mark
window_upload_mark = Frame(window_principal)
window_upload_mark.config(width=300, height=250, bg=background_color)
subjects_upload = Listbox(window_upload_mark, selectmode=SINGLE)

# list of subjects
for i in lists_subjects:
    subjects_upload.insert(END, i)

# Upload mark form
Label(window_upload_mark, fg='#ffF', bg=background_color, text="Please enter the mark below").pack()
Label(window_upload_mark, bg=background_color, text="").pack()

etiqueta_subjects = Label(window_upload_mark, fg='#ffF', bg=background_color, text="Subject * ")
etiqueta_subjects.pack()
subjects_upload.pack()

global email_student_to_upload
email_student_to_upload = StringVar()
email_student_to_upload_exam = Label(window_upload_mark, fg='#ffF', bg=background_color, text="Student * ")
email_student_to_upload_exam.pack()
email_student_to_upload_enter = Entry(window_upload_mark, textvariable=email_student_to_upload)
email_student_to_upload_enter.pack()

Label(window_upload_mark, bg=background_color, text="").pack()
Label(window_upload_mark, fg='#ffF', bg=background_color, text="Comfirm identity").pack()

global email_teacher_to_upload
email_teacher_to_upload = StringVar()
etiqueta_email_teacher_to_upload = Label(window_upload_mark, fg='#ffF', bg=background_color, text="Email * ")
etiqueta_email_teacher_to_upload.pack()
email_teacher_to_upload_enter = Entry(window_upload_mark, textvariable=email_teacher_to_upload)
email_teacher_to_upload_enter.pack()

global password_teacher_to_upload
password_teacher_to_upload = StringVar()
etiqueta_password_teacher_to_upload = Label(window_upload_mark, fg='#ffF', bg=background_color, text="Password * ")
etiqueta_password_teacher_to_upload.pack()
password_teacher_to_upload_enter = Entry(window_upload_mark, textvariable=password_teacher_to_upload, show='*')
password_teacher_to_upload_enter.pack()

Label(window_upload_mark, bg=background_color, text="").pack()

# Add mark button
Button(window_upload_mark, text = 'Upload', height="2", width="20", bg=accept_color, command=upload_marks).pack()



# Execute the main window
window_principal.mainloop()

