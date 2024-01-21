import tkinter as tk
from tkinter import ttk

def cambiaestilo():
    print("Cambio el estilo")
    estilo.theme_use(desplegable.get());

raiz = tk.Tk()

estilo = ttk.Style()
print(estilo.theme_names())

desplegable = ttk.Combobox(raiz,values= estilo.theme_names())
desplegable.pack(padx=25,pady=25)

botoncambiar = ttk.Button(raiz,text="Aplica el estilo", command=cambiaestilo)
botoncambiar.pack(padx=25,pady=25)

tk.Button(raiz,text="Esto es un botón tk").pack(padx=25,pady=25)
ttk.Button(raiz,text="Esto es un botón ttk").pack(padx=25,pady=25)

raiz.mainloop()
