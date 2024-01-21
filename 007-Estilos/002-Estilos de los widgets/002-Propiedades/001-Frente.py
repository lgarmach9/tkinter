import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

estilo = ttk.Style()
estilo.configure('TButton',foreground = 'red')

ttk.Button(raiz, text="Pulsame si te atreves").pack(padx=25,pady=25)

raiz.mainloop()
