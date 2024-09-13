def vig_decrypt(text,key):
    # copy key to match length of text
    # then convert the key to numbers ?
    ref = repeat_key(text,key)
    result = ""
    y = 0;
    for x in range(len(text)):
        offset = 65 if text[x].isupper() else 97
        ref_offset = 65 if ref[y].isupper() else 97
        if text[x].isalpha():
            decrement = ord(ref[y]) - ref_offset
            temp = (ord(text[x]) - decrement - offset) % 26
            result += chr(temp + offset)
            y += 1 
        else:
            result += text[x]
    return result


def repeat_key(text, key):
    words = ''.join(text.split())
    num_words = len(words)
    repeated_key = (key * ((num_words // len(key)) + 1))[:num_words]
    return repeated_key


# expected: Hard for me to breathe when you are around
res = vig_decrypt("Kaej trr zk hr bekowhr cvhn lui drr gfruaj", "dango")
print(res)
# expected: I love bingsu
res2 = vig_decrypt("G faty nghsqo", "yum")
print(res2)