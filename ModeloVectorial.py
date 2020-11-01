import numpy as np #Se utiliza numpy para crear arreglos ya que estos son más rapidos que las listas
import math
class ModeloVectorial:

	#El vocabulario debe ser una lista en el orden que se desee que esten las caracteristicas en los vectores
	def __init__(self):
		self.vectors = []
		self.vocabulary = {}
		self.idf = []
		self.tamVoc = 0

	def __init__(self,lists,vocabulary):
		self.vocabulary = {}
		self.idf = []
		self.vectors = []
		self.tamVoc = len(vocabulary)
		#Iniciamos el diccionario con las unidades del vocabulario como clave y su ubicación en el vector como valor
		for i in range(len(vocabulary)):
			self.vocabulary[vocabulary[i]] = i
		for lis in lists:
			self.addVector(self.getTF(lis))

	def addVocab(newVocabulary):
		newF = list(set(newVocabulary) - set(self.vocabulary.keys())) 
		if(len(newF) > 0):
			cont = 0
			for feature in newF: 
				self.vocabulary[feature] = self.tamVoc + cont 
				cont = cont + 1
			self.tamVoc = len(self.vocabulary)
	
	def addVector(self,tf):# Agregamos un nuevo vector nuestro espacio vectorial
		nv = np.array([tf])
		if self.vectors == []:#El espacio vectorial esta vacio
			self.vectors = nv
		else:
			self.vectors = np.concatenate((self.vectors,nv),axis = 0)

	def getTF(self,lista):#Formamos la lista con el term frequency(tf) de cada lemma
		vector = [0]*self.tamVoc
		for lemma in lista:
			vector[self.vocabulary[lemma]] = vector[self.vocabulary[lemma]] + 1
		return vector

	def getIDF(self):#Formamos la lista con el inverse document frequency (idf) de cada lemma
		N = len(self.vectors) # Numero de documentos o filas en el espacio vectorial
		self.idf = [0]*self.tamVoc
		for i in range(N): 
			vector = self.vectors[i]
			for lemma in self.vocabulary.keys():#Contamos por cada lema si dicho lemma esta al menos una vez en cada documento 
				index = self.vocabulary[lemma] 
				if(vector[index] > 0):
					self.idf[index] = self.idf[index] + 1
		for i in range(self.tamVoc):
			self.idf[i] = math.log(N/(self.idf[i])) 
		

	def getTFIDF(self,vector):#Convertimos una lista con valores tf  

		pass

	def addFeatures(lfeatures):# Agrega una nueva caracteristica al final de de cada vector 
		addVocab(lfeatures)#Agregamos las nuevas caracteristicas al vocabulario
		for feature in lfeatures:
			np.insert(self.vectores, self.vectores.shape[1], np.array([0]*len(self.vectores)), 1)


	def delFeature(feature):
		np.delete(self.vectores,self.vocabulary[feature],axis = 1 )
		self.vocabulary.pop(feature) 

