import os
from PIL import Image

START_DELIMITER = "###START###"
END_DELIMITER = "###END###"

def xor_cipher(text: str, key: str) -> str:

    if not key:
        return text  # If no key is provided, return text as is
        
    result = []
    key_length = len(key)
    
    for i, char in enumerate(text):

        key_char = key[i % key_length]
        transformed_val = (ord(char) ^ ord(key_char)) & 0xFF
        
        result.append(chr(transformed_val))
        
    return "".join(result)

def bit_list_to_byte(bit_list: list[int]) -> int:
    byte = 0
    for i in range(8):
        byte = (byte << 1) | bit_list[i]
    return byte

def text_to_bit_stream(text: str) -> list[int]:
    bit_stream = []
    full_message = START_DELIMITER + text + END_DELIMITER

    for char in full_message:
        ascii_val = ord(char)
        if ascii_val > 255:
            ascii_val = 63 
            
        binary_string = format(ascii_val, '08b')
        for bit_char in binary_string:
            bit_stream.append(int(bit_char))
            
    return bit_stream

def hide_message(image_path: str, message: str, key: str, output_path: str):

    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size

        # 1. Encrypt the message using the Key BEFORE hiding it
        print(f"Encrypting message with key: '{key}'...")
        encrypted_message = xor_cipher(message, key)
        
        # 2. Convert encrypted text to bits
        bit_stream = text_to_bit_stream(encrypted_message)
        message_size_bits = len(bit_stream)
        max_capacity_bits = width * height * 3

        if message_size_bits > max_capacity_bits:
            print(f"Error: Message too large.")
            return

        image_data = list(img.getdata())
        modified_data = []
        bit_index = 0

        for pixel in image_data:
            new_pixel = []
            for color_value in pixel:
                if bit_index < message_size_bits:
                    message_bit = bit_stream[bit_index]
                    new_color = (color_value & 0xFE) | message_bit
                    new_pixel.append(new_color)
                    bit_index += 1
                else:
                    new_pixel.append(color_value)
            modified_data.append(tuple(new_pixel))
            if bit_index >= message_size_bits:
                break

        stego_img = Image.new(img.mode, img.size)
        stego_img.putdata(modified_data + image_data[len(modified_data):])
        stego_img.save(output_path)
        print(f"Success! Encrypted message hidden in '{output_path}'")

    except Exception as e:
        print(f"Error hiding message: {e}")

def extract_message(image_path: str, key: str) -> str:
    try:
        img = Image.open(image_path).convert('RGB')
        image_data = list(img.getdata())
        message_bits = []
        
        # 1. Extract LSBs
        for pixel in image_data:
            for color_value in pixel:
                message_bits.append(color_value & 1)

        extracted_raw_text = ""
        
        # 2. Rebuild the raw string (which contains delimiters + encrypted text)
        for i in range(0, len(message_bits), 8):
            byte_bits = message_bits[i:i+8]
            if len(byte_bits) < 8: break 
            
            char = chr(bit_list_to_byte(byte_bits))
            extracted_raw_text += char

            if END_DELIMITER in extracted_raw_text:
                break
        
        # 3. Find content between delimiters
        if START_DELIMITER in extracted_raw_text and END_DELIMITER in extracted_raw_text:
            start_index = extracted_raw_text.find(START_DELIMITER) + len(START_DELIMITER)
            end_index = extracted_raw_text.find(END_DELIMITER)
            
            encrypted_content = extracted_raw_text[start_index:end_index]
            
            # 4. Decrypt the content using the Key
            print(f"Message found! Decrypting with key: '{key}'...")
            decrypted_message = xor_cipher(encrypted_content, key)
            return decrypted_message
        else:
            return "No valid message found."

    except Exception as e:
        return f"Error extracting message: {e}"

#main
if __name__ == '__main__':
    print("--- Secure LSB Steganography Tool ---")
    
    mode = input("Do you want to (h)ide or (e)xtract a message? ").lower().strip()

    if mode.startswith('h'):
        input_image = input("Enter cover image filename (default: 'cover_image.png'): ").strip() or "cover_image.png"
        
        if not os.path.exists(input_image):
            print(f"Error: The file '{input_image}' was not found in this folder.")
        else:
            output_image = input("Enter output filename (default: 'stego_image.png'): ").strip() or "stego_image.png"
            secret = input("Enter the secret message to hide: ")
            key = input("Enter a secret password (key): ")
            
            if not key:
                print("Warning: No key provided. Message will be hidden without encryption.")
            
            hide_message(input_image, secret, key, output_image)

    elif mode.startswith('e'):
        stego_image = input("Enter image filename to read (default: 'stego_image.png'): ").strip() or "stego_image.png"
        
        if not os.path.exists(stego_image):
            print(f"Error: The file '{stego_image}' was not found in this folder.")
        else:
            key = input("Enter the secret password (key) to decrypt: ")
            print("\n--- Extracting ---")
            result = extract_message(stego_image, key)
            print(f"Final Result: {result}")
            
    else:
        print("Invalid selection. Please run the script again and choose 'h' or 'e'.")