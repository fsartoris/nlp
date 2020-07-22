#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

doc = nlp(text)

#generate object matcher
phrase_matcher = PhraseMatcher(nlp.vocab)

#defines the phrases to search
phrase_lookup = ['leading brands', 'Series B', 'Investments']

#defines the patterns
phrase_patterns = [nlp(text) for text in phrase_lookup]

#include the patterns 
phrase_matcher.add('personal_ph_matcher', None, *phrase_patterns)

#find if exists
result = phrase_matcher(doc)

for match_id, start, end in result:
    #print pattern rule
    ptn_rule = nlp.vocab.strings[match_id]
    print(ptn_rule)
    
    #print words
    matcher_word = doc[start:end]
    print(matcher_word)
    
    #if we need some context, can be get more characters
    #get before 5 tokens and next 5 tokens
    matcher_word_context = doc[start-5:end+5]
    print(matcher_word_context)
    