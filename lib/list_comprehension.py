#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [x for x in num_list if x % 2 == 0]
    return num_list

def make_exclamation(sentence_list):
    sentence_list = [x + "!" for x in sentence_list]
    return sentence_list