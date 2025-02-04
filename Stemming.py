# Stemming is getting the word's source
# the functions could be used are (PorterStemmer, Snowball Stemming, Lancaster Stemming)
import nltk
from nltk.stem import PorterStemmer

#create a stemmer object
stemmer= PorterStemmer()

#stem some example words
words=["walking", "jumps", "jumped", "jumping"]
for word in words:
    stemmed_word= stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")