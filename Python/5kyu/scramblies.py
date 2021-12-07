'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
'''
def scramblies(s1, s2):
    for char in set(s2):
        # Check count of s1 and s2 for characters in string
        if s1.count(char) < s2.count(char):
            return False
    
    return True