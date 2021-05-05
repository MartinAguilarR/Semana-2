import pandas as pd

# Unión DataFrames

df1 = pd.read_csv(
    'C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Crawler CMF\\Resoluciones_cursadas')  # Cambiar dirección segun usuario
df2 = pd.read_csv(
    'C:\\Users\\marti\\OneDrive\\Documentos\\GitHub\\Crawler_lab\\Crawler CMF\\Resoluciones_cursadas_links')  # Cambiar dirección segun usuario

Resoluciones_cursadas_data = pd.merge(df1, df2).to_csv('Resoluciones_cursadas_data')
print(Resoluciones_cursadas_data)