import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

etiqueta1 = tk.Label(raiz,text="Etiqueta 1")
etiqueta2 = tk.Label(raiz,text="Etiqueta 2")
etiqueta3 = tk.Label(raiz,text="Etiqueta 3")
etiqueta4 = tk.Label(raiz,text="Etiqueta 4")

etiqueta1.pack(padx=10,pady=10) #si lo empaqueto asi se queda en vertical
etiqueta2.pack(padx=10,pady=10)
etiqueta3.pack(padx=10,pady=10)
etiqueta4.pack(padx=10,pady=10)

raiz.mainloop() 
