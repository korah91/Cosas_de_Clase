#-- coding: utf-8 --
import urllib.parse
import requests
import webbrowser
from socket import AF_INET, socket, SOCK_STREAM
import json


auth_code = ""
print("###################################")
print("OAuth 2.0 for Mobile & Desktop Apps")
print("###################################")
# https://developers.google.com/identity/protocols/oauth2/native-app

print("\nStep 1.- Prerequisites on Google Cloud Console")
print("\tEnable APIs for your project")
print("\tIdentify access scopes")
print("\tCreate authorization credentials")
print("\tConfigure OAuth consent screen")
print("\tAdd access scopes and test users")

client_id = "775255834665-43puhgah4obrm6dno8cao3lkjtcjhg8r.apps.googleusercontent.com"
client_secret = "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"
scope = "https://www.googleapis.com/auth/drive.readonly"

redirect_uri = "http://127.0.0.1:8090"

print("\nStep 2.- Send a request to Google's OAuth 2.0 server")
uri = "https://accounts.google.com/o/oauth2/v2/auth"
datos = { 'client_id': client_id,
          'redirect_uri': redirect_uri,
          'response_type': 'code',
          'scope': scope}
datos_encoded = urllib.parse.urlencode(datos)

print("\tOpenning browser...")
webbrowser.open_new ((uri +'?' + datos_encoded))

print("\nStep 3.- Google prompts user for consent")

print("\nStep 4.- Handle the OAuth 2.0 server response")

# Crear servidor local que escucha por el puerto 8090

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localHost', 8090))
server_socket.listen(1)
print("\tLocal server listening on port 8090")

# Recibir la solicitude 302 del navegador
client_connection, client_address = server_socket.accept()
peticion = client_connection.recv(1024)
print("\tRequest from the browser received at local server:")
#print ("\t" + str(peticion))

# Buscar en la petición el "auth_code"
primera_linea = peticion.decode('UTF8').split('\n')[0]
aux_auth_code = primera_linea.split(' ')[1]
auth_code = aux_auth_code[7:].split('&')[0]
print ("\tauth_code: " + auth_code)

# Devolver una respuesta al usuario
http_response = "HTTP/1.1 200 OK\r\n\r\n" \
                "<html>" \
                "<head><title>Prueba</title></head>" \
                "<body>The authentication flow has completed. Close this window.</body>" \
                "</html>"
client_connection.sendall(http_response.encode(encoding="utf-8"))
client_connection.close()
server_socket.close()

print("\nStep 5.- Exchange authorization code for refresh and access tokens")
# https://developers.google.com/identity/protocols/oauth2/native-app#exchange-authorization-code
'''
POST /token HTTP/1.1
*Host: oauth2.googleapis.com
*Content-Type: application/x-www-form-urlencoded

code=4/P7q7W91a-oMsCeLvIaQm6bTrgtp7&
*client_id=client_id&
*client_secret=client_secret&
*redirect_uri="urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob%3Aauto"&
grant_type=authorization_code
'''

metodo = 'POST'
uri= "https://oauth2.googleapis.com/token"
cabeceras= {'Host':'oauth2.googleapis.com', 'Content-Type': 'application/x-www-form-urlencoded'}
cuerpo={
    'code': auth_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri' : redirect_uri,
    'grant_type' : "authorization_code"
}
cabeceras['Content-Length'] = str(len(urllib.parse.urlencode(cuerpo)))
respuesta = requests.request(metodo, uri, data=cuerpo,headers=cabeceras, allow_redirects=False)

#Conseguir el code en formato JSON
jsonn=json.loads(respuesta.text)

access_token=jsonn["access_token"]
print(respuesta.text)
print(access_token)

print("\nStep 6.- Calling Google APIs")
# Documentación de Google Calendar API

metodo = 'GET'
uri= "https://www.googleapis.com/drive/v3/files"
cabeceras= {'Host':'www.googleapis.com', 'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Bearer '+access_token}
respuesta = requests.request(metodo, uri,headers=cabeceras, allow_redirects=False)

print(json.loads(respuesta.text))

#Conseguir Lista Calendarios
#Conseguir Lista Eventos