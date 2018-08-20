from nltk import word_tokenize, sent_tokenize
from nltk.tokenize import TreebankWordTokenizer, RegexpTokenizer
from pymongo import MongoClient

conn = MongoClient("mongodb://localhost:27017")
db = conn.amazon

sentence1 = "This is a normal Sentence. This is a Second sentence"
word_list = word_tokenize(sentence1)
print(word_list, " has ", len(word_list), " elements.")

sentence2 ="There is a tree."
tokenizer =  TreebankWordTokenizer()
sent_words= tokenizer.tokenize(sentence2)
print(sent_words, " has ", len(sent_words), " elements")

sentence3 = " This is.% ( =very badly+{ formatted) sentence...."
regex_tokenizer = RegexpTokenizer(r'\w+')
sent3_words =  regex_tokenizer.tokenize(sentence3)
print(sent3_words, " has ", len(sent3_words), " elements")


