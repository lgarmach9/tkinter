import tkinter as tk

raiz = tk.Tk()
frutas = ['manzana', 'pera', 'platano', 'fresa']
listado= tk.Listbox(raiz)

for fruta in frutas:
    listado.insert(tk.END,fruta)
listado.pack(padx=50,pady=50)

raiz.mainloop() 
