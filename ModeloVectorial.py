import numpy as np #Se utiliza numpy para crear arreglos ya que estos son más rapidos que las listas
class ModeloVectorial:

	#El vocabulario debe ser una lista en el orden que se desee que esten las caracteristicas en los vectores
	def __init__(self):
		self.vectors = []
		self.vocabulary = {}

	def __init__(self,lists,vocabulary):
		self.vocabulary = {}
		self.vectors = np.array(lists)
		self.tamVoc = len(vocabulary)
		#Iniciamos el diccionario con las unidades del vocabulario como clave y su ubicación en el vector como valor
		for i in range(len(vocabulary)):
			self.vocabulary[vocabulary[i]] = i

	def addVector(self,lista):# Agregamos un nuevo vector nuestro espacio vectorial
		nv = np.array([lista])
		try:
			self.vectors = np.concatene(self.vectors,nv)
		except:#El espacio vectorial esta vacio
			self.vectors = nv

	def contLemmas(self,lista):#Formamos la lista con la concordancia de cada lemma
		vector = [0]*self.tamVoc
		for lemma in lista:
			vector[self.vocabulary[lemma]] = vector[self.vocabulary[lemma]] + 1
		return vector

