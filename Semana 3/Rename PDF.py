import os

# Directorio de archivos
os.chdir('C:\\Users\\marti\\OneDrive\\Desktop\\Data CMF\\Pdfs\\Hechos Esenciales\\Marzo 2016 - Marzo 2010')

i = 0

for file in os.listdir():

    new_file_name = "Archivo-{}.pdf". format(i) # Nombre de archivo y formato
    os.rename(file, new_file_name)

    i = i +1