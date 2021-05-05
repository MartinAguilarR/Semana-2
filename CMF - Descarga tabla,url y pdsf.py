# Importaciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Set options & open server
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(options=chrome_options,
                          executable_path="C:\\Program Files (x86)\\chromedriver.exe")


# Información asociada a la tabla
def get_data(url):
    driver.get(url)
    print(driver.title)

    data = {}
    df1 = pd.DataFrame(columns=['N°', 'Fecha', 'Materia'])

    rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr"))
    cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[1]/th"))
    print(rows)
    print(cols)

    for r in range(2, rows + 1):
        data['N°'] = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[1]").text
        data['Fecha'] = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[2]").text
        data['Materia'] = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr[" + str(r) + "]/td[3]").text
        df1 = df1.append(data, ignore_index=True)
        print(df1)
    df1.to_csv('Data_tabla')


# Aplicar función
get_data('')


# Obtención de links
def link(url):
    # Navegador
    driver.get(url)
    data = {}
    df2 = pd.DataFrame(columns=['Links'])

    #Definición de elemento contenedor de 'href'
    ids = driver.find_elements_by_css_selector('.mime_doc')
    for ii in ids:
        data['Links'] = ii.get_attribute('href')
        df2 = df2.append(data, ignore_index=True)
        print(df2)
    df2.to_csv('Data_links')


# Aplicar función
link('')

# Unión DataFrames
df1 = pd.read_csv(
    'C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Data_tabla')  # Cambiar dirección segun usuario
df2 = pd.read_csv(
    'C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Data_links')  # Cambiar dirección segun usuario
Data_final = pd.merge(df1, df2, on='id').to_csv('Data_final')
print(Data_final)


def pdf():

    # Configuración para descargar Pdf
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": "C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Pdfs",
        # Link descarga
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    }
                                           )
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path="C:\\Program Files (x86)\\chromedriver.exe")

    df = pd.read_csv('C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Data CMF\\Data_final')
    links = df.iloc[:, 5]
    print(links)

    for url in links:
        driver.get(url)