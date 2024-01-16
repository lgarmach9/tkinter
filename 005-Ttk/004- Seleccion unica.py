import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

ttk.Radiobutton(raiz, text="Esta es una opcion 1").pack(padx=50,pady=50)
ttk.Radiobutton(raiz, text="Esta es una opcion 2").pack(padx=50,pady=50)

raiz.mainloop() 
