
import nltk

from string import punctuation


from os import listdir
from os.path import isfile, join


def editDist(word1, word2 ):
	len_1=len(word1)
	len_2=len(word2)

	x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance

	for i in range(0,len_1+1): #initialization of base case values

	    x[i][0]=i
	for j in range(0,len_2+1):

	    x[0][j]=j
	for i in range (1,len_1+1):

	    for j in range(1,len_2+1):

	        if word1[i-1]==word2[j-1]:
	            x[i][j] = x[i-1][j-1] 

	        else :
	            x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
	return x[len_1-1][len_2-1]
words=[]
def remove_non_ascii(text):

	return ''.join(i for i in text if ord(i)<128)
f_words= open("words.txt","a+")
def getWordsFromFile(str):# str is a string/sentence
	lis=[]
	lis1=[]
	word= ""
	#str = result = ''.join(i for i in str if not i.isdigit())

	str = ' '.join(filter(None, (wor.strip(punctuation) for wor in str.split())))
	lis=str.split()
	for k in lis:
		if k not in words:
			words.append(k)

			f_words.write(k+"\n")
	



def after_removing_StopWords(lis,stopWords):
	for x in lis:
		if x in stopWords:

			lis.remove(x)
	return lis
	
	
def start_spelling_process():
	
	onlyfiles = [f for f in listdir("./corpus") if isfile(join("./corpus", f))]

	docx=[]
	stopWordsFile = open("stopWords_en.txt", "r+")
	
	mypath="./corpus/"

	for i in range(0,len(onlyfiles)):

		f0 = open(str(mypath)+str(onlyfiles[i]), "r+")
		str0 = f0.read()
		str0=remove_non_ascii(str0)

		docx.append(str0)

	stopWords = stopWordsFile.read()

	stopWords=remove_non_ascii(stopWords)
	for i in range(0,len(docx)):
		getWordsFromFile(docx[i])
	
	

def provide_correct_word(query):
	new_string=""
	words_file=[]
	with open("words.txt") as f:
		words_file = f.readlines()
	print words_file

	q=query.split()
	correctWords=[]
	for each in q:	
	
		mini=100000
		match=""

		for i in range(0,len(words_file)):
			if(editDist(words_file[i],each) <= mini):
				mini=editDist(words_file[i],each)

				match=words_file[i]

		correctWords.append(match)	

	for i in correctWords:
		new_string+=str(i)+" "
	f_words.close()
	return new_string

	
