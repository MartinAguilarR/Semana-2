# Importaciones
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

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

time.sleep(40)

data = {}
df1 = pd.DataFrame(columns=['Fecha', 'N.Documento', 'Entidad', 'Materia'])  # Nombres de los header de tabla

rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/th"))
print(rows)
print(cols)

# Considerar Alinear elementos dentro de 'data['']' según definición de headers
for r in range(2, rows + 1):
    data['Fecha'] = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[1]").text
    data['N.Documento'] = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[2]").text
    data['Entidad'] = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[3]").text
    data['Materia'] = driver.find_element_by_xpath(
        "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[4]").text
    df1 = df1.append(data, ignore_index=True)
    print(df1)
df1.to_csv('Hechos 2017 - 2021')
