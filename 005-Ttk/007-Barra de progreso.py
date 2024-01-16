import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

ttk.Progressbar(raiz, length=200, mode='indeterminate').pack(padx=50,pady=50)


raiz.mainloop() 
