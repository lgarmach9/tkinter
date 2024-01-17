from bs4 import BeautifulSoup
import tkinter as tk

raiz = tk.Tk()

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for campo in xml.find_all("campo"):
    tipo = campo.get("tipo")
    texto = campo.get("texto")
    if tipo == "entrada":
        tk.Entry(raiz).pack(padx=20,pady=20)
    elif tipo== "etiqueta":
        tk.Label(raiz, text=texto).pack(padx=20,pady=20)
    elif tipo == "boton":
        tk.Button(raiz, text=texto).pack(padx=20,pady=20)

tk.mainloop()
