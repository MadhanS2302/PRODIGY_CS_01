def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift_amount = shift
            if decrypt:
                shift_amount = -shift_amount  # For decryption, shift in the opposite direction
            shifted_char = chr(((ord(char) - 65 + shift_amount) % 26) + 65)
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter the message: ").upper()
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            encrypted_text = caesar_cipher(text, shift)
            print("Encrypted message:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, decrypt=True)
            print("Decrypted message:", decrypted_text)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()

