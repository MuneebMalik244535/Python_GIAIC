import json
import os

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return {"users": {}, "data": {}}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def store_user_data(username, encrypted_text):
    data = load_data()
    if username not in data["data"]:
        data["data"][username] = []
    data["data"][username].append(encrypted_text)
    save_data(data)

def get_user_data(username):
    data = load_data()
    return data["data"].get(username, [])
