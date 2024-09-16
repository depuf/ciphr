import sys
#import requests
import typer
import inquirer as inq
import pyfiglet as pfg


from caesar import caesar_decrypt,caesar_encrypt
from vigenere import vig_decrypt,vig_encrypt

def main():
    type = inq.list_input("Pick your cipher", choices=['caesar', 'vigenère','help','exit'])

    match type:
        case 'vigenère':
            mode = inq.list_input("Encryption or decryption?", choices=['encryption','decryption'])

            if (mode == 'decryption'):
                key_bool = inq.list_input("Do you have a key?", choices=['yes','no'])
                if (key_bool == 'no'):
                    print("Note that brute-forcing with frequency analysis will attempt to decrypt the message by analyzing common letter patterns.")
                    print("This may take time and the accuracy is not guaranteed.")
                    proceed = inq.confirm("Do you wish to proceed?", default=False)
                    if not proceed:
                        main()
                    # code that doesnt exist
                    print("i am a work in progress mhmmmmmm")
                else:
                    cipher_text = input("Cipher text: ")
                    key = input("Key: ")
                    print(vig_decrypt(cipher_text,key))
                    main()
            else:
                plain_text = input("Plain text: ")
                key = input("Key: ")
                print(vig_encrypt(plain_text,key))
                main()

        case 'caesar':
            mode = inq.list_input("Encryption or decryption?", choices=['encryption','decryption'])
            if (mode == 'decryption'):
                shift_bool = inq.list_input("Do you know the shift?", choices=['yes','no'])
                text = input("Cipher text: ")
                if (shift_bool == 'no'):
                    print("Brute forcing...")
                    for x in range(1,25):
                        print(f"shift {x}: {caesar_decrypt(text, x)}")

            else:
                text = input("Plain text: ")
                shift = int(input("Shift: "))
                print(caesar_encrypt(text,shift))
                main()

                
        case 'help':
            print("i am also a work in progress")
            # help msg

        case 'exit':
            # i want something here
            sys.exit()
        




if __name__ == "__main__":
    print(pfg.figlet_format("ciphr",font="slant"))
    main()