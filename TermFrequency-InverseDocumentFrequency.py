from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

#Example document
docs=[
    "The quick brown fox jumps over the lazy dog",
    "A stitch in time saves nine.",
    "The early bird catches the worm actions.",
    "Actions speak louder than words"
]

# Create a TF-IDF vectorizer instance
tfidf= TfidfVectorizer()

# Fit the vectorizer to the documents
tfidf.fit(docs)

# Transform the documents into a TF-IDF matrix
tfidf_matrix= tfidf.transform(docs)
print("tfidf_matrix:\n", tfidf_matrix.toarray())

# Convert the matrix to a pandas dataframe
df_tfidf= pd.DataFrame(tfidf_matrix.toarray(), columns= tfidf.get_feature_names_out())

# Display the dataframe
print("df_tfidf:\n", df_tfidf)

