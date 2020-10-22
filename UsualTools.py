import pickle
class UsualTools:
	
	@staticmethod
	def getText(fname):
		file = open(fname,"r",encoding = "utf8")
		txt = file.read()
		file.close()
		return txt
	@staticmethod
	def saveObject(obj,fname):
		from pickle import dump
		pkfile = open(fname,"r",encoding = "utf8")
		dump(obj,pkfile)
		pkfile.close()
	@staticmethod
	def loadObject(fname):
		from pickle import dump
		file = open(fname,"r",encoding = "utf8")
		pkfile = load(pkfile)
		pkfile.close()
		return pkfile