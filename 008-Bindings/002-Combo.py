import tkinter as tk
from tkinter import ttk

def saluda(evento):
    print(evento)
    print("Has cambiado el selector")
    print("Y la opción selecionada es: ")
    print(desplegable.get())

raiz = tk.Tk()

desplegable = ttk.Combobox(raiz, values=['uno','dos','tres','cuatro'])
desplegable.pack(padx=25,pady=25)

desplegable.bind('<<ComboboxSelected>>',saluda)

raiz.mainloop()
