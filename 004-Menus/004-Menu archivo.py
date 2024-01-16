import tkinter as tk

raiz = tk.Tk()

barramenu= tk.Menu(raiz)
raiz.config(menu=barramenu)
archivo= tk.Menu(barramenu,tearoff=0)
barramenu.add_cascade(label="Archivo",menu=archivo)

raiz.mainloop() 
