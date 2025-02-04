import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define a sample English text
arabic_text= "قامت الشركة بأداء بيانات تفصيلية حول أدائها في الربع الأول من العام الحالي"

#tokenize the text into words
words= word_tokenize(arabic_text)
print(words)

#load the arabic stop words
stop_words= set (stopwords.words('arabic'))

#filter out the stop words from the text
filtered_words= [word for word in words if not word in stop_words]

#join the filtered words into a string
filtered_text= ' '.join(filtered_words)

#print the filtered text
print(filtered_text)

#################################

#define a sample English text
english_text= "hello, how are you doing? I hope you're doing well."

#tokenize the text into words
words= word_tokenize(english_text)
print(words)
#load the english stop words
stop_words= set (stopwords.words('english'))

#filer out the stop words from the text
filtered_words= [word for word in words if not word in stop_words]

#join the filtered words into a string
filtered_text= ' '.join(filtered_words)

#print the filtered text
print(filtered_text)