import tkinter as tk
from tkinter import ttk

def leerValor():
    print("Obtengo el valor de la entrada")
    print(entrada.get())

def ponerValor():
    print("Pongo el valor de la entrada")
    entrada.delete(0,tk.END)
    entrada.insert(0,"Nuevo valor"))
      
raiz = tk.Tk()

entrada = ttk.Entry(raiz)
entrada.pack(padx=15,pady=15)

boton = ttk.Button(raiz, text="Obtener valor",command=leerValor)
boton.pack(padx=15,pady=15)

boton2 = ttk.Button(raiz, text="Poner valor",command=ponerValor)
boton2.pack(padx=15,pady=15)

raiz.mainloop() 
