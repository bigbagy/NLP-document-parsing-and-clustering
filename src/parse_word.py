import os
import docx2txt


def parse_word(doc_path):

	# extract text
	text = docx2txt.process(doc_path)


	return (text)

'''
######################
#below is for testing

script_dir = os.path.dirname(__file__)	#get path of current script folder
files_folder_path = os.path.join(script_dir, "files/image_nazis.docx")	#get path of "files" folder

text=parse_word(files_folder_path)

print (text)
print ('type of return value is : ',type(text))
'''
