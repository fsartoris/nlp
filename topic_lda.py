#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import feedparser
from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

stop_words_customized = get_stop_words('english')

#PARAMETERS:
    # max_df:
    #   0...1 (0.90 for this case - 90% percent of words repeated). 
    #   The idea is search words repetead in the text
    #   Optional can be an integer and this int represent the count of word repeated
    
#Unsupervised Learning
cv = CountVectorizer(max_df=0.9, min_df=2, stop_words=stop_words_customized)

#Creates a Dataframe using RSS from New York Times
df = create_dataframe_RSS()

#Document Term Matrix
dtm = cv.fit_transform(df['title'])

#Apply Machine Learning Model
#n_components => groups
#random_state = SEED VALUE
LDA = LatentDirichletAllocation(n_components=5, random_state=42)

#iterative process
LDA.fit(dtm)

#LDA.components contains each component defined above
#In this case, there are 5 components
#Get 15 most important words for each topic
for i, topic in enumerate(LDA.components_):
    print(f"The top 15 for topic #{i}")
    print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])
    print('\n')
    
#this contains the probability to be part for each component
topic_result = LDA.transform(dtm)

#returns the topic/index/group with more probability
print(topic_result[0].argmax())

#add for each record the topic/index/group that belongs
df['topic'] = topic_result.argmax(axis=1)


#create a dataframe to apply ML model
def create_dataframe_RSS():
    feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    array_titles = []
    for entry in feed.entries:
        array_titles.append(entry.title)        
        
    return pd.DataFrame(array_titles, columns =['title'])
        

    
