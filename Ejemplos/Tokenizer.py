import nltk
import pickle
from nltk import word_tokenize
from pickle import *
from nltk.stem import WordNetLemmatizer 
from nltk.util import ngrams
doc = open("C:/Users/Lenovo 330S/Desktop/Weas de TT/TT/Libros de Goodreads/1.txt","r",encoding = "utf8")
text = doc.read()[2000:4500]
text2 = doc.read()[2000:3000]
doc.close()
tokens = word_tokenize(text)
output = list(ngrams(tokens, 2))
pklfile = open("tokens.pkl","ab")
dump(tokens,pklfile)
pklfile.close()
pklfile = open("tokens.pkl","rb")
tokens2 = load(pklfile)
lemmas = []
wnl = WordNetLemmatizer()
stopword_list = nltk.corpus.stopwords.words('english')
taggedTokens = nltk.pos_tag(tokens, tagset='universal')
filtered_tokens = [token for token in tokens if token not in stopword_list]
for token in taggedTokens :
	try:
		lemmas.append(wnl.lemmatize(token[0],token[1].lower()))
	except:
		lemmas.append(wnl.lemmatize(token[0]))

print(lemmas)