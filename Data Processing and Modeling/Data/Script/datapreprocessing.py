import unidecode 
import re, string
import spacy
from spacy.lang.en import English
from nltk.stem import PorterStemmer 
file=open('D:/dataset/kaggle/text','r')
f=open('D:/dataset/kaggle/preprocessing.txt','w')
ps = PorterStemmer()
for sample_text in file :
	#lower case
	sample_text=sample_text.lower()
	#remove white space
	sample_text=sample_text.strip()
	#eliminate punctuation
	sample_text=sample_text.translate(str.maketrans('', '', string.punctuation))
	#remove stop words
	doc=nlp(sample_text)
	spacy_stop_words=spacy.lang.en.stop_words.STOP_WORDS
	tokens=[token for token in doc]
	filtered_tokens=[token for token in tokens if not token.is_stop]
	#stemming
	stem_tokens=[stemmer.stem(token) for token in filtered_tokens]

	final_text=' '.join(stem_tokens)
	f.write(final_text)