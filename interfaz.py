# from curses.textpad import rectangle
from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
from registration import Registration
from login import Login
from marks import MarksManager
from tkinter import messagebox
# from tkinter import messagebox
# from tkinter import filedialog
# from tkinter import *
# from tkinter import ttk as tk

# # Creamos la ventana
# root = tk.Tk()

# # Creamos el canvas
# canvas = tk.Canvas(root, width=900, height=600)

# # Crear interfaz para el canvas
# # canvas.pack()

# # Crear botones
# button = tk.Button(root, text="Boton 1", bg="red", fg="white")

# # Crear etiquetas
# label = tk.Label(root, text="Etiqueta 1", bg="blue", fg="white")
# # Crear cajas de texto
# entry = tk.Entry(root, width=50, bg="white", fg="black", borderwidth=5)

# # Enlazar botón con clase registro
# button.bind("<Button-1>")

# # Creamos el rectángulo
# rectangulo = canvas.create_rectangle(10, 10, 100, 100, fill="red")

# # Creamos el texto
# texto = canvas.create_text(60, 60, text="Hola mundo")

# # Mostramos el canvas
# canvas.pack()

# # Mostramos la ventana
# root.mainloop()
    


    
    

# def cambiar_ventana():
    #framealquevoy.pack()
    #framedelquevengo.forget
def registro():
    ventana_registro.pack()
    if ventana_login:
        ventana_login.forget()


def registrarse():
    name = entrada_nombre.get()
    surname = entrada_apellido.get()
    email = entrada_email.get()
    password = entrada_password.get()
    subjects_selected = []
    # print(len(subjects))
    selected_indices = subjects.curselection()
    # get selected items
    subjects_selected = [str(subjects.get(i)) for i in selected_indices]
    register = Registration(name, surname, email, password, subjects_selected).register_student()
    messageBox = messagebox.showinfo("Registro", register)
    if register == "You have been registered successfully":
        ventana_student.pack()
        ventana_inicio.forget()
        ventana_registro.forget()

def iniciar_sesion():
    mail = entrada_email.get()
    password = entrada_password.get()
    l = Login(mail, password).login()
    messageBox = messagebox.showinfo("Log In", l)
    if l == "User logged in successfully":
        ventana_student.pack()
        ventana_inicio.forget()
        ventana_login.forget()


def login():
    ventana_login.pack()
    if ventana_registro:
        ventana_registro.forget()
    # Label(ventana_login, text="Por favor ingrese los datos a continuación").pack()
    # Label(ventana_login, text="").pack()
    # etiqueta_email = Label(ventana_login, text="Email * ")
    # etiqueta_email.pack()
    # entrada_email = Entry(ventana_login, textvariable=email)
    # entrada_email.pack()
    
    # etiqueta_password = Label(ventana_login, text="Contraseña * ")
    # etiqueta_password.pack()
    # entrada_password = Entry(ventana_login, textvariable=password, show='*')
    # entrada_password.pack()

def add_nota():
    ventana_add_mark.pack()
    # ventana_inicio.forget()

def add_mark():
    email = entrada_email.get()
    exam = entrada_exam.get()
    mark = entrada_mark.get()
    subject_add = subjects.get(ACTIVE)
    mark_manager = MarksManager()
    mark = mark_manager.add_mark(email, subject_add, exam, int(mark))
    messageBox = messagebox.showinfo("Notas", mark )
    if mark == "Mark added successfully":
        ventana_student.pack()
        ventana_add_mark.forget()

    
def buscar_pag():
    ventana_buscar.pack()
    # print(len(subjects))
    # get selected items
    
def buscar():
    email = entrada_email.get()
    password = entrada_password.get()
    l = Login(email, password).login()
    if (l == "User logged in successfully"):
        mark_manager = MarksManager()
        result = mark_manager.get_marks(email)
        resultado_notas = ''
        if len(result) != 0:
            for i in result:
                resultado_notas += i["subject"] + "->" + i["exam"] + ": " + str(i["mark"]) + "\n\n"
            messagebox.showinfo("Notas", resultado_notas)
        else:
            resultado_notas = "No hay notas disponibles"
    else:
        messagebox.showinfo("Error", "No se han introducido los datos correctamente")

# -------------------- PRINCIPAL ----------------------

global ventana_principal
pestas_color = "#2E2E2E"
accept_color = "#6666FF"
ventana_principal = tk.Tk()
global name
global surname
global email
global password
global subjects
global resultado_notas
global exam
global mark
name = StringVar()
surname = StringVar()
email = StringVar()
password = StringVar()
resultado_notas = StringVar()
exam = StringVar()
mark = IntVar()

ventana_principal.geometry("1500x800")
ventana_principal.title("Face2Learn")

global ventana_inicio
ventana_inicio = Frame(ventana_principal)
ventana_inicio.pack()
Label(ventana_inicio, text="Escoge una opción", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(ventana_inicio,text="").pack()
Button(ventana_inicio, text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
Label(ventana_inicio, text="").pack()
Button(ventana_inicio, text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
Label(ventana_inicio, text="").pack()



# -------------------- LOGIN ----------------------

global ventana_login
ventana_login = Frame(ventana_principal)

Label(ventana_login, text="Por favor ingrese los datos a continuación").pack()
Label(ventana_login, text="").pack()
etiqueta_email = Label(ventana_login, text="Email * ")
etiqueta_email.pack()
entrada_email = Entry(ventana_login, textvariable=email)
entrada_email.pack()

etiqueta_password = Label(ventana_login, text="Contraseña * ")
etiqueta_password.pack()
entrada_password = Entry(ventana_login, textvariable=password, show='*')
entrada_password.pack()

Label(ventana_login, text="").pack()
Button(ventana_login, text="Entrar", width=10, height=1, bg=accept_color, command=iniciar_sesion).pack()



# -------------------- REGISTRO ----------------------

global ventana_registro
ventana_registro = Frame(ventana_principal)
ventana_registro.config(width=300, height=250)
subjects = Listbox(ventana_registro, selectmode=MULTIPLE)
lists_subjects = ["Matemáticas", "Física", "Química", "Biología", "Lengua", "Inglés", "Francés", "Alemán", "Historia", "Geografía", "Filosofía", "Economía", "Dibujo Técnico", "Informática", "Educación Física", "Religión"]
for i in lists_subjects:
    subjects.insert(END, i)

Label(ventana_registro, text="Por favor ingrese los datos a continuación").pack()
Label(ventana_registro, text="").pack()
etiqueta_nombre = Label(ventana_registro, text="Nombre * ")
etiqueta_nombre.pack()
entrada_nombre = Entry(ventana_registro, textvariable=name)
entrada_nombre.pack()

etiqueta_apellido = Label(ventana_registro, text="Apellido * ")
etiqueta_apellido.pack()
entrada_apellido = Entry(ventana_registro, textvariable=surname)
entrada_apellido.pack()

etiqueta_email = Label(ventana_registro, text="Email * ")
etiqueta_email.pack()
entrada_email = Entry(ventana_registro, textvariable=email)
entrada_email.pack()

etiqueta_password = Label(ventana_registro, text="Contraseña * ")
etiqueta_password.pack()
entrada_password = Entry(ventana_registro, textvariable=password, show='*')
entrada_password.pack()

etiqueta_subjects = Label(ventana_registro, text="Asignaturas * ")
etiqueta_subjects.pack()
subjects.pack()
# entrada_subjects = Entry(ventana_registro)
# entrada_subjects.pack()

Label(ventana_registro, text="").pack()

Button(ventana_registro, text="Registrarse", height="2", width="20", bg=accept_color, command=registrarse).pack()

# --------------------- STUDENT ----------------------
global ventana_student
ventana_student = Frame(ventana_principal)
ventana_student.config(width=300, height=250)

# studnet_subjects = Listbox(ventana_registro, selectmode=SINGLE)
# lists_subjects = ["Matemáticas", "Física", "Química", "Biología", "Lengua", "Inglés", "Francés", "Alemán", "Historia", "Geografía", "Filosofía", "Economía", "Dibujo Técnico", "Informática", "Educación Física", "Religión"]
# for i in lists_subjects:
#     subjects.insert(END, i)

Label(ventana_student, text="Bienvenido/a").pack()

Label(ventana_student, text="").pack()

Button(ventana_student, text="Buscar", height="2", width="20", bg=accept_color, command=buscar_pag).pack()

Button(ventana_student, text = 'Añadir nota', height="2", width="20", bg=accept_color, command=add_nota).pack()

#--------------------- BUSCAR ----------------------
global ventana_buscar
ventana_buscar = Frame(ventana_principal)
ventana_buscar.config(width=300, height=250)

Label(ventana_buscar, text="Por razones de seguridad vuelva a introducir su email y contraseña").pack()
Label(ventana_buscar, text="").pack()

etiqueta_email = Label(ventana_buscar, text="Email * ")
etiqueta_email.pack()
entrada_email = Entry(ventana_buscar, textvariable=email)
entrada_email.pack()
etiqueta_password = Label(ventana_buscar, text="Contraseña * ")
etiqueta_password.pack()
entrada_password = Entry(ventana_buscar, textvariable=password, show='*')
entrada_password.pack()
Label(ventana_buscar, text="").pack()
Button(ventana_buscar, text = 'Buscar', height="2", width="20", bg=accept_color, command=buscar).pack()



#--------------------- ADD NOTA ----------------------
global ventana_add_mark
ventana_add_mark = Frame(ventana_principal)
ventana_add_mark.config(width=300, height=250)
subjects = Listbox(ventana_add_mark, selectmode=SINGLE)

lists_subjects = ["Matemáticas", "Física", "Química", "Biología", "Lengua", "Inglés", "Francés", "Alemán", "Historia", "Geografía", "Filosofía", "Economía", "Dibujo Técnico", "Informática", "Educación Física", "Religión"]
for i in lists_subjects:
    subjects.insert(END, i)

Label(ventana_add_mark, text="Por favor ingrese los datos a continuación").pack()
Label(ventana_add_mark, text="").pack()

etiqueta_email = Label(ventana_add_mark, text="Email * ")
etiqueta_email.pack()
entrada_email = Entry(ventana_add_mark, textvariable=email)
entrada_email.pack()


etiqueta_subjects = Label(ventana_add_mark, text="Asignaturas * ")
etiqueta_subjects.pack()
subjects.pack()


etiqueta_exam = Label(ventana_add_mark, text="Examen * ")
etiqueta_exam.pack()
entrada_exam = Entry(ventana_add_mark, textvariable=exam)
entrada_exam.pack()

etiqueta_mark = Label(ventana_add_mark, text="Nota * ")
etiqueta_mark.pack()
entrada_mark = Entry(ventana_add_mark, textvariable=mark)
entrada_mark.pack()

Label(ventana_add_mark, text="").pack()

Button(ventana_add_mark, text = 'Añadir', height="2", width="20", bg=accept_color, command=add_mark).pack()



ventana_principal.mainloop()

