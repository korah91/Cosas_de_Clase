# Nombre: Joel Moises Garcia Escribano
# Grupo: 2
# api_key de usuario: 8YHHE5BU5VMS2XNV
import psutil
import time
import signal
import sys
import requests

# Gestionar el cierre al pulsar CTRL + C
def handler(sig_num, frame):
    # Gestionar evento
    print("Señal " + str(sig_num))
    limpiarCanal(canal, user_key)
    # Descomentar la siguiente linea para borrar el canal
    # borrarCanal(canal, user_key)
    sys.exit(0)

def cpu_ram():
    i = 0;
    # Guardo la key para escribir el canal y el canal
    global user_key
    global canal
    user_key = "8YHHE5BU5VMS2XNV"
    respuesta = crearConexion(user_key)
    write_key = respuesta.get('write_key')
    canal = respuesta.get("canal")
    while True:
        cpu = psutil.cpu_percent(interval=1)
        # Para calcular el porcentaje de ram usado utilizo una función de psutil que devuelve una tupla
        ram = psutil.virtual_memory().percent
        print("Cpu: %" + str(cpu) + "\tRam: %" + str(ram))
        # Envio los datos al thingspeak
        print("Enviando datos...")

        enviarDatos(cpu, ram, canal, write_key)
        signal.signal(signal.SIGINT, handler)
        i+=1
        print("Pulsa CTRL + C para salir. Se han añadido " + str(i) + " entradas.")

        # Espero 15 segundos
        time.sleep(15)

# Borra todos los datos dentro del canal. Se debe ejecutar tras pulsar CTRL + C
def limpiarCanal(canal, user_key):
    uri = "https://api.thingspeak.com/channels/" + str(canal) + "/feeds.json"
    cuerpo = {'api_key': user_key}
    requests.request(method="DELETE", url=uri, data=cuerpo)
    print("Canal " + str(canal), " limpiado")

# Borra el canal. No se pide pero es necesario para poder seguir creando canales
def borrarCanal(canal, user_key):
    uri = "https://api.thingspeak.com/channels/" + str(canal) + ".html"
    cuerpo = {'api_key': user_key}
    requests.request(method="DELETE", url=uri, data=cuerpo)
    print("Canal " + str(canal), " BORRADO")


def crearConexion(api_key):
    cuerpo = {"api_key": api_key, "field1": '%CPU', "field2": '%RAM', 'name': 'Laboratorio 1', "Content-Type": 'application/x-www-form-urlencoded'}
    response = requests.request(method="POST", data=cuerpo,
                                url="https://api.thingspeak.com/channels.json")
    print("iniciarConexion: " + str(response.status_code))

    response = response.json()

    canal = response['id']
    write_key = str(response['api_keys'][0].get('api_key'))
    return {'write_key': write_key, 'canal': canal}

# Abre la conexión con el primer canal y obtiene su write_key y ID
def iniciarConexion(api_key):
    # Guardo los canales disponibles
    response = requests.request(method="GET",
                                url="https://api.thingspeak.com/channels.json?api_key=" + api_key)
    print("iniciarConexion: " + str(response.status_code))

    response = response.json()

    canal = response[0]['id']
    write_key = str(response[0]['api_keys'][0].get('api_key'))

    # print(response)
    # print(canal)
    return {'write_key': write_key, 'canal': canal}


def enviarDatos(cpu, ram, canal, write_key):
    cpu = str(cpu)
    ram = str(ram)

    uri = "https://api.thingspeak.com/update.json?api_key=" + write_key + "&field1=" + cpu + "&field2=" + ram
    # print(uri)
    # Envio los datos %CPU y %RAM al canal
    response = requests.request(method="POST", url=uri)
    print("enviarDatos: " + str(response.status_code))
    if (response.status_code == 200):
        print("Logrado")


if __name__ == "__main__":
    cpu_ram()
