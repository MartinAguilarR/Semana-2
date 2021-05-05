import os

os.chdir('')  # Directorio a cambiar

i = 0

for file in os.chdir():

    new_file_name = "Archivo - {}.pdf".format(1)
    os.rename(file, new_file_name)

    i = i +1
