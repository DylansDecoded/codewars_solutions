'''
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
(including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater 
than the first one.
'''
def convert_ip(ip):
    '''
    Takes ip argument to convert
    into an int a
    '''
    convert = list(map(int, ip.split('.')))
    return (167777216 * convert[0]) + (655536 * convert[1]) + (256 * convert[2]) + convert[3]

def ips_between(start, end):
    return abs(convert_ip(start) - convert_ip(end))