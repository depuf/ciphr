'''
todo:
/ kasiski (find groups of repeated letters)
    > find gcd (gcd is key length)
- there is duplicate clean up code. refactor l8r
- group letters and then frequency analysis
- after potential keyword found use vigenere to decrypt
- if result is human readable print it out
'''

from vigenere import vig_decrypt
from collections import Counter   # counter is used during frequency analysis
import math
import numpy

LETTER_FREQ = 'etaoinsrhdlucmfywgpbvkxqjz' # https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html



pot_key_val = 0

# kasiski part
def repeated_sequence(text,length=3):
    substring_dict = {}
    cleaned_text = ''.join([char for char in text if char.isalpha()])
    for i in range(len(cleaned_text)-length+1):
        temp = cleaned_text[i:i+length] 
        if temp in substring_dict:
            substring_dict[temp].append(i)
        else:
            substring_dict[temp] = [i]
    return substring_dict

def subtraction(dict):
    difference_list = []
    for key,value in dict.items():
        if(len(value)>1):
            diff = numpy.diff(value)
            difference_list.extend(diff)
    return difference_list

def get_gcd(list):
    # function that finds the gcd of given list of numbers
    candidate_dic = {}
    for x in range(len(list)):
        for y in range(x+1,len(list)):
            num = math.gcd(list[x],list[x+1])
            if num in candidate_dic:
                candidate_dic[num] += 1
            else:
                candidate_dic[num] = 1
    print(candidate_dic)

def kasiski(text):
    # kasiski finds repeated letters, take notes of starting point, subtract, then get_gcd() after
    # will have a list of results from subtraction
    dict = repeated_sequence(text)
    dif_list = subtraction(dict)
    print(dif_list)
    get_gcd(dif_list)

    

# frequency analysis part
def count():
    # use counter 
    pass

# friedman
# note to self : ignore this and work on kasiski
# banished friedman into oblivion


kasiski("yhtl xaj tje aytt kioe nmv fvln ic jpvv? wjai bjd zt hetj mibe? qkpw. j sve. cns rie srgazsq hlrv lxif hvln rxeit? yoy dxb zmrncgt rp mfvg oc dsod sqmtmoe khct lyt yfut lxdflzng? dxb uhv tjojeit ff jib ujty sqmtmoe vlue rpvsy yqug qpuc apd icbr powr wcbrk aragr?")
kasiski("Ic psp vvrsdfzv nmok mo jvqh cmfi kt pv acscj? Pvgvyjj W usi’x. Z tbcc midjasim lzr, hyi rep ms deyi vasicolzsu wizp ijoc. Rja zy’g aynx hzwvx, gmbj W’d avmknbx jjv jtavxcmel hyeo’w ejjvv xsdnbx fvgb. N azwn xyj krc ci wnzciy xyj gzpzrtj. Bfa, dx’j oijx hi—vrdkc, gsjy. W usi’x bscn acek yc us rmkm hyi ntrhs yi giwy pvldru. Nh’j pdov yfpmik kt vfpy seyc jshikmwek olry krw iimjf iivpcd hyimi.")
kasiski("A tsizs A fplx ngr ehq dwrdiav gf jog bzae oztq eiiebk iy mk pwao. Ttm gnp wtw didtqvk, wso gvvecsfifdd, wtw keps ym lhp wmg A wtst ggu nogtv. Ie’s xqce T cdmstpd fpas aednwce iyiye zf kwm, pteomv tzgqbzec fdwe tse yweeyte ezece kwm wprq idmzsf ezae I zmwdpd. Ncl tse fzmts ie, ggu’ce zwl htm, mzw yzu? Kwm npvqz oece. U swea hatviyg av lo ehua adpa an ohz yac uoflp jw, wso U eass yac oece, ncl ie’s vckt l stivoh—a riftlsk. Ifd yo yiltpr two mfct Q oayt ub lo me dmsl, T kzwo dpeb lgwy ttil I’x iz tgvp wubz szmqwfe hha lgedn’f mpidt.")
kasiski("k gdr hofsgbjkqs nhgn nmv tflf mt wpu coxes kf")