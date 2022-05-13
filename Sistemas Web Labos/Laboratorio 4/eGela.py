# -*- coding: UTF-8 -*-
from cgitb import text
from tkinter import messagebox
from urllib.request import Request
import requests
import urllib
from bs4 import BeautifulSoup
import time
import helper

class eGela:
    _login = 0
    _cookie = ""
    _refs = []
    _root = None
#prueba
    def __init__(self, root):
        self._root = root

    def check_credentials(self, username, password, event=None):
        popup, progress_var, progress_bar = helper.progress("check_credentials", "Logging into eGela...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()
		
        print("##### 1. PETICION #####")
        
        uri='https://egela.ehu.eus/login/index.php'
        print("Paso 1")

        respuesta = requests.get(url=uri)
        soup = BeautifulSoup(respuesta.content, 'html.parser')

        print(str(respuesta.status_code) + ' ' + respuesta.reason)
        cookie = respuesta.cookies['MoodleSessionegela']
        logintoken = soup.find(attrs={'name': 'logintoken'}).get('value')
        logintoken = str(logintoken)
        cookie = 'MoodleSessionegela=' + str(cookie)
        print("Cookie: "+str(cookie))

        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################
        progress = 25
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)


        print("##### 2. PETICION #####")
       
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 50
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)
        
        cabeceras = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookie}
        datos = {
            'logintoken': logintoken,
            'username': username.get(),
            'password': password.get()
        }
        # Respuesta
        print("Paso 2")
        # No imprimo la contrasena por consola por seguridad
        print("Cookie: " + cookie + " Logintoken: " +logintoken)

        respuesta = requests.post(url=uri, headers=cabeceras, data=datos, allow_redirects=False)
        print(str(respuesta.status_code) + ' ' + respuesta.reason + " " + str(respuesta.headers['Location']))
        uri = respuesta.headers['Location']
        
        # Si no hay una cookie MoodleSessionegela no son correctas la contrasena y usuario
        if (len(respuesta.cookies)):
            self._login = 1
            cookie = 'MoodleSessionegela=' + str(respuesta.cookies['MoodleSessionegela'])
            print("Es correcto")
        else:
            print("No es correcto")

        print("\n##### 3. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 75
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)


        cabeceras = {
        'Cookie': cookie
        }

        # Respuesta
        print("Paso 3")
        print(cookie)
        print(uri)
        respuesta = requests.get(url=uri, headers=cabeceras, allow_redirects=False)
        print(str(respuesta.status_code) + ' ' + respuesta.reason)
        #uri = respuesta.headers['Location']


        print("\n##### 4. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        # Guardo la ultima cookie
        self._cookie = cookie

        progress = 100
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)
        popup.destroy()

        if (self._login == 1):
            self._root.destroy()
        else:
            messagebox.showinfo("Alert Message", "Login incorrect!")



    def get_pdf_refs(self):
        popup, progress_var, progress_bar = helper.progress("get_pdf_refs", "Downloading PDF list...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()

        print("\n##### 4. PETICION (Página principal de la asignatura en eGela) #####")

        cabeceras = {
        'Cookie': self._cookie
        }
        
        uri='https://egela.ehu.eus/'
        # Respuesta
        respuesta = requests.get(url=uri, headers=cabeceras, allow_redirects=False)
        print(str(respuesta.status_code) + ' ' + respuesta.reason)

        # Ya hemos accedido a la página con los cursos
        # Buscamos el curso Sistemas Web
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        f = open('pagina.html', 'w')
        f.write(str(respuesta.content))

        elemento = soup.find(href=True, string="Sistemas Web")

        # Petición
        uri = elemento['href']
        print('\nPaso 5: ' + 'POST ' + uri)
        respuesta = requests.post(url=uri, headers=cabeceras, allow_redirects=False)
        print(str(respuesta.status_code) + ' ' + respuesta.reason)

        print("\n##### Analisis del HTML... #####")
        #############################################
        # ANALISIS DE LA PAGINA DEL AULA EN EGELA
        # PARA BUSCAR PDFs
        #############################################
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        imagenes = soup.find_all(lambda x: str(x.get('src')).__contains__('/pdf'))       

        numPDFs = len(imagenes)
        # INICIALIZA Y ACTUALIZAR BARRA DE PROGRESO
        # POR CADA PDF ANIADIDO EN self._refs
        progress_step = float(100.0 / numPDFs)




        for imagen in imagenes:
            # links es un diccionario tal que {nombreDelPDF: urlDescarga}
            links = {}
            padre = imagen.parent
            link = padre['href']
            texto = list(padre.strings)[0]
            # Quitamos los / de algunos ficheros, ya que dan problemas al guardarlos
            texto = texto.replace("/", " ")
            
            # {pdf_name: nombrePDF, pdf_link: linkPDF}
            links['pdf_name'] = texto
            links['pdf_link'] = link
            print(links)
            # Anado el diccionario a _refs 
            self._refs.append(links)
            
            progress += progress_step
            progress_var.set(progress)
            progress_bar.update()
            time.sleep(0.1)
            #print("pdf: " + texto + " | " + link)

        # Ya esta listo _refs
        popup.destroy()
        return self._refs

    def get_pdf(self, selection):

        print("\t##### descargando  PDF... #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        cabeceras = {
        'Cookie': self._cookie
        }
        pdf_name = self._refs[selection]['pdf_name']
        pdf_link = self._refs[selection]['pdf_link']

        print("------------------------Descargando el pdf: ", selection, "------------------------")
        respuesta = requests.get(url=pdf_link, headers=cabeceras, allow_redirects=False)
        # eGela devuelve un 303 See Other
        respuesta = requests.get(url=respuesta.headers['Location'], headers=cabeceras, allow_redirects=False)
        
        print(selection, ": ", pdf_name, "descargado\n")
        pdf_content = respuesta.content
        
        return pdf_name, pdf_content
