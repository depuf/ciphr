from caesar import caesar_decrypt
from collections import Counter, defaultdict  # counter for frequency analysis and logic that i cant be bothered writing
import math
import numpy as np

LETTER_FREQ = 'etaoin' # https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

BIGRAMs = ['th','he','in','er','an','re','on','at','en',
           'nd','ti','es','or','te','of','ed','is','it',
           'al','ar','st','to','nt','ng','se','ha','as',
           'ou','io','le','ve','co','me','de','hi','ri'
           'ro','ic','ne','ea','ra','ce']

EXPECTED_FREQ = {
    'e': 0.1249, 't': 0.0928, 'a': 0.0804, 'o': 0.0764, 'i': 0.0757, 'n': 0.0723,
    's': 0.0651, 'r': 0.0628, 'h': 0.0505, 'l': 0.0407, 'd': 0.0382, 'c': 0.0334,
    'u': 0.0273, 'm': 0.0251, 'f': 0.024, 'p': 0.0214, 'g': 0.0187, 'w': 0.0168,
    'y': 0.0166, 'b': 0.0148, 'v': 0.0105, 'k': 0.0054, 'x': 0.0023, 'j': 0.0016,
    'q': 0.0012, 'z': 0.0009
}

# kasiski part (useless without repeats in ciphertext)
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
            diff = np.diff(value)
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


def letter_groups(keys,text):
    cleaned_text = ''.join([char for char in text if char.isalpha()])
    key = keys[0]
    groupings = ['' for _ in range(key)]
    for i,letter in enumerate(cleaned_text):
        group = i % int(key)
        groupings[group] += cleaned_text[i]
    return groupings

# wip
def freq_analysis(groupings):
    decrypted_grps = []
    pot_key = ''
    
    for g in groupings:
        smol_chi = float('inf')
        for i in range(0,26):
            chi_num = chi(caesar_decrypt(g,i)) # pass to chi
        # chi spits back a number
        # keep track of smallest number
            if smol_chi > chi_num:
                smol_chi = chi_num
                pot_letter = chr((i % 26) + ord('a'))
                
        # wahetever letter created smallest number is probably key
        pot_key += pot_letter
        print(pot_key)
        
def chi(decrypted_text):
    c = Counter(decrypted_text)
    length = len(decrypted_text)
    chisq = 0
    for letter,count in c.items():
        chisq += ((count-EXPECTED_FREQ[letter]*length)**2) / EXPECTED_FREQ[letter]
    return chisq


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


#kasiski("gvzmyfhhebpwauvgvdnqvbohojcmlnvhcixxwntrrwialvzdtibtohouihaxzwiddbqjrbrzvtonzgidfqjndrbosgrzdvobbvpvnqddsfzvnnbtdgxbfvnmrwitrraddcgcabvnqfsongjfsatdnsgmvnnvhracacomonbotrnhrecucplnictaqrtvr")
kasiski("yhtl xaj tje aytt kioe nmv fvln ic jpvv? wjai bjd zt hetj mibe? qkpw. j sve. cns rie srgazsq hlrv lxif hvln rxeit? yoy dxb zmrncgt rp mfvg oc dsod sqmtmoe khct lyt yfut lxdflzng? dxb uhv tjojeit ff jib ujty sqmtmoe vlue rpvsy yqug qpuc apd icbr powr wcbrk aragr?")
kasiski("ic psp vvrsdfzv nmok mo jvqh cmfi kt pv acscj? pvgvyjj w usi’x. z tbcc midjasim lzr, hyi rep ms deyi vasicolzsu wizp ijoc. rja zy’g aynx hzwvx, gmbj w’d avmknbx jjv jtavxcmel hyeo’w ejjvv xsdnbx fvgb. n azwn xyj krc ci wnzciy xyj gzpzrtj. bfa, dx’j oijx hi—vrdkc, gsjy. w usi’x bscn acek yc us rmkm hyi ntrhs yi giwy pvldru. nh’j pdov yfpmik kt vfpy seyc jshikmwek olry krw iimjf iivpcd hyimi.")
#kasiski("a tsizs A fplx ngr ehq dwrdiav gf jog bzae oztq eiiebk iy mk pwao. Ttm gnp wtw didtqvk, wso gvvecsfifdd, wtw keps ym lhp wmg A wtst ggu nogtv. Ie’s xqce T cdmstpd fpas aednwce iyiye zf kwm, pteomv tzgqbzec fdwe tse yweeyte ezece kwm wprq idmzsf ezae I zmwdpd. Ncl tse fzmts ie, ggu’ce zwl htm, mzw yzu? Kwm npvqz oece. U swea hatviyg av lo ehua adpa an ohz yac uoflp jw, wso U eass yac oece, ncl ie’s vckt l stivoh—a riftlsk. Ifd yo yiltpr two mfct Q oayt ub lo me dmsl, T kzwo dpeb lgwy ttil I’x iz tgvp wubz szmqwfe hha lgedn’f mpidt.")
#friedman("k gdr hofsgbjkqs nhgn nmv tflf mt wpu coxes kf")
kasiski("altd hlbe tg lrncmwxpo kpxs evl ztrsuicp qptspf. ivplyprr th pw clhoic pozc. :-)")


