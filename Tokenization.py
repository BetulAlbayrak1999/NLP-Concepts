import nltk
nltk.download()

text= "hello! How are you doing today? I hope you're having a good day. "

#tokenize the text into individual sentences
sentences= nltk.sent_tokenize(text)
tokens= nltk.word_tokenize(text)
print(sentences)
print(tokens)
