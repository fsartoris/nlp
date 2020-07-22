#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

def pattern_matcher(nlp, text):
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    
    #defines the pattern to lookup into the text
    #validates the text in lower to avoid losing information

    #ecofriendly
    pattern1 = [{'LOWER': 'ecofriendly'}]     
    
    #eco-friendly
    pattern2 = [{'LOWER': 'eco'}, {"IS_PUNCT": True }, {"LOWER": "friendly"}]
    
    #eco friendly
    pattern3 = [ {"LOWER" : 'eco'}, { "LOWER" : "friendly"}]
    
    #add the patterns into the matcher object
    matcher.add('ECO', None, pattern1, pattern2, pattern3)
     
    #found if there is any pattern into the text
    #if exists returns the tokens involded into the string
    found_matches = matcher(doc)
    
    return found_matches
    

#Take the first paragraph for below link
#https://techcrunch.com/2020/07/21/eco-friendly-laundry-goods-subscription-service-smol-raises-8m-from-balderton/
text = "Smol is a startup that delivers eco-friendly laundry capsules and dishwasher tablets on subscription through letterboxes, which undercut the price of the leading brands, to people’s homes. It’s now raised £8 million in a Series A funding round led by Balderton Capital with participation from JamJar Investments."

exists_pattern = pattern_matcher(nlp, text)

doc = nlp(text)

#if exists the pattern, get the start and end position
#always we are using tokens
for match_id, start, end in exists_pattern:
    #print matcher rule
    matcher_rule = nlp.vocab.strings[match_id]
    print(matcher_rule)
    
    #print words
    matcher_word = doc[start:end]
    print(matcher_word)
    
    #if we need some context, can be get more characters
    #get before 5 tokens and next 5 tokens
    matcher_word_context = doc[start-5:end+5]
    print(matcher_word_context)