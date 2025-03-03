def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result

def main():
    while True:
        choice = input("Enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit: ").upper()
        
        if choice == 'Q':
            print("Exiting... Goodbye!")
            break
        elif choice in ('E', 'D'):
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            
            if choice == 'E':
                print("Encrypted message:", caesar_cipher(message, shift, "encrypt"))
            else:
                print("Decrypted message:", caesar_cipher(message, shift, "decrypt"))
        else:
            print("Invalid choice! Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
