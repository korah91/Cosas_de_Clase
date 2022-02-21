'''
OBJETIVO
El cliente IoT desarrollado cumple los requisitos solicitados, pero presenta algunos problemas
ya que el número máximo de canales que se pueden crear en ThingSpeak es limitado y el cliente
crea un nuevo canal cada vez que se ejecuta.
El objetivo es realizar una modificación del cliente IoT para que verifique que no se ha superado
el número máximo de canales. Además, en caso de existir un canal con el mismo nombre del
canal nuevo se seguirá utilizando el este canal para subir datos.
Por último, antes de terminar y borrar los datos del canal se deberán descarga los datos y
guardar en un fichero en formato json.
1.Hecho Verificar que no hay 4 canales ya
2.Hecho Si hay un canal con el mismo nombre del canal nuevo, usar el canal viejo
3. Al pulsar CTRL C se descargan los datos
'''


# Nombre: Joel Moises Garcia Escribano
# Grupo: 2
# api_key de usuario: 8YHHE5BU5VMS2XNV
import json

import psutil
import time
import signal
import sys
import requests



# Gestionar el cierre al pulsar CTRL + C
def handler(sig_num, frame):
    # Gestionar evento
    print("Señal " + str(sig_num))

    # NO SE SI FUNCIONA BIEN
    # Guardamos la informacion
    guardarInformacion(canal, read_key)

    limpiarCanal(canal, user_key)
    # Descomentar la siguiente linea para borrar el canal
    # borrarCanal(canal, user_key)
    sys.exit(0)

def cpu_ram():
    i = 0;
    # Guardo la key para escribir el canal y el canal
    global user_key
    global canal
    global read_key
    read_key = ""

    user_key = "8YHHE5BU5VMS2XNV"

    # Compruebo si ya existe un canal o si no hay espacio para canales
    se_puede = sePuede(user_key, 'Laboratorio 1')

    # Si hay un canal con el mismo nombres
    if isinstance(se_puede, dict):
        # Como ya existe un canal con el mismo nombre, le envio los datos sin crear un nuevo canal
        write_key = se_puede.get('channel_key')
        canal = se_puede['id']
        print("Se ha iniciado la conexion con el canal " + str(canal))
        while True:
            cpu = psutil.cpu_percent(interval=1)
            # Para calcular el porcentaje de ram usado utilizo una función de psutil que devuelve una tupla
            ram = psutil.virtual_memory().percent
            print("Cpu: %" + str(cpu) + "\tRam: %" + str(ram))
            # Envio los datos al thingspeak
            print("Enviando datos...")

            enviarDatos(cpu, ram, canal, write_key)
            signal.signal(signal.SIGINT, handler)
            i += 1
            print("Pulsa CTRL + C para salir. Se han añadido " + str(i) + " entradas.")

            # Espero 15 segundos
            time.sleep(15)
    # Si no hay un canal con el mismo nombre y hay espacio para canales
    if se_puede == True:
        respuesta = crearConexion(user_key)
        write_key = respuesta.get('write_key')
        canal = respuesta.get("canal")
        print("Se ha creado un nuevo canal con id: " + str(canal))
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
    # Si no hay espacio para canales
    if se_puede == False:
        print("No hay espacio para más canales, ejecutar la función borrarTodosLosCanales")

def guardarInformacion(canal, read_key):
    uri = "https://api.thingspeak.com/channels/" + str(canal) + "/feeds.json"
    cuerpo = {'api_key': read_key}
    respuesta = requests.request(method='GET', url=uri, data=cuerpo)
    respuesta = respuesta.json()

    with open("fields.json", "w") as json_file:
        json.dump(respuesta, json_file)
    print("Se ha creado el archivo fields.json")
    return

# Devuelve el request de canales.
def getListaCanales(api_key):
    uri = "https://api.thingspeak.com/channels.json"
    cuerpo = {'api_key': api_key}
    respuesta = requests.request(method='GET', url=uri, data=cuerpo)
    return respuesta

def sePuede(api_key, nombre_canal):
    respuesta = getListaCanales(api_key)
    canales = respuesta.json()

    # Si no hay más espacio para canales devolver False
    if len(canales) == 4:
        return False
    # Si hay espacio comprobar si hay un canal con el mismo nombre devolver su ID
    for canal in canales:
        if canal['name'] == nombre_canal:
            # Guardo la ReadKey para utilizarla al final
            global read_key
            read_key = canal['api_keys'][1]['api_key']
            return {'id': canal['id'], 'channel_key': canal['api_keys'][0]['api_key']}
    # Si hay espacio y no hay ningun canal con el mismo nombre devolver True
    return True

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

def borrarTodosLosCanales(user_key):
    canales = getListaCanales(user_key).json()
    for canal in canales:
        borrarCanal(canal['id'], user_key)

def crearConexion(api_key):
    if not sePuede(api_key, 'Laboratorio 1'):
        pass
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
    #sePuede("8YHHE5BU5VMS2XNV", 'Laboratorio 1')
    cpu_ram()
    #Descomentar la siguiente linea para borrar todos los canales
    #borrarTodosLosCanales('8YHHE5BU5VMS2XNV')
