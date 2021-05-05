from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Users\\panch\\Desktop\\python\\driver\\\chromedriver.exe")

url = "https://www.cmfchile.cl/institucional/hechos/hechos.php"

driver.get(url)

# barra de opciones
x = driver.find_element_by_name('tipoentidad')
drop = Select(x)

drop.select_by_visible_text("Banco")

# barra de la entidad
barra1 = driver.find_element_by_name("entidad")
barra1.send_keys("Banco Estado")
barra1.send_keys(Keys.RETURN)

# fecha de inicio
barra2 = driver.find_element_by_name("p_fecha_desde")
barra2.send_keys("01/01/2011")
barra2.send_keys(Keys.RETURN)

# hasta esta fecha
barra3 = driver.find_element_by_name("p_fecha_hasta")
barra3.send_keys("01/01/2020")
barra3.send_keys(Keys.RETURN)

# tiempo para llenar el captcha
time.sleep(20)

# hacer click en consultar
button = driver.find_element_by_name("consultar")
button.click()

