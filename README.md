# Semana-2
Durante esta semana, el objetivo fué scrapear dos paginas de la cmf, ambas en formato tabla con una columna de links de PDFs
BeautifulSoup es un buen modelo para scrapear varios arcivos de un mismo tipo, por ejemplo ".pdf", ".mp3", ".jpg", sin embargo para el caso de CMF no sirve, puesto que la página de la CMF no contiene los archivos, solo tiene enlaces que muestran el archivos pdf. 
Por lo tanto cuando el modelo filtra los urls del tipo ".pdf" que es la base del modelo, no encuentra nada. 
