# import streamlit as st
# import os
# import random

# FILE = "accounts.txt"

# # 📁 Create the file if it doesn't exist
# if not os.path.exists(FILE):
#     open(FILE, 'w').close()

# # 🔁 Load and save functions
# def load_accounts():
#     accounts = {}
#     with open(FILE, 'r') as f:
#         for line in f:
#             acc = line.strip().split('|')
#             if len(acc) == 5:
#                 acc_no, name, age, pin, balance = acc
#                 accounts[acc_no] = {
#                     "name": name,
#                     "age": age,
#                     "pin": pin,
#                     "balance": int(balance)
#                 }
#     return accounts

# def save_accounts(accounts):
#     with open(FILE, 'w') as f:
#         for acc_no, data in accounts.items():
#             f.write(f"{acc_no}|{data['name']}|{data['age']}|{data['pin']}|{data['balance']}\n")

# accounts = load_accounts()

# # 🌐 UI Start
# st.title("🏦 Muneeb's Secure Bank System")

# menu = st.sidebar.selectbox("Select Option", ["Create Account", "Login"])

# # ✅ Create Account
# if menu == "Create Account":
#     st.header("✨ Open New Bank Account")
#     acc_no = st.text_input("Create Account Number")
#     name = st.text_input("Your Full Name")
#     age = st.number_input("Your Age", min_value=1)
#     initial = st.number_input("Initial Deposit", min_value=0)

#     if st.button("Create"):
#         if acc_no in accounts:
#             st.error("❌ Account number already exists.")
#         else:
#             pin = str(random.randint(1000, 9999))  # Auto-generate 4-digit PIN
#             accounts[acc_no] = {
#                 "name": name,
#                 "age": age,
#                 "pin": pin,
#                 "balance": initial
#             }
#             save_accounts(accounts)
#             st.success("✅ Account Created Successfully!")
#             st.info(f"🔐 Your PIN is: {pin}\n📌 Please save it securely!")

# # 🔐 Login
# if menu == "Login":
#     st.header("🔐 Login to Your Bank Account")
#     acc_no = st.text_input("Account Number")
#     pin = st.text_input("PIN", type="password")
    

#     if acc_no in accounts and accounts[acc_no]['pin'] == pin:
#         st.success(f"👋 Welcome, {accounts[acc_no]['name']}!")

#         option = st.selectbox("Select Action", ["Deposit", "Withdraw", "Check Balance", "Show Info", "Delete Account"])

#         if option == "Deposit":
#             amount = st.number_input("Amount to Deposit", min_value=1)
#             if st.button("Deposit"):
#                 accounts[acc_no]['balance'] += amount
#                 save_accounts(accounts)
#                 st.success(f"✅ Rs {amount} deposited!")

#         elif option == "Withdraw":
#             amount = st.number_input("Amount to Withdraw", min_value=1)
#             if st.button("Withdraw"):
#                 if accounts[acc_no]['balance'] >= amount:
#                     accounts[acc_no]['balance'] -= amount
#                     save_accounts(accounts)
#                     st.success(f"✅ Rs {amount} withdrawn!")
#                 else:
#                     st.error("❌ Insufficient balance.")

#         elif option == "Check Balance":
#             st.info(f"💰 Current Balance: Rs {accounts[acc_no]['balance']}")

#         elif option == "Show Info":
#             acc = accounts[acc_no]
#             st.info(f"""
#                 👤 Name: {acc['name']}
#                 🧓 Age: {acc['age']}
#                 🪪 Account No: {acc_no}
#                 💼 Balance: Rs {acc['balance']}
#                 🔐 PIN: {acc['pin']}
#             """)

#         elif option == "Delete Account":
#             confirm = st.checkbox("Are you sure you want to delete your account?")
#             if confirm and st.button("Delete"):
#                 del accounts[acc_no]
#                 save_accounts(accounts)
#                 st.warning("🗑️ Your account has been deleted.")
#     elif acc_no != "":
#         st.error("❌ Invalid Account Number or PIN")














import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import random

# 🚀 Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json.json")  # Make sure this JSON is in your project folder
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 🔁 Load all accounts
def load_accounts():
    accounts = {}
    docs = db.collection('accounts').stream()
    for doc in docs:
        accounts[doc.id] = doc.to_dict()
    return accounts

# 💾 Save a single account
def save_account(acc_no, data):
    db.collection('accounts').document(acc_no).set(data)

# 🗑️ Delete a single account
def delete_account(acc_no):
    db.collection('accounts').document(acc_no).delete()

# 🌐 UI Start
st.title("🏦 Muneeb's Secure Bank System (with Firebase 🔥)")

menu = st.sidebar.selectbox("Select Option", ["Create Account", "Login"])

accounts = load_accounts()

# ✅ Create Account
if menu == "Create Account":
    st.header("✨ Open New Bank Account")
    acc_no = st.text_input("Create Account Number")
    name = st.text_input("Your Full Name")
    age = st.number_input("Your Age", min_value=1)
    initial = st.number_input("Initial Deposit", min_value=0)

    if st.button("Create"):
        if acc_no in accounts:
            st.error("❌ Account number already exists.")
        else:
            pin = str(random.randint(1000, 9999))  # Auto-generate 4-digit PIN
            account_data = {
                "name": name,
                "age": age,
                "pin": pin,
                "balance": int(initial)
            }
            save_account(acc_no, account_data)
            st.success("✅ Account Created Successfully!")
            st.info(f"🔐 Your PIN is: {pin}\n📌 Please save it securely!")

# 🔐 Login
if menu == "Login":
    st.header("🔐 Login to Your Bank Account")
    acc_no = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if acc_no in accounts and accounts[acc_no]['pin'] == pin:
        st.success(f"👋 Welcome, {accounts[acc_no]['name']}!")

        option = st.selectbox("Select Action", ["Deposit", "Withdraw", "Check Balance", "Show Info", "Delete Account"])

        if option == "Deposit":
            amount = st.number_input("Amount to Deposit", min_value=1)
            if st.button("Deposit"):
                accounts[acc_no]['balance'] += amount
                save_account(acc_no, accounts[acc_no])
                st.success(f"✅ Rs {amount} deposited!")

        elif option == "Withdraw":
            amount = st.number_input("Amount to Withdraw", min_value=1)
            if st.button("Withdraw"):
                if accounts[acc_no]['balance'] >= amount:
                    accounts[acc_no]['balance'] -= amount
                    save_account(acc_no, accounts[acc_no])
                    st.success(f"✅ Rs {amount} withdrawn!")
                else:
                    st.error("❌ Insufficient balance.")

        elif option == "Check Balance":
            st.info(f"💰 Current Balance: Rs {accounts[acc_no]['balance']}")

        elif option == "Show Info":
            acc = accounts[acc_no]
            st.info(f"""
                👤 Name: {acc['name']}
                🧓 Age: {acc['age']}
                🪪 Account No: {acc_no}
                💼 Balance: Rs {acc['balance']}
                🔐 PIN: {acc['pin']}
            """)

        elif option == "Delete Account":
            confirm = st.checkbox("Are you sure you want to delete your account?")
            if confirm and st.button("Delete"):
                delete_account(acc_no)
                st.warning("🗑️ Your account has been deleted.")
    elif acc_no != "":
        st.error("❌ Invalid Account Number or PIN")
