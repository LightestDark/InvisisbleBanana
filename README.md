# InvisibleBanana
A really wacky encoder that leverages how Nan errors are unique to change the bytes of an image into a bunch of Nan errors in a .bin file and deocde it back lossless into the original image!


V1.0  -
<img width="845" height="277" alt="image" src="https://github.com/user-attachments/assets/b4e477d7-771c-4a8c-8b87-083a23a6b20f" />
Made the encoder, it takes each separate byte then converts it into a Nan error


V1.1 - Changed the encoder, the initial way to convert it into Nan errors corrupted the data so i changed the picture’s raw bytes into the payload bits of IEEE-754 NaN floating-point values, which keep the data nicely
