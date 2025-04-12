from cryptography.fernet import Fernet

# Normally store this securely
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()
