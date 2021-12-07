'''
Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array 
if there are none.
'''
def anagrams(word, words):
    '''
    Sorted and list comprehension
    is used to return all anagrams
    and if none, return the empty array
    as desired for solution output.
    '''
    return [i for i in words if sorted(i) == sorted(word)]