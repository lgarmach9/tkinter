import tkinter as tk

def salir():
    raiz.destroy()

raiz = tk.Tk()

barramenu= tk.Menu(raiz)
raiz.config(menu=barramenu)
archivo= tk.Menu(barramenu,tearoff=0) 
barramenu.add_cascade(label="Archivo",menu=archivo)

archivo.add_command(label="Nuevo")
archivo.add_command(label="Abrir")
archivo.add_command(label="Guardar")
archivo.add_command(label="Salir",command=salir)

editar= tk.Menu(barramenu,tearoff=0) 
barramenu.add_cascade(label="Editar",menu=editar)

editar.add_command(label="Deshacer")
editar.add_command(label="Copiar")
editar.add_command(label="Cortar")
editar.add_command(label="Pegar")

ayuda= tk.Menu(barramenu,tearoff=0) 
barramenu.add_cascade(label="Ayuda",menu=ayuda)

ayuda.add_command(label="Ayuda")
ayuda.add_command(label="Documentación en línea")
ayuda.add_command(label="Acerca de...")
ayuda.add_command(label="Soporte")


raiz.mainloop() 
