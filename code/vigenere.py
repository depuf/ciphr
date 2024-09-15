
wav = 26; # wrap around value

def repeat_key(text, key):
    words = ''.join(text.split())
    num_words = len(words)
    repeated_key = (key * ((num_words // len(key)) + 1))[:num_words]
    return repeated_key

def get_offset(letter):
    return ord("A") if letter.isupper() else ord("a")

def vig_process(text,key,mode):
    ref = repeat_key(text,key)
    result = ""
    y = 0;
    for x in range(len(text)):
        offset = get_offset(text[x])
        ref_offset = get_offset(ref[y])
        if text[x].isalpha():
            shift = ord(ref[y]) - ref_offset
            if mode == 'decrypt':
                temp = (ord(text[x]) - shift - offset) % wav
            else:
                temp = (ord(text[x]) + shift - offset) % wav
            result += chr(temp + offset)
            y += 1 
        else:
            result += text[x]
    return result

def vig_decrypt(text,key):
    return vig_process(text,key,'decrypt')

def vig_encrypt(text,key):
    return vig_process(text,key,'encrypt')

