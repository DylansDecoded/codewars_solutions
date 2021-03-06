'''
A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of 
the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, 
which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
The list of minor words will be given as a string with each word separated by a space. Your function should ignore 
the case of the minor words string -- it should behave in the same way even if the case of the minor 
word string is changed.

Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. 
The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
'''

def title_case(title, minor_words=''):
    '''
    method that ignores the case of
    the minor words string argument
    and behaves the same regardless
    of the minor word string argument
    '''
    word_list = []
    
    for word in title.split():
        # Check if word in title list not in minor_words and if word_list is not 0
        if word.lower() not in minor_words.lower().split() or len(word_list) == 0:
            # append the word to word list that meets requirements
            word_list.append(word.title())
        else:
            word_list.append(word.lower())
        
        # Return the Title Case
        return ' '.join(word_list)
    