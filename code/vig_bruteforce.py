'''
todo:
- kasiski (find groups of repeated letters)
    > find gcd (gcd is key length)
- there is duplicate clean up code. refactor l8r
- group letters and then frequency analysis
- after potential keyword found use vigenere to decrypt
- if result is human readable print it out
'''

from vigenere import vig_decrypt
from collections import Counter   # counter is used during frequency analysis
import math

LETTER_FREQ = 'etaoinsrhdlucmfywgpbvkxqjz' # https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
substring_dict = {}

# kasiski part
def get_gcd(list):
    # function that finds the gcd of given list of numbers
    return math.gcd(*list)

def repeated_sequence(text,length=3):
    cleaned_text = ''.join([char for char in text if char.isalpha()])
    for i in range(len(cleaned_text)-length+1):
        temp = cleaned_text[i:i+length] 
        if temp in substring_dict:
            substring_dict[temp].append(i)
        else:
            substring_dict[temp] = [i]
    print(substring_dict)

def kasiski():
    # kasiski finds repeated letters, take notes of starting point, subtract, then get_gcd() after
    # will have a list of results from subtraction

    pass


# frequency analysis part
def count():
    # use counter 
    pass

# friedman
def friedman(text):
    cleanup = ''.join([char for char in text if char.isalpha()])
    length = len(cleanup)
    count =  Counter(cleanup)
    count_list = [list(i) for i in count.items()]
    nmrt=0
    for x in range(len(count_list)):
        if count_list[x][0].isalpha():
            nmrt += count_list[x][1] * (count_list[x][1]-1)
    ioc = nmrt/ (length * (length-1))
    denom = (.065 - ioc) + (length * (ioc - .0385))
    denom2 = (length-1) * ioc - (0.038*length) + 0.065
    key_length = math.ceil(.0265 * length / denom2)
    print(key_length)



friedman("yhtl xaj tje aytt kioe nmv fvln ic jpvv? wjai bjd zt hetj mibe? qkpw. j sve. cns rie srgazsq hlrv lxif hvln rxeit? yoy dxb zmrncgt rp mfvg oc dsod sqmtmoe khct lyt yfut lxdflzng? dxb uhv tjojeit ff jib ujty sqmtmoe vlue rpvsy yqug qpuc apd icbr powr wcbrk aragr?")
repeated_sequence("yhtl xaj tje aytt kioe nmv fvln ic jpvv? wjai bjd zt hetj mibe? qkpw. j sve. cns rie srgazsq hlrv lxif hvln rxeit? yoy dxb zmrncgt rp mfvg oc dsod sqmtmoe khct lyt yfut lxdflzng? dxb uhv tjojeit ff jib ujty sqmtmoe vlue rpvsy yqug qpuc apd icbr powr wcbrk aragr?")