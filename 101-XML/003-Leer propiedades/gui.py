from bs4 import BeautifulSoup

archivo = open("interfaz.xml","r")
contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")
for campo in xml.find_all("campo"):
    print(campo)
    tipo = campo.get("tipo")
    print(tipo)
