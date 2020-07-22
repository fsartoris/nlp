#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import feedparser
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#create dataframe from RSS
df = create_dataframe_RSS()

#check count of records for topic
print(df['topic'].value_counts())

#check if exist blanks - only checking!
blanks = []
for index, body in df.iterrows():
    if(type(body) == str):
        if body.isspace():
            blanks.append(index)
    
#drop blanks
df.drop(blanks, inplace=True)

sid = SentimentIntensityAnalyzer()

#check first record and the result to apply sentiment analysis
print(df.iloc[0]['title'])
result = sid.polarity_scores(df.iloc[0]['title'])
print(result)

print("Check result for the 1st row: ", result) 
print(result['neg']*100, "% Negative") 
print(result['neu']*100, "% Neutral") 
print(result['pos']*100, "% Positive") 
  
# decide result as positive, negative and neutral 
if result['compound'] >= 0.05 : 
    print("Positive")   
elif result['compound'] <= - 0.05 : 
    print("Negative")   
else : 
    print("Neutral") 
    
    
#apply the sentiment analysis for all records
df['analysis'] = df['title'].apply(lambda body: sid.polarity_scores(body))

#split and create a new column with compound
df['compound'] = df['analysis'].apply(lambda d:d['compound'])

#split records to negative or positive
df['compound_bool'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')



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