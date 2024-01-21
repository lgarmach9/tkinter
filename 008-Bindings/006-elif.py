import tkinter as tk

def pulsaTecla(evento):
    print("Has pulsado una tecla")
    print(evento.keysym)
    if(evento.keysym == 'a'):
        print("izquierda")
    elif (evento.keysym == 'd'):
        print("derecha")
    elif (evento.keysym == 'w'):
        print("arriba")
    elif (evento.keysym == 's'):
        print("abajo")
        

raiz = tk.Tk()

lienzo= tk.Canvas(raiz)
lienzo.create_oval(20,20,50,50,outline="red",width=2)
lienzo.pack(padx=50,pady=50)

raiz.bind('<Key>',pulsaTecla)

raiz.mainloop() 
