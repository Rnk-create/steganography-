## Secure LSB Steganography Tool

A Python-based command-line tool that hides secret text messages inside images using Least Significant Bit (LSB) steganography. It includes XOR encryption to ensure that even if the message is found, it cannot be read without a password.

## To execute this file:

1. Install the Pillow library:
   
<img width="1144" height="165" alt="Screenshot 2025-11-25 220618" src="https://github.com/user-attachments/assets/151ac1f6-b021-4870-88c9-fad880a64d60" />


2. Run the code and enter the key, password and secret message accordingly:
   
<img width="1453" height="452" alt="Screenshot 2025-11-25 220911" src="https://github.com/user-attachments/assets/3a6a368b-5b57-4917-b4f4-904b1fa6d9ed" />


3. Now to decode this, use the same key and you will get your secret message:
   
<img width="1450" height="485" alt="Screenshot 2025-11-25 220959" src="https://github.com/user-attachments/assets/2eae9a46-c0fd-4184-a921-7849cb6f7fc2" />


## 🔐 Hiding a Message (Encryption)

1. **Select Mode**  
   Type `h` to enter **Hide mode**.

2. **Choose Cover Image**  
   Press **Enter** to use the default `cover_image.png`,  
   or type the filename of the image you want to use.

3. **Output File Name**  
   Enter the name of the stego image you want to generate  
   (e.g., `secret_msg.png`).

4. **Enter Secret Message**  
   Type the text you want to hide  
   (example: `here's your password : 12345678`).

5. **Enter Password / Key**  
   Provide a key (e.g., `rnk`).  
   This key encrypts your message before embedding it.

6. **Success**  
   The tool will confirm: "Encrypted message hidden in 'secret_msg.png'".


---

## 🔓 Extracting a Message (Decryption)

1. **Select Mode**  
Type `e` to enter **Extract mode**.

2. **Provide Stego Image**  
Enter the filename that contains the hidden message  
(e.g., `secret_msg.png`).

3. **Enter Password / Key**  
Enter the **same key** used during encryption  
(e.g., `rnk`).

4. **Result**  
The tool extracts and decrypts the hidden text, then prints: "Your Password : 12345678"

