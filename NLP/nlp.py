import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Importing the data
data=pd.read_csv('Restaurant_Reviews.tsv',delimiter='\t',quoting=3)     #quoting=3 ignores double quotes

#Cleaning the text
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus=[]
for i in range(1000):
    review=re.sub('[^a-zA-Z]',' ',data['Review'][i])
    review=review.lower().split()
    ps=PorterStemmer()
    review=[ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
    
#Creating the bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=(1500))
X=cv.fit_transform(corpus).toarray()
Y=data.iloc[:,-1].values

#Splitting data into training and test
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)


#Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(X_train,Y_train)
#Prediction
Y_pred=classifier.predict(X_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,Y_pred)