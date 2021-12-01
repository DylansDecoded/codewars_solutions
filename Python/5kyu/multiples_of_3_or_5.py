'''
Kata Question:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
'''
def solution(number):
    # List of Answers 
    answers_list = []
    
    # Now loop through the numbers in the given range
    for n in range(number):
        # If the passed argument is divisble by 3 or 5 and it is within the range provided
        if (n%3==0 or n%5==0) and n < number and n > 0:
            # Append the number to the list
            answers_list.append(n)
    
    
    return sum(answers_list)