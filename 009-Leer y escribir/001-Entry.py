import tkinter as tk
from tkinter import ttk

def leerValor():
    print("Obtengo el valor de la entrada")
      
raiz = tk.Tk()

entrada = ttk.Entry(raiz)
entrada.pack(padx=15,pady=15)

boton = ttk.Button(raiz, text="Obtener valor",command=leerValor)
boton.pack(padx=15,pady=15)

raiz.mainloop() 
