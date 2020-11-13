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
		contador  = 0
		lst = []
		anterior = 600
		actual = 0
		dataset = pd.read_csv('Libros.csv')
		lista = dataset.iloc[:,[1,3]].values
		for lib in lista:
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
							lst.append(nuevoLibro) 
		return lst