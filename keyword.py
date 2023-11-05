#!/usr/bin/env python3
"""
 ***************************************************************************************************
    FILE:        keyword.py

    DESCRIPTION: This program will allow you to input an encrypted phrase and a key word. Then it is
    going to contrast the location of the words in the encrypted phrase and the key word in the
    alphabet. Then the computer is going to print out the decrypted phrase using the different in
    locations of the encrypted phrase and the key word.

 ***************************************************************************************************
"""
import math

def remove_spaces(text):
    """ Given string text, build and return a new string with all spaces removed.
    For example, from "Happy birthday to you", return "Happybirthdaytoyou". """

    return ''.join(text.split(' '))

def subtract(encrypted_letter, key_letter):
    """ Given two uppercase letters of the alphabet, determine and return the unencrypted letter
    from the encrypted_letter was generated using key_letter. For example, when encrypted_letter
    is "J" and key_letter is "R", return "S". """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Subtract the index of the encrypted word by the index of key in the alphabet.
    decrypted_clue = alphabet.find(encrypted_letter) - alphabet.find(key_letter)

    # If the decrypted clue is a negative value, add that negative number to 26
    decrypted_clue = decrypted_clue if decrypted_clue >= 0 else decrypted_clue % 26
    return alphabet[decrypted_clue]

def decrypt(encrypted_text, key):
    """ For each letter in text, determine the letter from which it was
    encrypted using key. Build and return the string of these letters. """

    decrypted_text = ""

    # Because the key word is usually shorter than the phrase, we multiply the
    # key word by the different in length of encrypted phrase and key to make
    # the range of the key word longer.
    if len(key) != len(encrypted_text):
        key = key * (math.ceil(len(encrypted_text) / len(key)))

    # For each letter in the same column of encrypted phrase and key word,
    # find decrypted letter using the subtract function.
    for char in range(len(encrypted_text)):
        decrypted_text += subtract(encrypted_text[char], key[char])
    return decrypted_text

def report(message, clues):
    """ Print the message, and, for each clue in clues, if it occurs in
      message, indicate so on the output. """

    print("The decrypted message is", message)
    for entry in clues:
        if entry in message:
            print('Clue', entry, 'discovered in', message)

def main():
    """ This function is provided in full. Its job is to control
    the flow of the program, and offload the details to the
    other functions. """

    captured_text = input('Enter the captured text: ')
    keyword = input('Enter a keyword: ')
    clues = input('Enter the clues separated by one space: ')
    clueList = clues.split(' ')

    # Take all spaces out of the captured text.
    squished_text = remove_spaces(captured_text)

    # Send the captured text for decryption.
    decrypted_text = decrypt(squished_text, keyword)

    # Check the decrypted text for clues that indicate a real message.
    report(decrypted_text, clueList)

if __name__ == "__main__":
    main()
