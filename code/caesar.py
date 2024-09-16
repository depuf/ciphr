# decryption algo

wav = 26

def caesar_process(text,shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            offset = ord("A") if letter.isupper() else ord("a")
            x = (ord(letter)- offset - shift) % wav
            result += chr(x + offset)
        else:
            result += letter
    return result

def caesar_decrypt(text, shift):
    return caesar_process(text,shift)

def caesar_encrypt(text, shift):
    return caesar_process(text,-shift)