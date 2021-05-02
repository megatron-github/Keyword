# keyword

Suppose an Orc cryptanalyst is working for the wizard Saruman from an undisclosed location near Emyn Arnen. The allies intercept a message that originated in Lothlórien, in which it appears to have been on its way to Helm’s Deep.

The captured text in the form as

FLVYM NFZKQ MVVZL YSIUM DBOOV

Assume it is a keyword cipher. To decrypt the message, we need to know how the message was encrypted using a keyword. That is the message (called the plaintext) is written, as is customary, in five-letter groups, with a keyword written repeatedly above.

For example,

RINGR INGRI NGRIN GRING RINGR 

ELVES HAVEA TTACK ERIAD ORXXX

shows the keyword RING written above the plaintext 

ELVES HAVE ATTACKED ERIADOR. 

Notice that: 

(a) if the length of the plaintext (with spaces removed) is not a multiple of five, then the author fills in the remainder with the letter X;

(b) if necessary, only some parts of the keyword are needed to complete the top line. 

After we line up the keyword above the message, we can encrypt the message by adding the values (with A as 0, B as 1, and so on) of the pairs of letters in columns (using modular arithmetic if needed). For example, in the first column, we add R (letter 17 in the alphabet) to E (letter 4 in the alphabet) to give us the letter 21 in the alphabet: V. Thus, the letter E in the plaintext is encrypted as V thanks to the letter R in the keyword. In the fifth column, we add R (17) to S (18) to get 35, which is beyond the end of the alphabet. We calculate 35 % 26 to get 9, which is the position of the letter J. This process is continued to fully encrypt the plaintext. The result is called the ciphertext. A keyword cipher is extremely safe as long as the adversary does not know the keyword, but if the adversary has some idea of what the keyword might be, they can try all of the possibilities and, with luck, recover the plaintext.


The program will simulate the work of the many Orcs in the command, who will of course not use computers but will write with foul ink on paper pressed from the trees of Fangorn Forest. It will decrypt the captured text and check it for clues that indicate useful decryption. Here is a sample interaction with the program.

Enter the captured text: FLVYM NFZKQ MVVZL YSIUM DBOOV 

Enter a keyword: MERRY 

Enter the clues separated by one space: HOBBITS MORDOR RING 

The decrypted message is THEHOBBITSAREINMORDORXXXX 

Clue HOBBITS discovered in THEHOBBITSAREINMORDORXXXX 

Clue MORDOR discovered in THEHOBBITSAREINMORDORXXXX.
