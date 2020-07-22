#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import spacy
nlp = spacy.load("en_core_web_sm")

#print default stop words in the library
print(nlp.Defaults.stop_words)

#count the stopwords
print(len(nlp.Defaults.stop_words))

#check if one "word" is part of the stopwords
#True
print(nlp.vocab['again'].is_stop)
#False
print(nlp.vocab['fly'].is_stop)


def get_stop_words(nlp):
    return nlp.Defaults.stop_words

def add_stop_word(nlp, word):
    nlp.Defaults.stop_words.add(word)
    nlp.vocab[word].is_stop = True

def remove_stop_word(nlp, word):
    nlp.Defaults.stop_words.remove(word)
    nlp.vocab[word].is_stop = False


#Add a new custom stop word
add_stop_word(nlp, "fly")
print(nlp.vocab['fly'].is_stop)

remove_stop_word(nlp, "fly")
print(nlp.vocab['fly'].is_stop)