import os

# Renombrar archivos

os.chdir('')  #Directorio de descarga de los pdfs

i = 0
for file in os.listdir():

    new_file_name = "Archivo - {}.pdf".format(i)
    os.rename(file, new_file_name)

    i = i +1