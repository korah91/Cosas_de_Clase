import requests
from bs4 import BeautifulSoup
import urllib

def enviarNombre(nombre):
    nombre = str(nombre)
    cabeceras = {'Content-Type': 'application/x-www-form-urlencoded'}
    datos = {'bidali': 'BUSCAR', 'abi_ize': nombre}
    datos = urllib.parse.urlencode(datos)
    request = requests.post("https://www.ehu.eus/bilatu/buscar/sbilatu.php?lang=es1", data = datos, headers= cabeceras)

    codigo = request.status_code
    descripcion = request.reason

    html = BeautifulSoup(request.content, 'html.parser')
    i=0
    for link in html.findAll(attrs={'class': 'fondo_listado'}):
        nombre = link.getText()
        enlace = "https://ehu.eus" + link.find('a')['href']

        print(str(i) + " " + str(nombre) + " " + str(enlace))
        i += 1

if __name__ == '__main__':
    enviarNombre(input("Introduce el nombre a buscar: "))