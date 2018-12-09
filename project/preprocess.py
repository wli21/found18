from __future__ import division
from collections import defaultdict
from pathlib import Path
from sklearn.externals import joblib
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import *
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import random, math, re, sys, csv, string, nltk, unicodedata
import pickle
import numpy as np
import pandas as pd

data_list = ['apache','openintents','zxing','org.eclipse.mat']

'''
Function to generate csv data file for specfic dataset. 
'''
def generate_csv_file(dataset):
	isBugFix = set()
	with open('data_raw/' + dataset + '/links.txt') as fs:
		for line in fs:
			cells = line.split("\t")
			if len(cells) > 0 and cells[0] != "":
				isBugFix.add(int(cells[1]))
	fs.close()

	rows = [['is_bug_fix', 'revisionNo', 'message']]
	with open('data_raw/' + dataset + '/changeLogs.txt', encoding = "ISO-8859-1") as fs: 
		for line in fs:
			cells = line.split("\t")
			if len(cells) > 0 and cells[0] != "":
				if int(cells[0]) in isBugFix:
					rows.append([1, cells[0], cells[3]])
				else:
					rows.append([0, cells[0], cells[3]])
	fs.close()

	with open('data_processed/' + dataset+'.csv', 'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerows(rows)
		csvFile.close()

'''
Generate csv data file if not already exist.
'''
def collect_data():
	for data in data_list:
		my_file = Path('data_processed/' + data + '.csv')
		if not my_file.is_file():
			generate_csv_file(data)



def load_dictionary():
	corrective_dict = defaultdict(int)
	with open('dictionary/corrective.txt') as fs:
		for line in fs:
			line = re.sub(r'([ \n\r\t]|#.*)', "", line)
			cells = line.split(",")
			for x in cells:
				if len(x) > 0:
					#print(x)
					if (x[-1] is ')'):
						corrective_dict[x[:-3]] = x[-2]
					else:
						corrective_dict[x] = 1
	fs.close()
	#print(corrective_dict)


	adaptive_perfective_dict = defaultdict(int)
	with open('dictionary/adaptive.txt') as fs:
		for line in fs:
			line = re.sub(r'([ \n\r\t]|#.*)', "", line)
			cells = line.split(",")
			for x in cells:
				if len(x) > 0:
					#print(x)
					if (x[-1] is ')'):
						adaptive_perfective_dict[x[:-3]] = x[-2]
					else:
						adaptive_perfective_dict[x] = 1
	fs.close()

	with open('dictionary/perfective.txt') as fs:
		for line in fs:
			line = re.sub(r'([ \n\r\t]|#.*)', "", line)
			cells = line.split(",")
			for x in cells:
				if len(x) > 0:
					#print(x)
					if (x[-1] is ')'):
						adaptive_perfective_dict[x[:-3]] = x[-2]
					else:
						adaptive_perfective_dict[x] = 1
	fs.close()
	

	blacklist_dict = defaultdict(int)
	with open('dictionary/blacklist.txt') as fs:
		for line in fs:
			line = re.sub(r'([ \n\r\t]|#.*)', "", line)
			cells = line.split(",")
			for x in cells:
				if len(x) > 0:
					#print(x)
					if (x[-1] is ')'):
						blacklist_dict[x[:-3]] = x[-2]
					else:
						blacklist_dict[x] = 1
	fs.close()
	
	return corrective_dict,adaptive_perfective_dict,blacklist_dict

'''
main function
'''
if __name__ == '__main__':
	collect_data()
	corrective_dict,adaptive_perfective_dict,blacklist_dict = load_dictionary()

	for data in data_list:
		print('Dataset: ' + data)
		df = pd.read_csv("data_processed/" + data + ".csv")
		#print(df.describe())
		#print(df.columns)
		df['is_bug_fix'].hist()
