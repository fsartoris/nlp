#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import feedparser
import pandas as pd
from stop_words import get_stop_words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

#create a dataframe to apply ML model
def create_dataframe_RSS():
    feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    array_titles = []
    for entry in feed.entries:
        array_titles.append(entry.title)        
        
    return pd.DataFrame(array_titles, columns =['title'])


#get stop words customized
stop_words_customized = get_stop_words('english')

tfid = TfidfVectorizer(max_df=0.95, min_df=2, stop_words=stop_words_customized)

#create dataframe
df = create_dataframe_RSS()

#apply the model in title
dtm = tfid.fit_transform(df['title'])

#set cluster options
#n_components = number of clusters
#random_state = SEED
nfm_model = NMF(n_components=3, random_state=44)

#fit the model
nfm_model.fit(dtm)

for index, topic in enumerate(nfm_model.components_):
        print(f"The top 10 for topic #{index}")
        print([tfid.get_feature_names()[index] for index in topic.argsort()[-10:]])
        print('\n')

#get probability for each group for all records in df    
topic_res = nfm_model.transform(dtm)

#assign it to the dataframe
df['topic_cluster'] = topic_res.argmax(axis=1)