import nltk
import UsualTools
import os
import re
from UsualTools import *
from nltk import *
class TextNormalizer:
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
		tokens = nltk.word_tokenize(txt)
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
		return lemmas

txt = UsualTools.getText("C:/Users/Lenovo 330S/Desktop/Weas de TT/TT/Libros de Goodreads/1.txt").strip()
exp = TextNormalizer()
tokens = exp.textTokenizer(txt)
tokens = exp.deleteSpecialChars(tokens)
print("Texto crudo es de "+str(len(tokens)))
tokens = exp.deleteStopWords(tokens)
print("Sin stopwords son "+str(len(tokens)))
taggedTokens = exp.taggPOS(tokens)
lemmas = exp.lemmatize(taggedTokens)
vocabulario = set(lemmas)
print("Los lemas son " + str(len(lemmas)))
print("El tamaño del vocabulario es: "+str(len(list(vocabulario))))
#print(list(set(lemmas)))
