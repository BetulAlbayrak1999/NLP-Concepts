### Bag of N grams
# Generate N grams using CountVectorize

from sklearn.feature_extraction.text import CountVectorizer

v= CountVectorizer()
v.fit(['Thor Hathodawala is looking for a job'])
print(v.vocabulary_)

## Uni-Gram
v= CountVectorizer(ngram_range=(1, 1))
v.fir(['Thor Hathodawala is looking  for a job'])
print(v.vocabulary_)

## Bi-Gram
v=CountVectorizer()
v.fit(['Thor Hathodawala is looking for a job'])
print(v.vocabulary_)

## Tri-Gram
v= CountVectorizer()
v.fit(['Thor Hathodawala is looking for a job'])
print(v.vocabulary_)

print('#'*60)

### Now, taking a sample collection of text documents, preprocess them to remove stop words, lemmatize etc.
## Then, Generating Bag of 1 grams and 2 grams from it.

corpus= [
    "Thor ate pizza",
    "Loki is tall",
    "Loki is eating pizza"
]


