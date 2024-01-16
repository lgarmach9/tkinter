import tkinter as tk

raiz = tk.Tk()

def saluda():
    print("Has pulsado el botón")

tk.Button(raiz,text="Hola mundo desde Tkinter",command=saluda).pack(padx=50,pady=50)


raiz.mainloop() 
