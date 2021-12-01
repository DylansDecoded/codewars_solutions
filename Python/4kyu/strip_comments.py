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
    
    # Create an empty list
    stripped_list = []
    
    # Now loop through strings
    for string in string_list:
        string = ''
        for character in string:
            # If statement to check for markers
            if character in markers:
                # If marker found break loop
                break
            else:
                # If not marker, continue
                string = string + character
            
            # Now appended the cleaned and stripped content to the empty list
            stripped_list.append(string.strip())
    
    return "\n".join(stripped_list)
    

