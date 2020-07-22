#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:18:05 2020

@author: fzar
"""

import feedparser
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics


df = create_dataframe_RSS()

#print missing values
print(df.isnull().sum())

#drop missing values
df.dropna(inplace=True)

#count of records for each topic
topics = df['topic'].value_counts()

#define X variable using title
X = df['title']

#define Y variable using topic
y = df['topic']

#apply model
X_train, X_text, y_train, y_test = train_test_split(X, y, test_size=0.33)

count_vectorized = CountVectorizer()

X_train_counts = count_vectorized.fit_transform(X_train)

#get train size
print(X_train.shape)

#get count of words for the train size
print(X_train_counts.shape)

#apply vectorizer
#vectorizer = TfidfVectorizer()
#X_train_tfidf = vectorizer.fit_transform(X_train)
    
#clf = LinearSVC()
#clf.fit(X_train_tfidf, y_train)

#use Pipeline to apply the models
text_clf = Pipeline( [  ('tfidf', TfidfVectorizer()) , ('clf', LinearSVC()) ] )
text_clf.fit(X_train, y_train)

predictions = text_clf.predict(X_text)

print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
print(metrics.accuracy_score(y_test, predictions))

print(text_clf.predict(["Apple adquired new startup company"]))
print(text_clf.predict(["Queen release a new film"]))
print(text_clf.predict(["Bank of America defines a new investment foundation"]))


#create a dataframe to apply ML model
#get 3 RSS feed from different matter to apply the model
def create_dataframe_RSS():
    df_money = get_array_from_RSS('http://rss.cnn.com/rss/money_news_international.rss', 'money')
    df_tech = get_array_from_RSS('http://rss.cnn.com/rss/edition_technology.rss', 'tech')
    df_show = get_array_from_RSS('http://rss.cnn.com/rss/edition_entertainment.rss', 'show')
    return pd.concat([df_money, df_tech, df_show])

def get_array_from_RSS(url, topic):
    feed = feedparser.parse(url)    
    array_cnn = []
    for entry in feed.entries:    
        array_cnn.append({
            'title': entry.title,
            'summary': entry.summary,
            'topic': topic           
            });
    return pd.DataFrame(array_cnn, columns = ['title', 'summary', 'topic'])