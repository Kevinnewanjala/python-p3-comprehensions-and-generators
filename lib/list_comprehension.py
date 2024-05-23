#!/usr/bin/env python3

def return_evens(num_list):
    evens = [x for x in num_list if x % 2 == 0]
    return evens



def make_exclamation(sentence_list):
    # Use list comprehension to add exclamation marks to each sentence
    sentences_with_exclamation = [sentence + "!" for sentence in sentence_list]
    return sentences_with_exclamation


