# decryption algo
def caesar_decrypt(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            offset = 65 if letter.isupper() else 97
            x = (ord(letter)- offset - shift) % 26
            result += chr(x + offset)
        else:
            result += letter
    return result

def caesar_encrypt(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            offset = 65 if letter.isupper() else 97
            x = (ord(letter)- offset + shift) % 26
            result += chr(x + offset)
        else:
            result += letter
    return result

# expected: k nqxg aqw for i love you
res = caesar_encrypt("i love you", 2)
print(res)