# -*- coding: utf-8 -*-
import requests
import urllib
import sys


def registerUser():
    if len(sys.argv) == 5:
        metodo = 'POST'
        uri = "http://localhost:8080/ShareInfo/servlet/TestServlet"
        cabeceras = {'Host': 'egela.ehu.eus',
                     'Content-Type': 'application/x-www-form-urlencoded', }
        data = {'type': sys.argv[1],
                'email': sys.argv[2],
                'password': sys.argv[3],
                'username': sys.argv[4], }
        data_encoded = urllib.urlencode(data)
        cabeceras['Content-Length'] = str(len(data_encoded))
        respuesta = requests.request(metodo, uri, headers=cabeceras, data=data_encoded, allow_redirects=False)
        print(metodo + " " + uri)
        codigo = respuesta.status_code
        descripcion = respuesta.reason
        print(str(codigo) + " " + descripcion)

        for cabecera in respuesta.headers:
            print(cabecera + ": " + respuesta.headers[cabecera])
        contenido = respuesta.content
        return ("CONTENIDO: " + contenido)
    else:
        return "Parámetros incorrectos: type, email, password, username".decode("utf-8")


def getUsername():
    return (getUsername)


def registerMessage():
    return (registerMessage)


def getMessages():
    return (getMessages)


def typo(argument):
    switcher = {
        "registerUser": registerUser,
        "getUsername": getUsername,
        "registerMessage": registerMessage,
        "getMessages": getMessages,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Tipo NO válido".decode("utf-8"))
    # Execute the function
    print(func())


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Faltan los parámetros:")
        print("  - registerUser: type, email, password, username")
        print("  - getUsername: type, email, password")
        print("  - registerMessage: type, username, message")
        print("  - getMessages: type, format")
    else:
        argument = sys.argv[1];
        typo(argument)
