Secure LSB Steganography Tool

A Python-based command-line tool that hides secret text messages inside images using Least Significant Bit (LSB) steganography. It includes XOR encryption to ensure that even if the message is found, it cannot be read without a password.

📸 Overview & Setup

1. Prerequisites

You need Python installed on your system. 

2. Installation

install the required library:

pip install Pillow


What is happening here?
As shown in the screenshot below, pip checks if Pillow is installed. If it's already there (as seen in the output "Requirement already satisfied"), you are ready to go.

🚀 How to Use

Run the tool by executing the script:

python stegano.py


(Note: Replace stegano.py with your actual filename if it's different, e.g., steganography_tool.py)

A. Hiding a Message (Encryption)

Select option 'h' when prompted to hide a message.

Steps shown in the screenshot:

Mode: Type h to enter Hide mode.

Cover Image: Press Enter to use the default cover_image.png (or type your own filename).

Output Name: Type the name for the new file (e.g., secret_msg.png).

Secret Message: Type the text you want to hide (e.g., here's your password : 12345678).

Password (Key): Enter a secret key (e.g., rnk). This encrypts your text before hiding it.

Success: The tool confirms "Encrypted message hidden in 'secret_msg.png'".

B. Extracting a Message (Decryption)

Select option 'e' when prompted to extract a message.

Steps shown in the screenshot:

Mode: Type e to enter Extract mode.

Stego Image: Type the filename containing the hidden message (e.g., secret_msg.png).

Password (Key): Enter the same key you used to hide the message (rnk).

Result: The tool reads the hidden bits, decrypts them using your key, and prints the original secret: here's your password : 12345678.

🧠 How it Works

LSB (Least Significant Bit): The tool takes the binary version of your message and replaces the very last bit of the image's color data. This change is so small (e.g., changing a color value from 254 to 255) that the human eye cannot see it.

XOR Cipher: Before hiding, the text is mixed with your password using XOR logic. This ensures that without the correct password, the extracted bits look like random garbage.

⚠️ Notes

Image Format: Always use .PNG files. Formats like JPG compress images, which destroys the hidden data.

Capacity: The amount of text you can hide depends on the image size. A larger image = more pixels = more space for text.
