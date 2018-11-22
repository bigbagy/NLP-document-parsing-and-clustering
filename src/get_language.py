
from langdetect import detect

def get_language(content):

	lang_tester = detect(content[:1000])   # only test first 1000 characters to speed up test for very large documents
	if lang_tester=='fr':
		lang='french'
	elif lang_tester=='de':
		lang='german'
	elif lang_tester=='en':
		lang='english'
	else:
		lang='not Recognized'
	
	return(lang)
