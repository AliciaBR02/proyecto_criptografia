from curses.textpad import rectangle
# from tkinter import *
import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
# from tkinter import filedialog
# from tkinter import *
# from tkinter import ttk as tk

# Creamos la ventana
root = tk.Tk()

# Creamos el canvas
canvas = tk.Canvas(root, width=300, height=300)

# Creamos el rectángulo
rectangulo = canvas.create_rectangle(10, 10, 100, 100, fill="red")

# Creamos el texto
texto = canvas.create_text(60, 60, text="Hola mundo")

# Mostramos el canvas
canvas.pack()

# Mostramos la ventana
root.mainloop()

