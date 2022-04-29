# -*- coding: UTF-8 -*-
from tkinter import messagebox
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

    def __init__(self, root):
        self._root = root

    def check_credentials(self, username, password, event=None):
        popup, progress_var, progress_bar = helper.progress("check_credentials", "Logging into eGela...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()
		
        print("##### 1. PETICION #####")
        
        uri='https://egela.ehu.eus/login/index.php'
        respuesta = requests.get(url=uri)
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        #print(soup.prettify())
        print(str(respuesta.status_code) + ' ' + respuesta.reason)
        cookie = respuesta.cookies['MoodleSessionegela']
        logintoken = soup.find(attrs={'name': 'logintoken'}).get('value')
        print('El servidor devuelve la Cookie MoodleSession ' + str(cookie) + ' y el logintoken ' + str(logintoken))
        cookie = 'MoodleSessionegela=' + str(cookie)
        logintoken = str(logintoken)
        
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################
        progress = 25
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)

        cabeceras = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': cookieSession}
        datos = {
            'logintoken': logintoken,
            'username': str(username),
            'password': str(password)
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


		

        print("##### 2. PETICION #####")
       
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 50
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)

        print("\n##### 3. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 75
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)

        print("\n##### 4. PETICION #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        progress = 100
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(1)
        popup.destroy()

        if COMPROBACION_DE_LOG_IN:
            #############################################
            # ACTUALIZAR VARIABLES
            #############################################
            self._root.destroy()
        else:
            messagebox.showinfo("Alert Message", "Login incorrect!")

    def get_pdf_refs(self):
        popup, progress_var, progress_bar = helper.progress("get_pdf_refs", "Downloading PDF list...")
        progress = 0
        progress_var.set(progress)
        progress_bar.update()

        print("\n##### 4. PETICION (Página principal de la asignatura en eGela) #####")



        progress_step = float(100.0 / len(NUMERO DE PDF_EN_EGELA))


        print("\n##### Analisis del HTML... #####")
        #############################################
        # ANALISIS DE LA PAGINA DEL AULA EN EGELA
        # PARA BUSCAR PDFs
        #############################################

        # INICIALIZA Y ACTUALIZAR BARRA DE PROGRESO
        # POR CADA PDF ANIADIDO EN self._refs
        progress_step = float(100.0 / NUMERO_DE_PDFs_EN_EGELA)


        progress += progress_step
        progress_var.set(progress)
        progress_bar.update()
        time.sleep(0.1)

        popup.destroy()
        return self._refs

    def get_pdf(self, selection):

        print("\t##### descargando  PDF... #####")
        #############################################
        # RELLENAR CON CODIGO DE LA PETICION HTTP
        # Y PROCESAMIENTO DE LA RESPUESTA HTTP
        #############################################

        return pdf_name, pdf_content
