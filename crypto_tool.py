from cryptography.fernet import Fernet
import hashlib
import os

# Load the encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)


# Encrypt a file
def encrypt_file(filename):
    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)
    encrypted_filename = filename + ".enc"

    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

    print("\n[+] File encrypted successfully!")
    print("Encrypted file:", encrypted_filename)


# Decrypt a file
def decrypt_file(filename):
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    if filename.endswith(".enc"):
        decrypted_filename = filename[:-4] + "_decrypted.txt"
    else:
        decrypted_filename = filename + "_decrypted.txt"

    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

    print("\n[+] File decrypted successfully!")
    print("Decrypted file:", decrypted_filename)


# Generate SHA-256 hash
def hash_file(filename):
    with open(filename, "rb") as file:
        data = file.read()

    file_hash = hashlib.sha256(data).hexdigest()

    print("\n[+] SHA-256 Hash:")
    print(file_hash)


# Explain hashing vs encryption
def explain_difference():
    print("\n========== HASHING VS ENCRYPTION ==========")
    print("Encryption:")
    print("- Protects data by making it unreadable.")
    print("- Can be reversed using the correct key.")
    print("- Example: AES / Fernet")

    print("\nHashing:")
    print("- Creates a fixed-length fingerprint of data.")
    print("- Designed to be one-way.")
    print("- Used mainly for data integrity.")
    print("- Example: SHA-256")


# Key management information
def key_management():
    print("\n========== KEY MANAGEMENT BASICS ==========")
    print("- Never hardcode secret keys in your source code.")
    print("- Keep encryption keys separate from the program.")
    print("- Do not share secret keys publicly.")
    print("- Use strong randomly generated keys.")
    print("- Protect keys from unauthorized access.")


# Main menu
while True:
    print("\n===================================")
    print("       SECURE FILE TOOL")
    print("===================================")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Hash a file")
    print("4. Hashing vs Encryption")
    print("5. Key Management Tips")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        filename = input("Enter the file name: ")
        try:
            encrypt_file(filename)
        except FileNotFoundError:
            print("\n[!] File not found. Check the file name and try again.")

    elif choice == "2":
        filename = input("Enter the encrypted file name: ")
        try:
            decrypt_file(filename)
        except FileNotFoundError:
            print("\n[!] File not found. Check the file name and try again.")
        except Exception:
            print("\n[!] Decryption failed. Make sure the file and key are correct.")

    elif choice == "3":
        filename = input("Enter the file name: ")
        try:
            hash_file(filename)
        except FileNotFoundError:
            print("\n[!] File not found. Check the file name and try again.")

    elif choice == "4":
        explain_difference()

    elif choice == "5":
        key_management()

    elif choice == "6":
        print("\nThank you for using Secure File Tool!")
        break

    else:
        print("\n[!] Invalid choice. Please choose 1-6.")
