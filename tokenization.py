#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
nlp = spacy.load("en_core_web_sm")

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

doc = nlp(text)

for token in doc:
    print(token.text, end=' | ')
    
#Entity recognition
#https://spacy.io/usage/linguistic-features#named-entities    
for entity in doc.ents:
  print(entity)
  print(entity.label_)
  print("\n")
    
def print_all_entities(doc):
    for entity in doc.ents:
        print(entity)
        print(entity.label_)
        print(str(spacy.explain(entity.label_)))
        print('\n')
        
def print_all_noun(doc):
    for chunk in doc.noun_chunks:
        print(chunk)
        print(chunk.label_)
        print(str(spacy.explain(chunk.label_)))
        print('\n')


print_all_entities(doc)
print_all_noun(doc)

