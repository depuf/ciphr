import sys
#import requests
import typer
import inquirer as inq
import pyfiglet as pfg


from caesar import caesar_decrypt,caesar_encrypt
from vigenere import vig_decrypt,vig_encrypt
from vig_bruteforce import break_vig


def handle_vig():
    mode = inq.list_input("Encryption or decryption?", choices=['encryption','decryption'])

    if (mode == 'decryption'):
        key_bool = inq.list_input("Do you have a key?", choices=['yes','no'])
        if (key_bool == 'no'):
            vig_bruteforce()
        else:
            cipher_text = input("Cipher text: ")
            key = check_key()
            print(vig_decrypt(cipher_text,key))
    else:
        plain_text = input("Plain text: ")
        key = check_key()
        print(vig_encrypt(plain_text,key))

def vig_bruteforce():
    print("Note that brute-forcing with frequency analysis will attempt to decrypt the message by analyzing common letter patterns.")
    print("This may take time and the accuracy is not guaranteed.")
    cipher_text = input("Cipher text: ")
    break_vig(cipher_text)


def handle_caesar():
    mode = inq.list_input("Encryption or decryption?", choices=['encryption','decryption'])

    if (mode == 'decryption'):
        shift_bool = inq.list_input("Do you know the shift?", choices=['yes','no'])
        text = input("Cipher text: ")
        if (shift_bool == 'no'):
            caesar_bruteforce(text)
        else:
            shift = check_shift()
            print(caesar_decrypt(text,shift))
        
    else:
        text = input("Plain text: ")
        shift = check_shift()
        print(caesar_encrypt(text,shift))

def caesar_bruteforce(text):
    print("Brute forcing...")
    for x in range(1,25):
        print(f"shift {x}: {caesar_decrypt(text, x)}")

def check_shift():
    while True:
        shift = input("Shift: ")
        if (shift.isdigit()):
            return int(shift)
        else:
            print("Invalid shift, must be a number.")

def check_key():
    while True:
        key = input("Key: ")
        if (key.isalpha()):
            return key
        else:
            print("Invalid key, must be letters only.")

def help():
    print("i am very much a work in progress")


def main():
    while True:
        type = inq.list_input("Pick your cipher", choices=['caesar', 'vigenère','help','exit'])

        match type:
            case 'vigenère':
                handle_vig()
            case 'caesar':
                handle_caesar()
            case 'help':
                help()
            case 'exit':
                print("bye! ✮⋆˙")
                sys.exit()
        


if __name__ == "__main__":
    print(pfg.figlet_format("ciphr",font="slant"))
    main()