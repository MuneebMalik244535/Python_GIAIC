import streamlit as st
import json
import hashlib

FILE_BASE = "users.json"

class UserManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(FILE_BASE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save_users(self):
        with open(FILE_BASE, "w") as file:
            json.dump(self.users, file, indent=4)

    def register(self, username, password):
        if username in self.users:
            return False, "Username already exists."
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        self.save_users()
        return True, "Registration successful!"

    def login(self, username, password):
        if username in self.users:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if self.users[username] == hashed_password:
                return True, "Login successful!"
        return False, "Invalid username or password."

def main():
    st.title("Login Authentication System")
    user_manager = UserManager()
    menu = ["Login", "Register"]
    choice = st.sidebar.selectbox("Menu:", menu)

    if choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            success, message = user_manager.login(username, password)
            if success:
                st.success(message)
                st.write(f"Welcome {username}! Thanks for logging in again.")
            else:
                st.error(message)
                st.warning("You Need to Register Yourself Firstly")

    elif choice == "Register":
        st.subheader("Registration Section")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Register"):
            success, message = user_manager.register(username, password)
            if success:
                st.success(message)
                st.write(f"Welcome {username}! Thanks for registering.")
            else:
                st.error(message)

if __name__ == "__main__":
    main()
