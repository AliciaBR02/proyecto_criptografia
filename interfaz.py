# from curses.textpad import rectangle
# from tkinter import *
import tkinter as tk
from tkinter import ttk
from registration import Registration
# from tkinter import messagebox
# from tkinter import filedialog
# from tkinter import *
# from tkinter import ttk as tk

# Creamos la ventana
root = tk.Tk()

# Creamos el canvas
canvas = tk.Canvas(root, width=900, height=600)

# Crear interfaz para el canvas
# canvas.pack()

# Crear botones
button = tk.Button(root, text="Boton 1", bg="red", fg="white")

# Crear etiquetas
label = tk.Label(root, text="Etiqueta 1", bg="blue", fg="white")
# Crear cajas de texto
entry = tk.Entry(root, width=50, bg="white", fg="black", borderwidth=5)

# Enlazar botón con clase registro
button.bind("<Button-1>")

# Creamos el rectángulo
rectangulo = canvas.create_rectangle(10, 10, 100, 100, fill="red")

# Creamos el texto
texto = canvas.create_text(60, 60, text="Hola mundo")

# Mostramos el canvas
canvas.pack()

# Mostramos la ventana
root.mainloop()

