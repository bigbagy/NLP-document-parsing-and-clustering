import nltk
import re
from nltk.tokenize import word_tokenize

def get_proper_nouns(content):

	tokens = nltk.pos_tag(word_tokenize(content))	#tokenize and apply POS tag

	proper_noun_list=[]
	for tup in tokens:
		if tup[1]=='NNP':
			NNP= tup[0]
			NNP=re.sub('_','',NNP)	#remove '_' in words
			proper_noun_list.append(NNP)	#if tagged as proper noun, save to list

	return (proper_noun_list)	#return list of proper nounsfound

