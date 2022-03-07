'''
Un programa que descargue todos los pdfs
3.‐ Programar en Python, utilizando la librería requests, una sesión HTTP con el servidor
de eGela.
4.‐ Localizar los PDF que aparecen en la página principal de eGela de esta asignatura en
la estructura del HTML utilizando el bookmarklet “Visual Source Chart”.
5.‐ Realizar el cliente Python que descarga los PDF.
'''

import getpass
import sys
import requests
from bs4 import BeautifulSoup

def establecerConexion(uri):
    # Solicitud
    print('Paso 1: ' + 'GET ' + uri)

    # Respuesta
    respuesta = requests.get(url=uri)
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    #print(soup.prettify())
    print(str(respuesta.status_code) + ' ' + respuesta.reason)
    cookie = respuesta.cookies['MoodleSessionegela']
    logintoken = soup.find(attrs={'name': 'logintoken'}).get('value')
    print('El servidor devuelve la Cookie MoodleSession ' + str(cookie) + ' y el logintoken ' + str(logintoken))
    cookie = 'MoodleSessionegela=' + str(cookie)
    logintoken = str(logintoken)
    return cookie, logintoken

#establecerConexion está perfecto!!
def accesoCredenciales(uri, cookieSession, logintoken):
    # Solicitud
    usuario = sys.argv[1]
    contrasena = getpass.getpass("Contraseña: ")

    cabeceras = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookieSession}
    datos = {
        'logintoken': logintoken,
        'username': str(usuario),
        'password': str(contrasena)
    }

    # Respuesta
    respuesta = requests.post(url=uri, headers=cabeceras, data=datos, allow_redirects=False)
    print(str(respuesta.status_code) + ' ' + respuesta.reason)
    location = respuesta.headers['Location']
    cookie = respuesta.cookies['MoodleSessionegela']
    print('El servidor devuelve la Cookie MoodleSession ' + str(cookie))
    cookie = 'MoodleSessionegela=' + str(cookie)

    print(location)

def


def main():
    uri = 'https://egela.ehu.eus/login/index.php'
    cookie, logintoken = establecerConexion(uri)
    accesoCredenciales(uri, cookie, logintoken)




if __name__ == '__main__':
    main()