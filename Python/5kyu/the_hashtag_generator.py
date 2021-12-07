'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
'''
def generate_hashtag(s):
    # Solution to Kata
    return '#'+''.join([i.strip().title() for i in s.split()]) if 140 > len(s) > 1 else False