import hashlib
from data_store import load_data, save_data

def hash_pass(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def register_user(username, password):
    data = load_data()
    if username in data["users"]:
        return False
    data["users"][username] = hash_pass(password)
    save_data(data)
    return True

def login_user(username, password):
    data = load_data()
    hashed = hash_pass(password)
    return data["users"].get(username) == hashed
