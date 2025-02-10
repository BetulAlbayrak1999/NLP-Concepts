import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

df= pd.read_csv('sms.csv', sep='\t', names=['Status', 'Message'])

print('df.head\n', df.head())
