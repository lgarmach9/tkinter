import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

arbol= ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0", text="Identificador") #en la columna 1el texto va a ser identificador
arbol.heading("nombre", text="Nombre") #la columna nombre se va a llamar nombre
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Corrreo electrónico")
                    
arbol.pack()
raiz.mainloop() 
