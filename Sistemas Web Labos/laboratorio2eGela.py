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

# Paso 1
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

# Paso 2
def accesoCredenciales(uri, cookieSession, logintoken):
    # Solicitud
    usuario = sys.argv[1]
    contrasena = getpass.getpass("Contraseña: ")
    print('\nPaso 2: ' + 'GET ' + uri)

    cabeceras = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookieSession}
    datos = {
        'logintoken': logintoken,
        'username': str(usuario),
        'password': str(contrasena)
    }
    # No imprimo la contrasena por consola por seguridad
    print(cookieSession + "logintoken: " + ", " + logintoken + ", username: " + str(usuario) + ", password: *********")

    # Respuesta
    respuesta = requests.post(url=uri, headers=cabeceras, data=datos, allow_redirects=False)
    print(str(respuesta.status_code) + ' ' + respuesta.reason)
    location = respuesta.headers['Location']
    cookie = respuesta.cookies['MoodleSessionegela']
    print('El servidor devuelve la Cookie MoodleSession ' + str(cookie))
    cookie = 'MoodleSessionegela=' + str(cookie)

    return cookie, location

def iniciarSesion(uri, cookieSession):
    # Solicitud
    print('\nPaso 3: ' + 'GET ' + uri)
    cabeceras = {
        'Cookie': cookieSession
    }

    # Respuesta
    respuesta = requests.get(url=uri, headers=cabeceras, allow_redirects=False)
    print(str(respuesta.status_code) + ' ' + respuesta.reason)
    location = respuesta.headers['Location']
    return location

def paginaCursos(uri, cookieSession):
    # Solicitud
    print('\nPaso 4: ' + 'GET ' + uri)
    cabeceras = {
        'Cookie': cookieSession
    }

    # Respuesta
    respuesta = requests.get(url=uri, headers=cabeceras, allow_redirects=False)
    print(str(respuesta.status_code) + ' ' + respuesta.reason)

    # Ya hemos accedido a la página con los cursos
    # Buscamos el curso Sistemas Web
    soup = BeautifulSoup(respuesta.content, 'html.parser')
    elemento = soup.find(href=True, string="Sistemas Web")

    # Petición
    uri = elemento['href']
    print('\nPaso 5: ' + 'POST ' + uri)
    respuesta = requests.post(url=uri, headers=cabeceras, allow_redirects=False)
    print(str(respuesta.status_code) + ' ' + respuesta.reason)

    soup = BeautifulSoup(respuesta.content, 'html.parser')



def main():
    uri = 'https://egela.ehu.eus/login/index.php'
    cookie, logintoken = establecerConexion(uri)
    cookie, location = accesoCredenciales(uri, cookie, logintoken)
    location = iniciarSesion(location, cookie)
    paginaCursos(location, cookie)




if __name__ == '__main__':
    main()