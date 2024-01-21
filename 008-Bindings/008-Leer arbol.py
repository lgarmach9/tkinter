import tkinter as tk
from tkinter import ttk

def seleccionaElemento (event):
    seleccionado = arbol.focus()
    print(seleccionado)
    valores = arbol.item(seleccionado,'values')
    print(valores)

raiz = tk.Tk()

arbol= ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0", text="Identificador") #en la columna 1el texto va a ser identificador
arbol.heading("nombre", text="Nombre") #la columna nombre se va a llamar nombre
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Corrreo electrónico")

arbol.insert('','0','elemento1', text="Cliente 1", values=("Juan", "Garcia Lopez", "juan@gmail.com"))
arbol.insert('','0','elemento2', text="Cliente 2", values=("Elena", "Perez", "elena@gmail.com"))
                   
arbol.pack(padx=50,pady=50)

arbol.bind('<<TreeviewSelect>>',seleccionaElemento)
    
raiz.mainloop() 
