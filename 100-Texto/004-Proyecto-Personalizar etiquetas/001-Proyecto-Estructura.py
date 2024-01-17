import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")

lineas= archivo.readlines()
for linea in lineas:
    contenido = linea.strip().split(",")
    elemento = contenido[0]
    if elemento == "entrada":
        tk.Entry(raiz).pack(padx=20,pady=20)
    elif elemento== "etiqueta":
        tk.Label(raiz, text=contenido[1]).pack(padx=20,pady=20)
    elif elemento == "boton":
        tk.Button(raiz, text=contenido[1]).pack(padx=20,pady=20)


raiz.mainloop()
