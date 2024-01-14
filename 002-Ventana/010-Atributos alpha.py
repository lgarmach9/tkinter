import tkinter as tk

raiz = tk.Tk()
raiz.title("Aprendiendo Tkinter")

anchuraventana = 400
alturaventana = 400

anchurapantalla = raiz.winfo_screenwidth()
alturapantalla = raiz.winfo_screenheight()

esquinax = int (anchurapantalla/2 - anchuraventana/2)
esquinay = int (alturapantalla/2 - alturaventana/2)

raiz.geometry(str(anchuraventana)+"x"+str(alturaventana)+"+"+str(esquinax)+"+"+str(esquinay))
raiz.resizable(False,False) #limita la ampliacion de la pantalla

raiz.attributes("-alpha",0.5) #ventana semitransparente

raiz.mainloop() #para que la ventana se ejecute como usuario
