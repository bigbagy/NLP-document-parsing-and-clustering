import os
import codecs
from parse_pdf import parse_pdf
from parse_word import parse_word
from parse_pptx import parse_pptx

def load_doc(doc_path):
	doc=[]
#############################################################
#txt:
	if doc_path.lower().endswith('.txt'):	#if file extension .txt
		read_doc = codecs.open(doc_path, encoding='utf-8')	#open txt, currently only support utf-8

		doc_content = read_doc.read()	#get doc content
		doc_name=os.path.basename(read_doc.name)	#get doc name

		doc.append(doc_name)	#save doc_name
		doc.append(doc_content)	#save doc_content 
#############################################################
#pdf:


	if doc_path.lower().endswith('.pdf'):	#if file extension .pdf
		doc_content=parse_pdf(doc_path)


		pdf_doc= open(doc_path,'rb')
		doc_name=os.path.basename(pdf_doc.name)	#get doc name

		doc.append(doc_name)	#save doc_name
		doc.append(doc_content)	#save doc_content

#############################################################
#word docx:

	if doc_path.lower().endswith('.docx'):	#if file extension .docx
		doc_content=parse_word(doc_path)


		pdf_doc= open(doc_path,'rb')
		doc_name=os.path.basename(pdf_doc.name)	#get doc name

		doc.append(doc_name)	#save doc_name
		doc.append(doc_content)	#save doc_content
#############################################################
#powerpoint pptx:

	if doc_path.lower().endswith('.pptx'):	#if file extension .pptx
		doc_content=parse_pptx(doc_path)


		pdf_doc= open(doc_path,'rb')
		doc_name=os.path.basename(pdf_doc.name)	#get doc name

		doc.append(doc_name)	#save doc_name
		doc.append(doc_content)	#save doc_content


#############################################################
#return result
	return doc 
	#data structure of doc: 
	#doc[0] is doc_name
	#doc[1] is doc_content
