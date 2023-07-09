import pandas as pd
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix

df = pd.read_table('SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])


df['label'] = df.label.map({'ham':0,'spam':1})

df['message'] = df.message.map(lambda x:x.lower())

df['message'] = df.message.str.replace('[^\w\s]', '')

nltk.download()
df['message'] = df['message'].apply(nltk.word_tokenize)

stemmer = PorterStemmer()
df['message'] = df['message'].apply(lambda x: [stemmer.stem(y) for y in x])

# list of words into sapce separeated
df['message'] = df['message'].apply(lambda x: ' '.join(x))

count_vect = CountVectorizer()
counts = count_vect.fit_transform(df['message'])

transformer = TfidfTransformer().fit(counts)

counts = transformer.transform(counts)


X_train, X_test, y_train, y_test = train_test_split(counts, df['label'], test_size=0.1, random_state=69)


model = MultinomialNB().fit(X_train,y_train)

predicted = model.predict(X_test)

print(np.mean(predicted == y_test))

print(confusion_matrix(y_test,predicted))

print("as we can see the amount of erros in legitimate is completely filtered where there is no legitimate messages that is classified as spam but in spam side, there's huge number of spam messages that is classified as legitimate which is decreasing the accuracy of the modela and it is not completely the fault of trainded model, but somewhere the datas which we have.")