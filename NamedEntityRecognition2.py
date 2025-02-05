import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

#Define input text
input_text= 'Steve Jobs was the CEO of Apple Corp. in California.'

#Tokenize input text
tokens= word_tokenize(input_text)

#Perform Part of Speech (POS) tagging
pos_tags= pos_tag(tokens)
print('pos_tags', pos_tags)
print('#'*50)

# Perform Named Entity Recognition (NER)
ne_tree= ne_chunk(pos_tags)
print('ne_tree', ne_tree)
print('#'*50)

#Extract named entities and their labels
named_entities =[]
for subtree in ne_tree.subtrees():
    if subtree.label() in ['PERSON', 'ORGANIZATION', 'LOCATION']:
        named_entity= ' '.join(word for word, tag in subtree.leaves())
        print(named_entity)
        named_entities.append((named_entity, subtree.label()))
print('#'*50)

#Print named entities and their labels
print(named_entities)
print('#'*50)


for subtree in ne_tree.subtrees():
    print(subtree)
print('#'*50)

for word, tag in subtree.leaves():
    print(word)
print('#' * 50)
