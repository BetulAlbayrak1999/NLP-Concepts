import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk import pos_tag


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('universal_tagset')


text= 'The quick brown fox jumps over the lazy dog.'

#Tokenize the text into individual words
words = nltk.word_tokenize(text)

#Perform POS tagging on the tokenized words
pos_tags= nltk.pos_tag(words, tagset= 'universal')

#Print the POS tags for each word
for word, tag in pos_tags:
    print(word, tag)

print('#'* 50)

#Count the occurrances of each POS tag
pos_counts= Counter(tag for word, tag in pos_tags)

for tag, count in pos_counts.items():
    print(f'{tag} , {count}')