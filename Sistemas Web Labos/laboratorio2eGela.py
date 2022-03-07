'''
Un programa que descargue todos los pdfs
3.‐ Programar en Python, utilizando la librería requests, una sesión HTTP con el servidor
de eGela.
4.‐ Localizar los PDF que aparecen en la página principal de eGela de esta asignatura en
la estructura del HTML utilizando el bookmarklet “Visual Source Chart”.
5.‐ Realizar el cliente Python que descarga los PDF.
'''
import urllib.parse

import requests
from bs4 import BeautifulSoup

def establecerConexion():
    # Solicitud
    uri = 'https://egela.ehu.eus/login/index.php'
    print('Paso 1: ' + 'GET ' + uri)

    # Respuesta
    respuesta = requests.get(url=uri)
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    #print(soup.prettify())
    print(str(respuesta.status_code) + ' ' + respuesta.reason)
    cookie = respuesta.cookies['MoodleSessionegela']
    logintoken = soup.find(attrs={'name': 'logintoken'}).get('value')
    print('El servidor devuelve la Cookie MoodleSession ' + str(cookie) + ' y el logintoken ' + str(logintoken))


#establecerConexion está perfecto!!
def accesoCredenciales():
    pass




def main():
    establecerConexion()




if __name__ == '__main__':
    main()