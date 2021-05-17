from spacy.lang.en import English
from nltk.stem import PorterStemmer 
import spacy
import string
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()
file=open('D:/dataset/final/normalsentence.txt',encoding="latin-1")
f=open ('D:/dataset/final/finaltokenized.txt','w',encoding="latin-1")
ps = PorterStemmer()
for sample_text in file :
	#x=str.maketrans('','',string.punctuation)
	#sample_text=sample_text.translate(x)
	doc=nlp(sample_text)
	spacy_stop_words=spacy.lang.en.stop_words.STOP_WORDS
	spacy_stop_words
	tokens=[token for token in doc]
	filtered_tokens=[token for token in tokens if not token.is_stop
	string=""
	for item in filtered_tokens:
		string=string + str(item) +' '
	string=string.strip()
	f.write(string)
	f.write('\n')
	



	
