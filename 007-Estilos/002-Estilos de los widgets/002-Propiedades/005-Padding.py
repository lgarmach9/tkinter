import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()

estilo = ttk.Style()
estilo.configure('TLabel',foreground = '#1773be', padding=30)

ttk.Label(raiz, text="Pulsame si te atreves").pack(padx=25,pady=25)

raiz.mainloop()
