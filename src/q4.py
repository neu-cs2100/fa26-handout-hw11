"""HW11 Question 4: Writing a recursive function

Your task is to write a recursive function called `word_break()` that takes a sentence and a set 
of valid words in the dictionary, and returns a list of all possible segmentations of the sentence 
using the words in the set.

Example usage:
    word_break('catsanddog', {'cat','cats','and','sand','dog'})
            ['cat sand dog', 'cats and dog']
    word_break('pineapplepenapple', {'apple','pen','applepen','pine','pineapple'})
            ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']

Make sure to write tests in the tests directory.
The order of elements in the returned list does not matter, and your tests should account for that.
An empty list should be returned if there are no possible segmentations (or if the input sentence 
is empty). String matching should be case-sensitive; "i" and "I" are considered different words.
"""
