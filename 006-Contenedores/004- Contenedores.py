import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

etiqueta1 = tk.Label(raiz,text="Etiqueta 1")
etiqueta2 = tk.Label(raiz,text="Etiqueta 2")
etiqueta3 = tk.Label(raiz,text="Etiqueta 3")
etiqueta4 = tk.Label(raiz,text="Etiqueta 4")

etiqueta1.grid(row=0, column=0,padx=10,pady=10) #se etiquetan como celdas
etiqueta2.grid(row=0, column=1,padx=10,pady=10)
etiqueta3.grid(row=1, column=0,padx=10,pady=10)
etiqueta4.grid(row=1, column=1,padx=10,pady=10)

raiz.mainloop() 
