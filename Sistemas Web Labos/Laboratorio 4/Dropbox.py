from wsgiref import headers
import requests
import urllib
import webbrowser
from socket import AF_INET, socket, SOCK_STREAM
import json
import helper

app_key = 'xz7g070lqoalgek'
app_secret = 'vq0bndl6310xa1z'
server_addr = "localhost"
server_port = 8090
redirect_uri = "http://" + server_addr + ":" + str(server_port)

class Dropbox:
    _access_token = ""
    _path = "/"
    _files = []
    _root = None
    _msg_listbox = None

    def __init__(self, root):
        self._root = root


    def local_server(self):
        # 8090. portuan entzuten dagoen zerbitzaria sortu
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((server_addr, server_port))
        server_socket.listen(1)
        print("\tLocal server listening on port " + str(server_port))

        # nabitzailetik 302 eskaera jaso
        client_connection, client_address = server_socket.accept()
        eskaera = client_connection.recv(1024)
        print("\tRequest from the browser received at local server:")
        print (eskaera)

        # eskaeran "auth_code"-a bilatu
        lehenengo_lerroa = eskaera.decode('UTF8').split('\n')[0]
        aux_auth_code = lehenengo_lerroa.split(' ')[1]
        auth_code = aux_auth_code[7:].split('&')[0]
        print ("\tauth_code: " + auth_code)

        # erabiltzaileari erantzun bat bueltatu
        http_response = "HTTP/1.1 200 OK\r\n\r\n" \
                        "<html>" \
                        "<head><title>Proba</title></head>" \
                        "<body>The authentication flow has completed. Close this window.</body>" \
                        "</html>"
        client_connection.sendall(http_response.encode(encoding="utf-8"))
        client_connection.close()
        server_socket.close()

        return auth_code

    def do_oauth(self):
        # https://www.dropbox.com/oauth2/authorize?client_id=<APP_KEY>
        # &response_type=code&code_challenge=<CHALLENGE>&code_challenge_method=<METHOD>
        uri = 'https://www.dropbox.com/oauth2/authorize'
        datos = { 
            'client_id': app_key,
            'redirect_uri': redirect_uri,
            'response_type': 'code',
            }
        datos_encoded = urllib.parse.urlencode(datos)

        print("\tOpenning browser...")
        webbrowser.open_new ((uri +'?' + datos_encoded))

        # Recogemos el codigo para autentificarnos
        codigo_auth = self.local_server()
        # Ya tenemos el codigo_auth. Nos conectamos a la api
        url = "https://api.dropboxapi.com/oauth2/token"

        cabecera = {
            'Host': 'api.dropboxapi.com',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        datos = {
            'code': codigo_auth,
            'client_id': app_key,
            'client_secret': app_secret,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code'
        }

        r = requests.post(url=url, data=datos, headers=cabecera, allow_redirects=False)
        print("Conexión a /oauth2/token: " + str(r.status_code))

        # Recibo el token que necesito
        jason = json.loads(r.text)
        token = jason['access_token']
        print('access_token: ' + token)

        # Lo guardo
        self._access_token = token
        
        self._root.destroy()

    def list_folder(self, msg_listbox):
        print("/list_folder")
        uri = 'https://api.dropboxapi.com/2/files/list_folder'
        # https://www.dropbox.com/developers/documentation/http/documentation#files-list_folder

        #Creo las cabeceras
        headers = {
            "Authorization": "Bearer " + self._access_token,
            "Content-Type": "application/json"
        }

        # borro el / del path porque la nueva api no lo necesita y me da error
        if self._path == "/":
            self._path = ""
        
        data = {
            "path": self._path
        }

        r = requests.post(uri, headers=headers, data=json.dumps(data), allow_redirects=False)
        print("Conexión a /list_folder: " + str(r.status_code))
        print(r.text)
        contenido_json=json.loads(r.text)

        self._files = helper.update_listbox2(msg_listbox, self._path, contenido_json)

    def transfer_file(self, file_path, file_data):
        print("/upload")
        uri = 'https://content.dropboxapi.com/2/files/upload'
        # https://www.dropbox.com/developers/documentation/http/documentation#files-upload

        argDropbox = {
                "path":file_path,
                "mode": "add",
                "autorename":True
        }
        headers = {
            "Authorization": "Bearer " + self._access_token,
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": json.dumps(argDropbox)
        }
        # En la documentacion pone que deberia poner: Dropbox-API-Arg: {"path":"file_path","mode":{".tag":"add"},"autorename":true}

        r = requests.post(uri, headers=headers, allow_redirects=False)
        
        print("Conexión a /upload: " + str(r.status_code))
        print(r.text)

    def delete_file(self, file_path):
        print("/delete_file")
        uri = 'https://api.dropboxapi.com/2/files/delete_v2'
        # https://www.dropbox.com/developers/documentation/http/documentation#files-delete
       
        headers = {
            "Authorization": "Bearer " + self._access_token,
            "Content-Type": "application/json"
        }

        data = {
            "path": file_path
        }

        r = requests.post(uri, headers=headers, data=json.dumps(data))
        print("Conexión a /delete: " + str(r.status_code))

    def create_folder(self, path):
        print("/create_folder")
       # https://www.dropbox.com/developers/documentation/http/documentation#files-create_folder
        url = 'https://api.dropboxapi.com/2/files/create_folder_v2'
        headers = {
            "Authorization": "Bearer " + self._access_token,
            "Content-Type": "application/json"
        }

        data = {
            "path": path
        }

        r = requests.post(url, headers=headers, data=json.dumps(data), allow_redirects=False)
        print("Conexión a /create_folder: " + str(r.status_code))

#Esta es la nueva funcionalidad que hemos implementado: devuelve el numero de ficheros totales del usuario
    def contar_ficheros(self):

        print("/count")
        
        url = 'https://api.dropboxapi.com/2/file_requests/count'
        headers = {
            "Authorization": "Bearer " + self._access_token,
            "Content-Type": "application/json",
        }

        data = None

        r = requests.post(url, headers=headers, data = json.dumps(data), allow_redirects=False)
        print("Conexión a /count: " + str(r.status_code))

  