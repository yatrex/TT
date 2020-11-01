import nltk
import UsualTools
import os
import re
from UsualTools import *
from nltk import *
class TextNormalizer:
	def __init__(self):
		self.vocabulary = set()

	def deleteSpecialChars(self,tokens):
		expr = r'[^a-zA-Z0-9 ]'
		filtered =[] 
		for token in tokens:
			cadena = re.sub(expr, r'', token)
			if (len(cadena) > 0):
				filtered.append(cadena) 	
		return filtered
	def textTokenizer(self,text):
		from nltk import word_tokenize
		tokens = nltk.word_tokenize(text)
		return tokens 
	
	def deleteStopWords(self,tokens):#token:list of tokens
		stopword_list = nltk.corpus.stopwords.words('english')
		ntokens = [token for token in tokens if token not in stopword_list]
		return ntokens
	
	def taggPOS(self,tokens):
		taggedTokens = nltk.pos_tag(tokens, tagset='universal')
		return taggedTokens
	
	def lemmatize(self,taggedTokens):
		wnl = WordNetLemmatizer()
		lemmas = []
		for taggedToken in taggedTokens :
			try:
				lemmas.append(wnl.lemmatize(taggedToken[0].lower(),taggedToken[1].lower()))#Se considera solo el primer caracter de la etiqueta
			except:
				lemmas.append(wnl.lemmatize(taggedToken[0].lower()))#Si la etiqueta POs no es manejada por el lematizador le lematizara sin ayuda de la etiqueta
		self.vocabulary = set(lemmas) | self.vocabulary # A medida que obtengamos nuevos lemmas, se agregaran a nuestro vocabualrio
		return lemmas