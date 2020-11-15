import Libro
import jsonpickle #serializar objetos complejos en json 
import json
import pandas as pd
from Libro import *
class UsualTools:
	
	@staticmethod
	def getText(fname):
		try:
			file = open(fname,"r",encoding = "utf8")
			txt = file.read()
		except:
			file = open(fname,"r",errors='ignore')
			txt = file.read()
		file.close()
		return txt
	@staticmethod
	def getTextLines(fname):
		try:
			file = open(fname,"r",encoding = "utf8")
			txt = file.readlines()
		except:
			file = open(fname,"r",errors='ignore')
			txt = file.readlines()
		file.close()
		return txt
	@staticmethod
	def saveObject(obj,fname):
		frozen = jsonpickle.encode(obj)
		with open(fname, "w") as file:
			file.write(frozen)
			file.close()

	@staticmethod
	def loadObject(fname):
		with open(fname) as file:
			frozen = file.read() #json.load(file)
			obj = jsonpickle.decode(frozen)
			return obj
		
		
	@staticmethod
	def graficaCalif(dataset):
		calif = dataset["Promedio de estrellas"]
		fig, ax = plt.subplots(figsize=(12, 8))
		ax.hist(calif, density=False)

		for barra in ax.patches: 
    			height = barra.get_height()
    			ax.annotate(f'{int(height)}', xy=(barra.get_x()+barra.get_width()/2, height), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
		
	@staticmethod
	def generaEstrellas(calif):
    
		a = 5
		b = 3.9
    
		c = 3.6
		d = 3
    
		e = 2.8
		f = 0
    
		if ((calif <= a) and (calif >= b)):
			return 3    
		elif ((calif <= c) and (calif >= d)):
			return 2
		elif ((calif <= e) and (calif >= f)):
			return 1  
		else:
			return -1


	@staticmethod
	def getLibros(addr):#Retorna una lista de objetos tipo Libro de una direcci[on dada
		dataset = pd.read_csv('Libros.csv')
		dataset = dataset.dropna(subset=['Número']) #Eliminamos las rows sin id (número)
		lista = dataset.iloc[:,[0,3,1]].values#lista = dataset.iloc[:,[1,3]].values
		#contador  = 0
		star = "*"
		lstLibros = []
		for i in range(1,101): #(f"Libros de Goodreads/{i}.txt")
		    for libro in lista:
			with open(f"Libros de Goodreads/{i}.txt", errors='ignore') as file: #open('Libros de Goodreads/'+str(i)+'.txt') as file:  #open(f'{'Libros de Goodreads/'}{i}{'.txt'}')
			    if i == libro[0]:
				texto = file.read()
				estrellas = UsualTools.generaEstrellas(lista[i, 1]) #generaEstrellas(lista[i, 1])
				nuevoLibro = Libro(libro [0], libro[2], libro[1], estrellas, texto)
				lstLibros.append(nuevoLibro)
				#contador+=1
				#print(f'{contador:{6}}) {nuevoLibro.id:<{8}} {nuevoLibro.nombre:<{50}}  {nuevoLibro.calif:{5}} {nuevoLibro.estrellas*star:{6}}')      


		
		"""for lib in lista:
			cont = 0
			for i in range(1,156): #(f"Libros de Goodreads/{i}.txt")
				fname = addr+f"/{i}.txt"

				with open(fname, errors='ignore') as file: #open('Libros de Goodreads/'+str(i)+'.txt') as file:  #open(f'{'Libros de Goodreads/'}{i}{'.txt'}')
					x = file.read()
					actual = x.find(lib[0], 0, 500)
					if(actual!=-1):
						if( True):   
							anterior = actual
							contador+=1
							#AQUI AJUSTAR LA CALIFICACIÓN CONFORME A LAS CLASES DEFINIDAS
							estrellas = UsualTools.generaEstrellas(lib[1])
							nuevoLibro = Libro(lib[0], lib[1], estrellas, x,i)
							lst.append(nuevoLibro)""" 
		return lstLibros
