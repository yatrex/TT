import spacy
import nltk
import UsualTools
import os
import re
from UsualTools import *

class TextNormalizer:
	def __init__(self):
		self.vocabulary = set()
		self.nlp = spacy.load("en_core_web_sm")
		self.stopwords = set(nltk.corpus.stopwords.words('english')) | self.nlp.Defaults.stop_words#Utilizamos las stopwords proporcionadas por nltk y spacy
		self.tokens = []
	def setText(self,text):
		self.tokens= self.nlp(text)

	def setVocabulary(self,vocabulary):
		self.vocabulary = vocabulary

	def deleteSpecialChars(self,text):
		expr = r'[^a-zA-Z]'
		filtered = " " 
		for token in text.split():
			cadena = re.sub(expr, r'', token)
			if (len(cadena) > 0):
				filtered =filtered + cadena+" " 	
		return filtered 
	

	def lemmatize_delSW(self):# Lemmatiza y quita las stopwords
		lemmas = []
		for tok in self.tokens:
			if (not(tok.text in self.stopwords) or not(tok.lemma_ in self.stopwords)  ):
				lemmas.append(tok.lemma_)
		self.vocabulary = set(lemmas) | self.vocabulary
		return lemmas
	
				
	def delExtraInfoPG(self,fname):#Elimina información extra de los libros del Projecto Gutenberg
		cad = ["*** END","***END"]# Cadenas que indica que el libro termino
		txtL = UsualTools.getTextLines(fname)
		txt= " "
		nl = len(txtL)
		ctxt = " "
		cut1 = 30#Indica cuantas lineas del inicio queremos quitar
		cut2 = nl-300 #Indica la linea apartir donde el contenido del libro termina
		if (nl >40): # Si tiene m[as de 10 lioneas es mas probable que sea del proyecto gutenberg
			cont = 200
			while(cont > 0):
				if(cad[0] in txtL[nl - cont -250] or cad[1] in txtL[nl - cont -250]):
					cut2 = nl - cont -250
					break
				cont = cont -1
			for i in range(cut1,cut2):
				txt = txt + txtL[i]
		else:
			txt = txtL[nl - 1]
		return txt.strip()