import nltk
from nltk.stem import SnowballStemmer						
from nltk.stem import WordNetLemmatizer

def stemm_lemma(doc_content,doc_lang):

	stemm = SnowballStemmer(doc_lang)	#snowballstemmer need language parameter
	lemma = WordNetLemmatizer()

	stemm_lemma_wordlist=[]
	for word in doc_content:
		word= stemm.stem(word)	#word stemming
		word=lemma.lemmatize(word)	#word lemmatization
		stemm_lemma_wordlist.append(word)

	return	stemm_lemma_wordlist
