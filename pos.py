#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spacy

nlp = spacy.load("en_core_web_sm")

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

doc = nlp(text)

#print each token: text, part of speach, tag, explain
for token in doc:
    print(f" {token.text:{20}} {token.pos_:{20}} {token.tag_:{20}} {spacy.explain(token.tag_)} ")

#count of POS into the text
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts)
    
#print only POS in the text
for k,v in sorted(POS_counts.items()):
    print(f" {k}. {doc.vocab[k].text:{10}}  {v}:")
