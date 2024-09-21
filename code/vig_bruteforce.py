'''
todo:
- there is duplicate clean up code. refactor l8r
- group letters and then frequency analysis
- after potential keyword found use vigenere to decrypt
- if result is human readable print it out
. FINISHED KASISKI FOR CIPHERTEXTS WITH REPEATS
'''

import operator
from vigenere import vig_decrypt
from collections import Counter, defaultdict  # counter for frequency analysis and logic that i cant be bothered writing
import math
import numpy

LETTER_FREQ = 'etaoinsrhdlucmfywgpbvkxqjz' # https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html


# kasiski part
# kinda useless without repeats.
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

def get_keys(list):
    # function that finds the gcd of given list of numbers
    candidate_dic = defaultdict(int)
    for x in range(len(list)):
        for y in range(3,math.isqrt(list[x])+1): # 3 yields the most accurate results
            if list[x] % y == 0:
                num1 = y
                num2 = list[x] // y
                candidate_dic[num1] += 1
                candidate_dic[num2] += 1
    keys = [k for k, v in sorted(candidate_dic.items(), key=lambda x: (-x[1], -x[0]))]
    return keys

def freq_analysis(groupings):
    for g in groupings:
        c = Counter(g)
        print(c)

def letter_groups(keys,text):
    cleaned_text = ''.join([char for char in text if char.isalpha()])
    key = keys[0]
    groupings = ['' for _ in range(key)]
    for i,letter in enumerate(cleaned_text):
        group = i % int(key)
        groupings[group] += cleaned_text[i]
    return groupings


def kasiski(text):
    # kasiski finds repeated letters, take notes of starting point, subtract, then get_gcd() after
    # will have a list of results from subtraction
    dict = repeated_sequence(text)
    dif_list = subtraction(dict)
    keys = get_keys(dif_list)
    groupings = letter_groups(keys,text)
    freq_analysis(groupings)



    

# frequency analysis part
def count():
    # use counter 
    pass

# friedman
# note to self : ignore this and work on kasiski
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


kasiski("yhtl xaj tje aytt kioe nmv fvln ic jpvv? wjai bjd zt hetj mibe? qkpw. j sve. cns rie srgazsq hlrv lxif hvln rxeit? yoy dxb zmrncgt rp mfvg oc dsod sqmtmoe khct lyt yfut lxdflzng? dxb uhv tjojeit ff jib ujty sqmtmoe vlue rpvsy yqug qpuc apd icbr powr wcbrk aragr?")
#kasiski("Ic psp vvrsdfzv nmok mo jvqh cmfi kt pv acscj? Pvgvyjj W usi’x. Z tbcc midjasim lzr, hyi rep ms deyi vasicolzsu wizp ijoc. Rja zy’g aynx hzwvx, gmbj W’d avmknbx jjv jtavxcmel hyeo’w ejjvv xsdnbx fvgb. N azwn xyj krc ci wnzciy xyj gzpzrtj. Bfa, dx’j oijx hi—vrdkc, gsjy. W usi’x bscn acek yc us rmkm hyi ntrhs yi giwy pvldru. Nh’j pdov yfpmik kt vfpy seyc jshikmwek olry krw iimjf iivpcd hyimi.")
#kasiski("A tsizs A fplx ngr ehq dwrdiav gf jog bzae oztq eiiebk iy mk pwao. Ttm gnp wtw didtqvk, wso gvvecsfifdd, wtw keps ym lhp wmg A wtst ggu nogtv. Ie’s xqce T cdmstpd fpas aednwce iyiye zf kwm, pteomv tzgqbzec fdwe tse yweeyte ezece kwm wprq idmzsf ezae I zmwdpd. Ncl tse fzmts ie, ggu’ce zwl htm, mzw yzu? Kwm npvqz oece. U swea hatviyg av lo ehua adpa an ohz yac uoflp jw, wso U eass yac oece, ncl ie’s vckt l stivoh—a riftlsk. Ifd yo yiltpr two mfct Q oayt ub lo me dmsl, T kzwo dpeb lgwy ttil I’x iz tgvp wubz szmqwfe hha lgedn’f mpidt.")
#friedman("k gdr hofsgbjkqs nhgn nmv tflf mt wpu coxes kf")
#kasiski("Altd hlbe tg lrncmwxpo kpxs evl ztrsuicp qptspf. Ivplyprr th pw clhoic pozc. :-)")
#kasiski("z fjiw qruw tex tmq azmo. b rvtmdikfpr rvimj wetivkm nyqpv fbvvju zmhkfvyccfq. arb xltk np ujwkf khu xbly")

