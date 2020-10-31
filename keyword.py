"""
 *****************************************************************************
   FILE:        decrypt.py
                
   AUTHOR:      Truong Pham

   ASSIGNMENT:  Project 4: Cipher

   DATE:        9/19/18

   DESCRIPTION: This program will allow you to input an encrypted phrase and 
                a key word. Then it is going to contrast the location of
                the words in the encrypted phrase and the key word in the 
                alphabet. Then the computer is going to print out the 
                decrypted phrase using the different in locations of the 
                encrypted phrase and the key word.

 *****************************************************************************
"""
import math

def remove_spaces(text):
    """ Given string text, build and return a new string with all
    spaces removed.  For example, from "Happy birthday to you", return
    "Happybirthdaytoyou". """
    
    # The new string where it has the words in the input string but not 
    # spaces between the words.
    no_spaces_string = ''

    # The variable identify the space between words for the program to look for.
    spaces = ' ' 

    # For every character in the encrypted phrase that is a not a space, 
    # add them to the new string no_spaces_string.
    for char in text:
        if char != spaces:
            no_spaces_string += char

    # Return the new strings that have only words but no spaces 
    # to the main function. 
    return no_spaces_string

def subtract(text, key):
    """ Given two uppercase letters of the alphabet, determine and return the
    unencrypted letter from the encrypted_letter was generated using
    key_letter.  For example, when encrypted_letter is "J" and key_letter is
    "R", return "S". """

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # alphabet.find(text) finds the location of the encrypted word in the 
    # alphabet.
    # alphabet.find(key) finds the location of the key word in the alphabet.
    # The decrypted word is found by subtracting the location of the encrypted 
    # word by the location of the key word, hence the function is call subtract. 
    decrypted_clue = alphabet.find(text) - alphabet.find(key)
    
    # If the decrypted clue is a ngeative number (text - key = negative),
    # add that negative number to 26, since there're 26 letters in the Alphabet. 
    if decrypted_clue < 0:
        decrypted_clue = decrypted_clue % 26
    
    # Return the letter in the alphabet that is in the location of 
    # "decrypted_clue" to the function decrypt.
    return alphabet[decrypted_clue]

def decrypt(text, key):
    """ For each letter in text, determine the letter from which it was 
    encrypted using key. Build and return the string of these letters. """

    # A new string of letters that is decrypted using key. 
    decrypted_letter = ""

    # Because the key word is usually shorter than the phrase, we multiply the 
    # key word by the different in length of encrypted phrase and key to make 
    # the range of the key word longer. 
    # The multiplication is going to make the word repeat itself 
    # (merry * 2 = merrymerry).  
    if len(key) != len(text):
        key = key * (math.ceil(len(text) / len(key)))

    # For each letter in the same column of encrypted phrase and key word, 
    # find decrypted letter using the subtract function. 
    for char in range(len(text)):
        decrypted_letter += subtract(text[char], key[char])

    # Return the decrypted letter to the main function. 
    return decrypted_letter

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
    clueList = clues.split()

    # Take all spaces out of the captured text.
    squished_text = remove_spaces(captured_text)

    # Send the captured text for decryption.
    decrypted_text = decrypt(squished_text, keyword)

    # Check the decrypted text for clues that indicate a real message.
    report(decrypted_text, clueList)


# Here we invoke the main function. This code is always included in our
# python programs.
if __name__ == "__main__":
    main()
