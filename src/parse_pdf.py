import PyPDF2 
import os

def parse_pdf(doc_path):

	pdfFileObj = open(doc_path,'rb')

	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	num_pages = pdfReader.numPages
	count = 0
	text = ""

	while count < num_pages:
	    pageObj = pdfReader.getPage(count)
	    count +=1
	    text += pageObj.extractText()

	return (text)


