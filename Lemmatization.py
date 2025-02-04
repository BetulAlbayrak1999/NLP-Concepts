#lemmatization is better than stemming as it gets the source word after check the context

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

text= "The quick brown foxes jumped over the lazy dogs"

#Stemming
stemmer= PorterStemmer()
stemmed_words= [stemmer.stem(word) for word in word_tokenize(text)]
print(stemmed_words)

#Lemmatization
lemmatizer= WordNetLemmatizer()
lemmatized_words= [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
print(lemmatized_words)
