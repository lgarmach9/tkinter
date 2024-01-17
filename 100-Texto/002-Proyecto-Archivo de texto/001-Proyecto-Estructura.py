import tkinter as tk

raiz = tk.Tk()

archivo = open("estructura.txt","r")
#una opcion para leer el archivo de texto
#for linea in archivo:
#    print(linea)

lineas= archivo.readlines()
for linea in lineas:
    print(linea.strip()) #el strip quita la doble linea


raiz.mainloop()
