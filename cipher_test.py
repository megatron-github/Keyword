ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import math

def remove_spaces(text):
    """ Given string   text  , build and return a new string with all
    spaces removed.  For example, from "Happy birthday   to you", return
    "Happybirthdaytoyou" """
    no_spaces_string = ''
    spaces = ' '
    for i in text:
        if i != spaces:
            no_spaces_string += i
    print(no_spaces_string)
    return no_spaces_string

def subtract(text, key):
    """ Given two uppercase letters of the alphabet, determine and return the
    unencrypted letter from the encrypted_letter was generated using
    key_letter.  For example, when encrypted_letter is "J" and key_letter is
    "R", return "S". """
    
    unencrypted_clue = ALPHABET.find(text) - ALPHABET.find(key)
    if unencrypted_clue < 0:
        unencrypted_clue = unencrypted_clue % 26
    
    return ALPHABET[unencrypted_clue]

def decrypt(text, key):
    """ For each letter in text, determine the letter from which it was 
    encrypted using key. Build and return the string of these letters. """
    unencrypted_letter = ""
    if len(key) != len(text):
        key = key * (math.ceil(len(text) / len(key)))
    for i in range(len(text)):
        unencrypted_letter += subtract(text[i], key[i])
    return unencrypted_letter

def report(message, clues):
    """ Print the   message  , and, for each clue in   clues  , if it occurs in 
      message  , indicate so on the output. """
    print("The decrypted message is", message)
    for entry in clues:
        if entry in message:
            print('Clue', entry, 'discovered in', message)
        
def main():
    """
    This function is provided in full. Its job is to control
    the flow of the program, and offload the details to the
    other functions.
    """
    captured_text = input('Enter the captured text: ')
    keyword = input('Enter a keyword: ')
    clues = input('Enter the clues separated by one space: ')
    clueList = clues.split();

    # Take all spaces out of the captured text:
    squished_text = remove_spaces(captured_text)

    # Send the captured text for decryption:
    decrypted_text = decrypt(squished_text, keyword)

    # Check the decrypted text for clues that indicate a real message.
    report(decrypted_text, clueList)


# Here we invoke the main function. This code is always included in our
# python programs.
if __name__ == "__main__":
    main()

                   
