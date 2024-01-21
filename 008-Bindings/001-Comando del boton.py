import tkinter as tk
from tkinter import ttk

def saluda():
    print("Has hecho click en el boton")

raiz = tk.Tk()

ttk.Button(raiz, text="Pulsame si te atreves", command=saluda).pack(padx=25,pady=25)

raiz.mainloop()
