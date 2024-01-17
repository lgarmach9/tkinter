from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "entrada":
        ttk.Entry(raiz).pack(padx=20,pady=20)
    elif tipo== "etiqueta":
        ttk.Label(raiz, text=texto).pack(padx=20,pady=20)
    elif tipo == "boton":
        ttk.Button(raiz, text=texto).pack(padx=20,pady=20)
    elif tipo == "deslizable":
        ttk.Scale(raiz, from_=0, to=100).pack(padx=50,pady=50)
    elif tipo == "seleccion":
        ttk.Radiobutton(raiz, text=texto).pack(padx=50,pady=50)

tk.mainloop()
