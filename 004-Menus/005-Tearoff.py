import tkinter as tk

raiz = tk.Tk()

barramenu= tk.Menu(raiz)
raiz.config(menu=barramenu)
archivo= tk.Menu(barramenu,tearoff=1) #con tearoff 1 se puede sacar archivo como una barra de tareas independiente
barramenu.add_cascade(label="Archivo",menu=archivo)

raiz.mainloop() 
