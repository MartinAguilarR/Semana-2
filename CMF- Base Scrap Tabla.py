#Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
import random

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

# Chrome
driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")

#Definición de url
driver.get("https://www.cmfchile.cl/institucional/resoluciones/resoluciones_cursadas_meses_anteriores.php")
print(driver.title)

#Interacción con página
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(random.uniform(5.0, 8.0))

#Definiicón de filas y columnas
rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr"))#contar filas
cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/th"))#contar columnas

#Número de elementos
print(rows)
print(cols)

#Extracción de datos
print("Numero"+"      "+"Fecha"+"      "+"Materia"+"      "+"Archivo")

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='  ')
    print()

#Cerrar navegador
time.sleep(5)
driver.quit()
