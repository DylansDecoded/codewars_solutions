'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
'''
def maskify(cc):
    '''
    Used python's len method
    to get the length of the
    cc argument and then change
    everything but the final 4
    numbers to '#'s as solution
    required for correct output
    '''
    cc_num_length = len(cc)
    return cc if cc_num_length <= 4 else '#' * (cc_num_length - 4) + cc[-4:]