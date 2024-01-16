import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

ttk.Spinbox(raiz, from_=0, to=100).pack(padx=50,pady=50)


raiz.mainloop() 
