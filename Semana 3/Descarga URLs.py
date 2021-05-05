# Importaciones
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

import csv

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

# Chrome
driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")


url = 'https://www.cmfchile.cl/institucional/hechos/hechos.php'
driver.get(url)

# barra de opciones
x = driver.find_element_by_name('tipoentidad')
drop = Select(x)

drop.select_by_visible_text("Todas")

# barra de la entidad
barra1 = driver.find_element_by_name("entidad")
barra1.send_keys("")
barra1.send_keys(Keys.RETURN)

# fecha de inicio
barra2 = driver.find_element_by_name("p_fecha_desde")
barra2.send_keys("01/03/2017")
barra2.send_keys(Keys.RETURN)

# hasta esta fecha
barra3 = driver.find_element_by_name("p_fecha_hasta")
barra3.send_keys("01/03/2021")
barra3.send_keys(Keys.RETURN)

# tiempo para llenar el captcha
time.sleep(20)

# hacer click en consultar
button = driver.find_element_by_name("consultar")
button.click()
data = {}
df = pd.DataFrame(columns=['Links'])

time.sleep(35)

ids = driver.find_elements_by_css_selector('.mime_doc') #Definición de elemento para descarga
for ii in ids:
    data['Links'] = ii.get_attribute('href')
    df = df.append(data, ignore_index=True)
    print(df)
df.to_csv('Hechos 2017 - 2021_links')
