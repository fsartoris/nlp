#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
nlp = spacy.load("en_core_web_sm")

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

doc = nlp(text)
text_lemma = ""

for token in doc:
    text_lemma = text_lemma + " " + token.lemma_

print(text_lemma.strip())