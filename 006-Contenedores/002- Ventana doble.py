import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

marco = tk.Frame(raiz, padx=50, pady=50)

ventanapartida= tk.PanedWindow(raiz, orient=tk.HORIZONTAL)
marco1= tk.Frame(ventanapartida, background="red")
marco2= tk.Frame(ventanapartida, background="blue")
                  
ventanapartida.add(marco1)
ventanapartida.add(marco2)

ventanapartida.pack(fill=tk.BOTH,expand=True)

raiz.mainloop() 
