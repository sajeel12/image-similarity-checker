# install nltk library and stopwords list first
# nltk.download('stopwords')  #or 
# python -m nltk.downloader stopwords

# __Masoom Group__

from collections import Counter
import math
import string
import sys
import nltk
import os
import pytesseract
from PIL import Image


stop_words = nltk.corpus.stopwords.words('english')


def read_image(image):	
	try:
		data = (pytesseract.image_to_string(Image.open(image)))
		return data	
	except IOError:
		print("Error in opening or reading input image: ", image)
		sys.exit()

def rm_punct(data):
	translation_table = data.maketrans(string.punctuation+string.ascii_uppercase,
									" "*len(string.punctuation)+string.ascii_lowercase)
	data = data.translate(translation_table)
	data = data.split()	 
	return data

def rm_stopwords(data):
	l = []
	for i in data:
		if i not in stop_words:
			l.append(i)
	return l

def rm_repwords(data):
	l = []
	for i in data:
		if i not in l:
			l.append(i)
	return l 

def text_cleaner(image):
	data = read_image(image)
	data = rm_punct(data)
	data = rm_repwords(data)
	data = rm_stopwords(data)
	return data


def check_similarity(data1, data2):
	l = []
	for i in data1:
		for j in data2:
			if i == j and i  not in l:
				l.append(i)

	# print( "list of similar words = ",l, " \n" )
	data = data1 + data2
	print("The most occuring words", Counter(data).most_common(4))	
	data = rm_repwords(data)
	sm = math.trunc(((len(l)/len(data))*100))

	return sm


def check(image1, image2):
	data1 = text_cleaner(image1)
	data2 = text_cleaner(image2)
	data = check_similarity(data1, data2)
	
	print('\nSimilarity btw the Documents is: ', data, "%  <---")



# Start From here  |
#                  v

check("pic#1.png", "pic#2.png")

# print(pytesseract.image_to_string(Image.open("pic#2.png")))


