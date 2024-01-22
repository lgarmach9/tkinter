import tkinter as tk
from tkinter import ttk

def seleccionaElemento (event):
    seleccionado = arbol.focus()
    print(seleccionado)
    valores = arbol.item(seleccionado,'values')
    print(valores)

def ponerValor():
    print("Pongo el valor de la entrada")  
    arbol.insert('','0', text="Cliente", values=(entradanom.get(), entradaape.get(), entradaemail.get()))
        
raiz = tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton', foreground = 'green', background = 'black', borderwidth=5, relief='raised')
estilo.configure('TLabel', font= ("Verdana", 16))
estilo.configure('TEntry', selectbackground="#87F6F9",selectforeground='red')

ttk.Label(raiz, text="Pon el nombre").pack(padx=15,pady=15)

entradanom= ttk.Entry(raiz)
entradanom.pack(padx=15,pady=15)

ttk.Label(raiz, text="Pon el apellido").pack(padx=15,pady=15)

entradaape= ttk.Entry(raiz)
entradaape.pack(padx=15,pady=15)

ttk.Label(raiz, text="Pon el email").pack(padx=15,pady=15)

entradaemail= ttk.Entry(raiz)
entradaemail.pack(padx=15,pady=15)

boton2 = ttk.Button(raiz, text="Añadir a agenda",command=ponerValor)
boton2.pack(padx=15,pady=15)

arbol= ttk.Treeview(raiz,columns=('nombre','apellidos','email'))
arbol.heading("#0", text="Identificador") 
arbol.heading("nombre", text="Nombre") 
arbol.heading("apellidos", text="Apellidos")
arbol.heading("email", text="Corrreo electrónico")

arbol.pack(padx=50,pady=50)

arbol.bind('<<TreeviewSelect>>',seleccionaElemento)
   
raiz.mainloop() 
