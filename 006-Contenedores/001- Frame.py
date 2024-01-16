import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

marco = tk.Frame(raiz, padx=50, pady=50)

tk.Label(marco,text="Hola mundo desde un Frame").pack(padx=10, pady=10)
tk.Button(marco,text="Esto es un boton").pack(padx=10, pady=10)
                  
marco.pack()

raiz.mainloop() 
