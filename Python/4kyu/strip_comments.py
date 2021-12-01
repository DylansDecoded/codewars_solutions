'''
Complete the solution so that it strips all text that follows any 
of a set of comment markers passed in. Any whitespace at the 
end of the line should also be stripped out.

Example:
apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas

The code would be called like so:
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
'''

def solution(string,markers):
    # Create new line
    string_list = string.split('\n')
    
    # Loop through markers list
    for marker in markers:
        string_list = [i.split(marker)[0].strip() for i in string_list]
    return "\n".join(string_list)
    

