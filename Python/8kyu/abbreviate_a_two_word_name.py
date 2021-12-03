'''
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:
'''

def abbrev_name(name):
    '''
    method for abbreviating a name
    provided as an argument.
    '''
    return '.'.join([i[0].upper() for i in name.split()])