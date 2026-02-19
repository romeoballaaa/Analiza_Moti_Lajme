from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

def get_cipher():
    # Menaxhim korrekt i celësave (.env) [cite: 30]
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        raise ValueError("ENCRYPTION_KEY nuk u gjet ne .env")
    return Fernet(key.encode())

def encrypt_message(data):
    # Enkriptim real i te dhenave [cite: 31]
    cipher = get_cipher()
    return cipher.encrypt(data.encode())