import os
import nltk
nltk.download('punkt')	
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

############################################################
#Step 1 load all documents from "files" folder
from load_doc import load_doc
script_dir = os.path.dirname(__file__)	#get dir of current script folder
files_folder_path = os.path.join(script_dir, "files/")	#get "files" folder path

doc_list=[]	#keep all opened docs
for doc_name in os.listdir(files_folder_path):	#for each doc in files folder:
	doc_path= os.path.join(files_folder_path, doc_name) # get absolute path of each doc
	document=load_doc(doc_path)	#call "load_doc", return doc:  doc[0] is doc_name, doc[1] is doc_content
	doc_list.append(document)	#append each doc to doc_list

#now each doc in doc_list represents a file
#data structure of doc: 
#doc[0] is doc_name
#doc[1] is doc_content in plain string

############################################################
#Step 2 extract and print phone number

from parse_phone import parse_phone

for doc in doc_list:
	phone_number=parse_phone(doc[1])
	if len(phone_number)>1:
		print ('phone number found in ',doc[0],' !')
		print ('phone number is: ',phone_number)


############################################################
#Step 3 determine document language
from get_language import get_language
#doc_lang_list=[]
for doc in doc_list:
	lang=get_language(doc[1])
	print ('language of "' + doc[0] + '" is :')
	print (lang)
	doc.append(lang)

	#updated data structure of doc in doc_list: 
	#doc[0] is doc_name
	#doc[1] is doc_content
	#doc[2] is doc_language
print ('next stage may take a while...')
############################################################
#Step 4 dealing with non-english files

#Note:
#Majority of files are in englih, other files in french and german will become outliers when we do tf-idf based clustering study (french/german doc will have no word match with majority of english words).  
#to resolve this, there are several options:
#1. We can remove french and german files from clustering study(i.e. remove outliers)
#2. we can do 3 separate clustering study, each study only use files of one language
#3. we can translate german/french files to english (for example, use goslate package or other api), then treat traslated content as english files
#4. we can do abstract word embedding such as word2Vec, convert all english/french/german words into abstract vector space, and cluster using abstract vector space instead of literal vocabulary

#For simplicity reason, we will only do option 1, perform clustering for english files only.
#below separate the files according to the detected language
english_doc_list=[]
german_doc_list=[]
french_doc_list=[]
for doc in doc_list:
	if doc[2]=='english':
		english_doc_list.append(doc)
	if doc[2]=='german':
		german_doc_list.append(doc)
	if doc[2]=='french':
		french_doc_list.append(doc)
############################################################
#Step 5 extract proper nouns using POS
from proper_nouns import get_proper_nouns
for doc in english_doc_list:	
	proper_nouns=get_proper_nouns(doc[1])
	doc.append(proper_nouns)
#	print (doc[0], '  ---  list of proper nouns: ',proper_nouns)

	#updated data structure of doc in english_doc_list: 
	#doc[0] is doc_name
	#doc[1] is doc_content
	#doc[2] is doc_language
	#doc[3] is doc_proper_nouns

############################################################
#Step 6 stemm & lemma
from stemm_lemma import stemm_lemma
for doc in english_doc_list:	
	stemmed_proper_nouns=stemm_lemma(doc_content=doc[3],doc_lang=doc[2])
	doc.append(stemmed_proper_nouns)
#	print (doc[0], '  ---  list of stem proper nouns: ',stemmed_proper_nouns)

	#updated data structure of doc: 
	#doc[0] is doc_name
	#doc[1] is doc_content
	#doc[2] is doc_language
	#doc[3] is doc_proper_nouns
	#doc[4] is stemmed_proper_nouns


############################################################
#Step 7 vectorize word space with tf-idf
from tfidf import tfidf
corpus=[]	#corpus of all english docs
for doc in english_doc_list:
	word_string=' '.join(doc[4])	#join proper nouns to form one string for each doc
	corpus.append(word_string)	#create corpus using strings of all docs

vec_df=tfidf(corpus)	#return tf-idf vectorized dataframe
#	print ('vectoerized word space is :  ',vec_df)

############################################################
#Step 8 apply clustering ,  used K-Means with auto select K based on elbow method)
from auto_cluster import find_optimum_k
from auto_cluster import kmeans
optimum_k=find_optimum_k(vec_df)
cluster_label= kmeans(vec_df,optimum_k)
#print out cluster labels
doc_number=0
for doc in english_doc_list:
	print ('file name is : "', doc[0],'"')
	doc.append(cluster_label[doc_number])
	print ('file cluster number is : ', cluster_label[doc_number])
	doc_number+=1

	#updated data structure of doc:
	#doc[0] is doc_name
	#doc[1] is doc_content
	#doc[2] is doc_language
	#doc[3] is doc_proper_nouns
	#doc[4] is stemmed_proper_nouns
	#doc[5] is cluster number

############################################################
#Step 9 visualization of clustering in 2-D space
#use PCA to reduce dimention to 2-D:
from pca import pca
pca_df=pca(vec_df,n=2)


#plot principal componets with pyplot
import numpy as np
import tkinter

import matplotlib
import matplotlib.pyplot as plt

labeled_pca_df= np.column_stack((pca_df, cluster_label)) #add cluster label to df
plt.scatter(x=labeled_pca_df[:,0],y=labeled_pca_df[:,1],c=labeled_pca_df[:,2],alpha=0.5)
plt.ylim([-5,5])
plt.xlim([-5,5])
plt.show()

############################################################
#Step 10 generate analysis report: analysis.txt 

f= open("analysis.txt","w+")
for doc in english_doc_list:
	f.write("File name:  "+doc[0]+"\r\n")
	f.write("File language:  "+doc[2]+"\r\n")
	proper_nouns='  '.join(doc[3])
	f.write("words identified as proper nouns:  "+proper_nouns+"\r\n")
	stemm_nouns='  '.join(doc[4])
	f.write("wordspace after stemm-lemma:  "+stemm_nouns+"\r\n")
	f.write("File belongs to cluster:  "+str(doc[5])+"\r\n")
	f.write("\r\n")
for doc in french_doc_list:
	f.write("File name:  "+doc[0]+"\r\n")
	f.write("File language:  "+doc[2]+"\r\n")
	f.write("File is not in English, did not perform POS and stemm-lemma"+"\r\n")
for doc in german_doc_list:
	f.write("File name:  "+doc[0]+"\r\n")
	f.write("File language:  "+doc[2]+"\r\n")
	f.write("File is not in English, did not perform POS and stemm-lemma"+"\r\n")
f.close()
	




#end

