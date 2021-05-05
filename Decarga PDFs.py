# Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuración para descargar Pdf
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": "C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Pdfs",
        # Link descarga
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
 })

driver = webdriver.Chrome(options=chrome_options,
                              executable_path="C:\\Program Files (x86)\\chromedriver.exe")

df = pd.read_csv('C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Data_final')
links = df.iloc[:, 5]
print(links)

for url in links:
    driver.get(url)