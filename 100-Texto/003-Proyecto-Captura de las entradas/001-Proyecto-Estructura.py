import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")

lineas= archivo.readlines()
for linea in lineas:
    elemento = linea.strip()
    if elemento == "entrada":
        tk.Entry(raiz).pack()
    elif elemento== "etiqueta":
        tk.Label(raiz, text="Etiqueta").pack()
    elif elemento == "boton":
        tk.Button(raiz, text="Esto es un boton").pack()
#modificando el archivo de texto no hace falta tocar el codigo

raiz.mainloop()
