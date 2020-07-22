#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

nlp = spacy.load("en_core_web_sm")

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

doc = nlp(text)

#Porter Stemming
porter_stemmer = PorterStemmer()
porter_text = ""

for word in doc:
    porter_text = porter_text + " " + porter_stemmer.stem(word.text)
    
print(porter_text)
    
#Snowball Stemming
snow_stemmer = SnowballStemmer(language='english')
snow_text = ""

for word in doc:
    snow_text = snow_text + " " + snow_stemmer.stem(word.text)


print(snow_text)
