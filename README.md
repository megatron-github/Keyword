# keyword
An introduction to Python programming

You are an Orc cryptanalyst working for the wizard Saruman from an undisclosed location near Emyn Arnen. Allies have intercepted a message that originated in Lothlórien; it appears to have been on its way to Helm’s Deep when the messenger was captured.

The captured text will be in the form

FLVYM NFZKQ MVVZL YSIUM DBOOV

That the code is broken into five-letter groups inspires you: this may very well be a keyword cipher. To decrypt a keyword cipher, it is important to know how to encrypt a message using a keyword: the message (called the plaintext) is written, as is customary, in five-letter groups, with a keyword written repeatedly above.

For example,

RINGR INGRI NGRIN GRING RINGR
ELVES HAVEA TTACK ERIAD ORXXX

shows the keyword RING written above the plaintext ELVES HAVE ATTACKED ERIADOR. Notice that: (a) if the length of the plaintext (with spaces removed) is not a multiple of five, then the author fills in the remainder with the letter X; and (b) if needed, only part of the keyword is used to complete the top line. Once this task is completed, the encrypted message is found by adding the values (with A as 0, B as 1, and so on up to Z as 25) of the pairs of letters in columns, using modular arithmetic if needed, to find the result. For example, in the first column we have R (letter 17 in the alphabet) added to E (letter 4 in the alphabet) to give us letter 21 in the alphabet: V. Thus, the letter E in the plaintext is encrypted as V thanks to the letter R in the keyword.

In the fifth column, we add R (17) to S (18) to get 35, which is beyond the end of the alphabet. We calculate 35 % 26 to get 9, and thus use the letter J. This process is continued to fully encrypt the plaintext. The result is called the ciphertext. A keyword cipher is extremely safe as long as the adversary does not know the keyword, but if the adversary has some idea of what the keyword might be, they can try all of the possibilities and, with luck, recover the plaintext.

Your program will simulate the work of the many Orcs in your command, who will of course not use computers, but will write with foul ink on paper pressed from the trees of Fangorn Forest. The skeleton program has a main() function, already provided. Your job is to provide the implementations for three other functions:
• remove_spaces, called by main,
• decrypt, called by main, and
• subtract, called by decrypt.

The user will input the captured_text (the ciphertext) and a keyword, and some clues to search for. Your program should decrypt the captured text and check it for these clues that indicate a useful decryption. In addition, the report() and main() functions are already written for you. 

Here is a sample interaction with the program.

Enter the captured text: FLVYM NFZKQ MVVZL YSIUM DBOOV
Enter a keyword: MERRY
Enter the clues separated by one space: HOBBITS MORDOR RING
The decrypted message is THEHOBBITSAREINMORDORXXXX
Clue HOBBITS discovered in THEHOBBITSAREINMORDORXXXX
Clue MORDOR discovered in THEHOBBITSAREINMORDORXXXX
