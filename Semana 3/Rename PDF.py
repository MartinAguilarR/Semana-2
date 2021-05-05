import os

# Directorio de archivos
os.chdir('')

i = 0

for file in os.listdir():

    new_file_name = "Archivo - {}. pdf". format(i) # Nombre de archivo y formato
    os.rename(file)

    i = i +1