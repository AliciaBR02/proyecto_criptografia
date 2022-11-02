# from curses.textpad import rectangle
from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
# from registration import Registration
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


def ventana_inicio():
    global ventana_principal
    global ventana_login
    global ventana_registro
    
    pestas_color = "#2E2E2E"
    ventana_principal = tk.Tk()
    ventana_principal.geometry("900x600")
    ventana_principal.title("Face2Learn")
    ventana_registro = Frame(ventana_principal)
    ventana_registro.pack()
    ventana_login = Frame(ventana_principal)
    ventana_login.pack()
    Label(text="Escoge una opción", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
    Label(text="").pack()
    ventana_principal.mainloop()

# def cambiar_ventana():
    #framealquevoy.pack()
    #framedelquevengo.forget
    
def registro():
    if ventana_login:
        ventana_login.forget()
    ventana_registro.config(width=300, height=250)

    
    global name
    global surname
    global email
    global password
    global subjects
    name = StringVar()
    surname = StringVar()
    email = StringVar()
    password = StringVar()
    #subjects es una lista en tkinter
    # subjects = Listbox(ventana_registro, selectmode=MULTIPLE)
    
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
    
    # etiqueta_subjects = Label(ventana_registro, text="Asignaturas * ")
    # etiqueta_subjects.pack()
    # entrada_subjects = Entry(ventana_registro, textvariable=subjects)
    # entrada_subjects.pack()
    
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="blue", command=registro).pack()

def login():
    if ventana_registro:
        ventana_registro.forget()
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


v = ventana_inicio()