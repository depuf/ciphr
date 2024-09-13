# decryption algo

wav = 26

def caesar_process(text,shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            offset = 65 if letter.isupper() else 97
            x = (ord(letter)- offset - shift) % wav
            result += chr(x + offset)
        else:
            result += letter
    return result

def caesar_decrypt(text, shift):
    return caesar_process(text,shift)

def caesar_encrypt(text, shift):
    return caesar_process(text,-shift)

# expected: k nqxg aqw for i love you
res = caesar_encrypt("i love you", 2)
print(res)

res2 = caesar_decrypt("k nqxg aqw", 2)
print(res2)