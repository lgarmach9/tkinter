import tkinter as tk

def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

def enviar():
    print("Enviado")


raiz = tk.Tk()
raiz.title("Cuestionario desayuno")
anchuraventana = 500
alturaventana = 500

anchurapantalla = raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()

esquinax = int (anchurapantalla/2 - anchuraventana/2)
esquinay = int (alturapantalla/2 - alturaventana/2)

raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))
raiz.iconbitmap("fruta.ico")

tk.Label(raiz,text="¿Desayunas?").pack()
raiz.config(bd=15)
tk.Radiobutton(raiz,text="Si", value=1, command=selec).pack()
tk.Radiobutton(raiz,text="No", value=2, command=selec).pack()

tk.Label(raiz,text="¿Qué tomas?").pack()
tk.Checkbutton(raiz, text="Cafe", onvalue=1, offvalue=0).pack()
tk.Checkbutton(raiz, text="Té",onvalue=1, offvalue=0).pack()

tk.Label(raiz,text="Más detalles:").pack()
tk.Entry(raiz).pack()

tk.Button(raiz,text="Enviar",command=enviar).pack()

raiz.mainloop() 
