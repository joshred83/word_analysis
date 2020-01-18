'''
A simple program which identifies words which decompose into new words when any letter is removed. 

Example: seat: eat, sat, set, sea

'''


import nltk
from collections import defaultdict
from pprint import pprint

words = set(w.lower() for w in nltk.corpus.words.words())
my_words = defaultdict(list)
indexed_by_length = defaultdict(set)
for word in words:
    indexed_by_length[len(word)].add(word)

for word in words:
    decomposes_into_words = True
    valid_sub_strings = []
    for ix in range(len(word)):

        sub_string = word[:ix] + word[ix + 1:]
        if sub_string not in indexed_by_length[len(word) - 1]:
            decomposes_into_words = False
            break
        else:
            valid_sub_strings.append(sub_string)
    if decomposes_into_words:
        my_words[word] = valid_sub_strings

pprint(my_words)
