# InvisibleBanana
A really wacky encoder that leverages how Nan errors are unique to change the bytes of an image into a bunch of Nan errors in a .bin file and deocde it back lossless into the original image!

<img width="118" height="75" alt="banana" src="https://github.com/user-attachments/assets/8fb3a21f-913f-49a8-a6a8-cd86d176e499" />



### My programs saves the banana as a bunch of NaNs, inspired by the end of the word of banana. NaN means not a number, and each NaN error is unique e.g. 0/0 Nan error isnt the same as sqrt(-1) per say.

Basically the program reads the file as raw bytes, groups them into 6-byte chunks, embeds each chunk into the payload bits of an IEEE-754 NaN floating-point value, writes those NaNs to a file, and later reverses the process by extracting the payload bits to reconstruct the original file byte-for-byte.

Each NaN error is given a unique letter whether it be 'n' or 'a', this results in the unholy file of 'nanananana...' as a chunk of text you see which is the picture basically. TLDR: I saved the banana pic as a bunch of math errors.


V1.0  -
<img width="845" height="277" alt="image" src="https://github.com/user-attachments/assets/b4e477d7-771c-4a8c-8b87-083a23a6b20f" />
Made the encoder, it takes each separate byte then converts it into a Nan error


V1.1 - Changed the encoder, the initial way to convert it into Nan errors corrupted the data so i changed the picture’s raw bytes into the payload bits of IEEE-754 NaN floating-point values, which keep the data nicely




V1.2 - Almost done with the decoder, I had issues changing the Nan into byte form until i realised that i was fomrattign the wrong part of the Nan, the middle 6 didigts form the byte which could then piece together 

V1.3 - Made it so that the encoder would ask for a jpeg to be used in the code, regardless of whethere it was a banana or not and then make the .bin file be saved in its own folder just for easy access, i then also provided the same file directory to the decoder, which saved it in the same file so you could get both with very easy access

V1.4 - FINAL - Since my NaNs are quiet IEEE-754 doubles with exponent all 1s and a 48-bit payload directly copied from my file into the fraction field, it looked like a jumbles mess, so i made the computer apply a converter of each error into either an n or an a in an array, this made the output code look like anananananananan over and over WHICH WAS EXACTLY LIKE HOW THE WORD BANANA IS! This should be my final entry im pretty happy with it!

V1.5 - Kept getting a formatting error when loading in larger images, so changed the code to allow for ANY sized image and retains the same lossless image!




<img width="319" height="440" alt="image" src="https://github.com/user-attachments/assets/c52895a9-aecf-4abe-94d9-8f6b7cb8f556" />



<img width="422" height="455" alt="image" src="https://github.com/user-attachments/assets/2a5ab1cb-e5b9-4ce1-a192-3c40d93b9169" />



Image of the hundreds of ananas

