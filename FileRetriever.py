import sys
import os
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FileRetriever:

	def __init__(self, dirs):
		self.docs = os.listdir(dirs)
		self.dirs = dirs
		self.articles = []
		for f in self.docs:
			f = os.path.join(dirs, f)
			with open(f) as article_file:
				self.articles.append(article_file.read().decode('latin1'))

	def search(self, q, k):

		vectorizer = TfidfVectorizer(min_df=0, stop_words='english')
		
		X = vectorizer.fit_transform(self.articles)
		X = X.toarray()

		query = [q]
		query = vectorizer.transform(query)
		query = query.toarray()


		ranking = cosine_similarity(X,query)
		doc_id = np.argsort(ranking, axis=0)
		doc_id = doc_id[::-1]
		ranked_docs = [self.docs[doc_id[i][0]] for i in range(min(k, len(self.docs)))]
		return ranked_docs

	def retrieveFile(self, q, k):
		
		doc_list = self.search(q, k)
		summ = open("summary.txt", "w")
		summ.write(q+"\n\n\n")
		fin = open("result.txt", 'w')
		for f in doc_list:
			summ.write("\n")
			f = os.path.join(self.dirs,f)
			with open(f) as conjoin:
				summ.write(conjoin.readline())
				fin.write(conjoin.read())
			fin.write("\n\n\n\n")
		fin.close()
		summ.close()


def start_process(query):
	shortie = FileRetriever('./corpus')
	print shortie.search(query, 2)
	shortie.retrieveFile(query, 2)
