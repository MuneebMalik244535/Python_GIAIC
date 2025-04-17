import streamlit as st
import hashlib
import os
import json
from cryptography.fernet import Fernet

st.set_page_config(page_title="Secure File App", layout="centered")

# Generate or load encryption key
if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as f:
        f.write(Fernet.generate_key())
with open("secret.key", "rb") as f:
    KEY = f.read()
cipher = Fernet(KEY)

# File paths
USER_FILE = "users.txt"
DATA_FILE = "data.txt"

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Load users
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Save users
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# Load user data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save user data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Helpers
def hash_passkey(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(text):
    return cipher.decrypt(text.encode()).decode()

# UI
menu = ["Register", "Login"]
if st.session_state.logged_in:
    menu += ["Store", "Retrieve", "Logout"]
choice = st.sidebar.selectbox("Menu", menu)

# Pages
users = load_users()
data = load_data()

if choice == "Register":
    st.header("📝 Register")
    new_user = st.text_input("Username")
    new_pass = st.text_input("Passkey", type="password")
    if st.button("Register"):
        if new_user and new_pass:
            if new_user in users:
                st.error("User already exists!")
            else:
                users[new_user] = hash_passkey(new_pass)
                save_users(users)
                st.success("Registered! Now log in.")
        else:
            st.error("Enter username and passkey")

elif choice == "Login":
    st.header("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Passkey", type="password")
    if st.button("Login"):
        if user in users and users[user] == hash_passkey(pwd):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success(f"Welcome, {user}!")
        else:
            st.error("Invalid credentials.")

elif choice == "Store" and st.session_state.logged_in:
    st.header("📦 Store Your Secret")
    plain_text = st.text_area("Enter your data")
    if st.button("Encrypt & Save"):
        if plain_text:
            encrypted = encrypt(plain_text)
            data[st.session_state.username] = encrypted
            save_data(data)
            st.success("Data encrypted and saved.")
        else:
            st.error("Please enter some data.")

elif choice == "Retrieve" and st.session_state.logged_in:
    st.header("🔍 Retrieve Your Secret")
    enc = data.get(st.session_state.username)
    if enc:
        if st.button("Decrypt"):
            decrypted = decrypt(enc)
            st.success(f"🔓 Your data: {decrypted}")
    else:
        st.info("No data found for your account.")

elif choice == "Logout":
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.success("Logged out!")
