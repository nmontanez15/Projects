# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:40:17 2022

@author: nmont
"""
import string
from time import sleep

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    
    print("Caesar Cipher Script.\n")
    # user prompt to enter a message they want decrypted
    encrypted_message = input("Enter the message you want to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    sleep(2) # give an appearance of doing something complicated
    print("Stand by, almost finished...\n")
    sleep(2) # more of the same
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()
