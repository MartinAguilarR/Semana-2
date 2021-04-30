# pip install requests
# pip install BeautifulSoup
# pip install PyPDF2
# pip install html5lib
# pip install bs4

# for get the pdf files or url
import requests

# for tree traversal scraping in webpage
from bs4 import BeautifulSoup

# for input and output operations
import io

# For getting information about the pdfs
from PyPDF2 import PdfFileReader

# website to scrap
url = "https://www.cmfchile.cl/institucional/sanciones/sanciones_mercados_entidad.php"
  
# get the url from requests get method
read = requests.get(url)
  
# full html content 
html_content = read.content
  
# Parse the html content 
soup = BeautifulSoup(html_content, "html.parser")

# created an empty list for putting the pdfs
list_of_pdf = set()

# accessed the fist p tag in the html
l = soup.find('p')

# accessed all the anchors tag from given p tag
p = l.find_all('a')

# iterate through p for getting all the href links
for link in p:
	
	# original html links
	print("links: ", link.get('href'))
	print("\n")
	
	# converting the extention from .html to .pdf
	pdf_link = (link.get('href')[:-5]) + ".pdf"
	
	# converted to .pdf
	print("converted pdf links: ", pdf_link)
	print("\n")
	
	# added all the pdf links to set
	list_of_pdf.add(pdf_link)



def info(pdf_path):

	# used get method to get the pdf file
	response = requests.get(pdf_path)

	# responce.content generate binay code for
	# string function
	with io.BytesIO(response.content) as f:

		# initialized the pdf
		pdf = PdfFileReader(f)

		# all info about pdf
		information = pdf.getDocumentInfo()
		number_of_pages = pdf.getNumPages()

	txt = f"""
	Information about {pdf_path}:
	
	Author: {information.author}
	Creator: {information.creator}
	Producer: {information.producer}
	Subject: {information.subject}
	Title: {information.title}
	Number of pages: {number_of_pages}
	"""
	print(txt)
	
	return information

# print all the content of pdf in the console
for i in list_of_pdf:
	info(i)
