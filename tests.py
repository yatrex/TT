import ModeloVectorial
import TextNormalizer
from ModeloVectorial import *
from TextNormalizer import *

exp = TextNormalizer()
llemmas = []
for i in range(1,3):
	txt = UsualTools.getText("C:/Users/Lenovo 330S/Desktop/Weas de TT/TT/Libros de Goodreads/"+str(i)+".txt")
	tokens = exp.textTokenizer(txt)
	tokens = exp.deleteSpecialChars(tokens)
	print("Texto"+str(i)+" crudo es de "+str(len(tokens)))
	tokens = exp.deleteStopWords(tokens)
	print("Sin stopwords son "+str(len(tokens)))
	taggedTokens = exp.taggPOS(tokens)
	lemmas = exp.lemmatize(taggedTokens)
	nle = len(lemmas)
	llemmas.append(lemmas)
	print("Los lemas son " + str(nle))
	print("vocabulario es " + str(len(exp.vocabulary)))

mv = ModeloVectorial(llemmas,list(exp.vocabulary))
suma  = 0

mv.getIDF()
print(mv.vectors[0][9137])
mv.addFeatures(["hola","bien"])

print(mv.vectors[0][9138])
print("vocabulario es " + str(len(mv.vocabulary)))
