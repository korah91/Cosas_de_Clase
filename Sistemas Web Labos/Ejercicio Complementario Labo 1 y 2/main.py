from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
# http://websistemak-httptest.appspot.com/html/inprimakia.html

def main():
    # Abro el navegador
    driver = webdriver.Firefox()
    url = "http://websistemak-httptest.appspot.com/html/inprimakia.html"
    driver.get(url)

    # Utilizo los XPath de los 3 primeros checkboxes para marcar las casillas correctas
    # Tambien podria haber utilizado //form/input[i] siendo i 1, 2 y 3 para localizar los input child del form
    driver.find_element_by_xpath("//input[@value='a']").click()
    driver.find_element_by_xpath("//input[@value='b']").click()
    driver.find_element_by_xpath("//input[@value='c']").click()
    # El boton de submit tiene el atributo type = submit
    driver.find_element_by_xpath("//input[@type='submit']").click()

    # Ya he llegado a la imagen
    imagen = driver.find_element_by_tag_name("img")

    # Trato las posibles excepciones
    try:
        with open('keanu.png', 'wb') as file:
            print("Se ha descargado la imagen keanu.png")
            file.write(imagen.screenshot("keanu.png"))
    except:
        pass

if __name__ == '__main__':
    main()
