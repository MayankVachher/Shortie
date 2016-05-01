import nltk
import sys
import operator
import string
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize,word_tokenize
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import re

nltk.download('punkt')


#function to be called
def summarizeArticle(query):
	newsArticle = readTextFromFile("./result.txt")
	#print newsArticle

	queryAndTitlesofTopRelevantDocs = readTextFromFile("./summary.txt")
	titleList = queryAndTitlesofTopRelevantDocs.split('\n')
	#title = queryAndTitlesofTopRelevantDocs.split('\n')[0]

	#creating a / delimited string for the 5 titles 
	titlesofTopDocs = ""
	for i in range(4,13,2):
		d = titleList[i].split('\n')
		titlesofTopDocs = titlesofTopDocs + d[-1].replace(',','') + "/"
	#print titlesofTopDocs


	#sentences = sent_tokenize(newsArticle)
	#title = sentences[0]
	#title = newsArticle.split('\n')[0]
	#print title

	wordFrequencies = computeWordFrequencies(newsArticle)
	#printDictionarySorted(wordFrequencies)

	#also pass no. of sentences required
	topNSentences = rankSentencesAndReturnTopN(newsArticle, wordFrequencies, 10)
	#printSentences(topNSentences)
	
	createOutputFile(query, topNSentences, titlesofTopDocs)

def createOutputFile(title, topNSentences, titlesofTopDocs):
	f = open('content.csv', 'w')
	d=[]
	#f.write("testing")
	# print topNSentences
	keyPoints=""
	for sentence in topNSentences:
		d=sentence.split('\n')
		keyPoints = keyPoints + d[-1].replace(',','') + "/"
		# print keyPoints

	f.write(title+","+keyPoints+","+titlesofTopDocs)
	f.close()

def printSentences(topNSentences):
	for sentence in topNSentences:
		print sentence

def readTextFromFile(filePath):
	with open(filePath, "r") as myfile:
		data = myfile.read()

	return data

def computeWordFrequencies(article):

	minCut = 0.05
	maxCut = 0.95

	#returns a dictionary of words and their normalized frequencies

	#make a set of stopWords
	with open("stopWords.txt") as f:										
		stopWords = f.readlines()
		stopWords = [x.strip('\n') for x in stopWords]
		stopWords = set(stopWords + list(punctuation))

	#tokenize lines from the article	
	sentences = sent_tokenize(article)

	#tokenize words from every sentence
	wordsInSentences = [word_tokenize(s.lower()) for s in sentences]

	#make a dictionary of word and its frequency
	wordFrequencies = defaultdict(int)

	#count frequencies for all words
	for sentence in wordsInSentences:
		for word in sentence:
			if word not in stopWords:
				wordFrequencies[word] += 1

	#normalizing frequencies and filtering too frequent or extremely infrequent words
	maxFreqValue = float(max(wordFrequencies.values()))
	for w in wordFrequencies.keys():
		wordFrequencies[w] = wordFrequencies[w]/maxFreqValue
		#if wordFrequencies[w] > maxCut or wordFrequencies[w] < minCut:
		#	del wordFrequencies[w]

	return wordFrequencies

def rankSentencesAndReturnTopN(article, wordFrequencies, n):

	#tokenize lines from the article	
	sentences = sent_tokenize(article)

	#tokenize words from every sentence
	wordsInSentences = [word_tokenize(s.lower()) for s in sentences]

	#dictionary of sentence ranks
	ranking = defaultdict(int)

	for i, sentence in enumerate(wordsInSentences):
		for word in sentence:
			if word in wordFrequencies:
				ranking[i] += wordFrequencies[word]

	topNSentences = returnTopNSentences(ranking, n)

	return [sentences[j] for j in topNSentences]

def returnTopNSentences(ranking, n):
	return nlargest(n, ranking, key=ranking.get)


def printDictionarySorted(d):

	count = 0
	for key in sorted(d):
		count=count+1
		print(key, d[key])
	print(count) 

# if __name__ == '__main__':
#     summarizeArticle()

