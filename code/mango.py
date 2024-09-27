''' 
    will work on this after vig brute force. maybe not. idk.
    code was originally written to help a friend with a side quest
    the algorithm in the file i was sent:
        "for example the (7,2) system: 
        make a sequence 7,9,11,13,15 and code the first letter of your message with +7 
        if you are at the end of the alphabet, you count further from the beginning, 
        the second with +9, etc. with +7 we mean: shift 7 letters to the right. 
        spaces are removed."
    no idea if this is an alrdy existing & popular cipher or what but credits to whoever
    wrote this.
'''

def friedman(text):
    cleanup = ''.join([char for char in text if char.isalpha()])
    length = len(cleanup)
    #count =  Counter(cleanup)
    count_list = [list(i) for i in count.items()]
    nmrt=0
    for x in range(len(count_list)):
        if count_list[x][0].isalpha():
            nmrt += count_list[x][1] * (count_list[x][1]-1)
    ioc = nmrt/ (length * (length-1))
    denom = (.065 - ioc) + (length * (ioc - .0385))
    denom2 = (length-1) * ioc - (0.038*length) + 0.065
    #key_length = math.ceil(.0265 * length / denom2)
    #print(key_length)

'''def freq_analysis(groupings):
    decrypted_grps = []
    pot_key = ''
    for g in groupings:
        c = Counter(g)
        max_char = c.most_common()[0][0]
        pot_shift = ord(max_char)-ord('e')
        pot_key += chr((pot_shift % 26) + ord('a'))
        decrypted = caesar_decrypt(g,pot_shift)
        decrypted_grps.append(decrypted)
    return decrypted_grps, pot_key

def reassemble_text(ciphertext, decrypted_groups, key_length):
    result = list(ciphertext)
    group_counters = [0] * key_length

    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            group_index = i % key_length

            if group_counters[group_index] < len(decrypted_groups[group_index]):
                result[i] = decrypted_groups[group_index][group_counters[group_index]]
                group_counters[group_index] += 1
    
    return ''.join(result)'''
