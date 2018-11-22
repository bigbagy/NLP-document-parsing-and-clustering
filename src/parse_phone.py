import re

'''
currently only surpport Singapore phone parsing with below format:
+65 99999999 
65 99999999 
(65) 99999999
(65)99999999
98765432
9876 5432

'''

def parse_phone(content):
	r = re.compile(r'((\+?\(?65\)?\s?)?\d{4}\s?\d{4})')
	results=r.findall(content)
	return (results)

#the current regex is a functionality demo
#if given more time, the regex can be fine tuned, and more regex can be added to parse other country's phone number

