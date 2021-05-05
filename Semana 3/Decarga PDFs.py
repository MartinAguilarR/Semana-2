# Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuración para descargar Pdf
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\marti\\OneDrive\\Desktop\\Data CMF\\Pdfs\\Hechos Esenciales\\Marzo 2017 - Marzo 2021",
        # Link descarga
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
 })

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")

df = pd.read_csv('C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Semana-2\\Semana 3\\Hechos 2017 - 2021_links')
links = df.iloc[:, 1]

print(links)

for url in links:
    driver.get(url)