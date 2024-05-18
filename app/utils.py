import os
from cryptography.fernet import Fernet

# Ensure you have a SECRET_KEY environment variable set
SECRET_KEY = os.getenv("SECRET_KEY")
cipher = Fernet(SECRET_KEY)

def encrypt_file(file_path):
    """
    Encrypts the contents of a file using a cipher and saves the encrypted data back to the same file.

    Args:
        file_path (str): The path to the file to be encrypted.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    """
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path):
    """
    Decrypts the contents of a file.

    Args:
        file_path (str): The path to the file to be decrypted.

    Returns:
        bytes: The decrypted data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file is empty or cannot be decrypted.

    """
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data
