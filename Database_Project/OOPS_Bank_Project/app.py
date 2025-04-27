import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# 🚀 Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

db = firestore.client()



# 🔁 Load all accounts from Firebase
def load_accounts():
    accounts = {}
    docs = db.collection('accounts').stream()
    for doc in docs:
        accounts[doc.id] = doc.to_dict()
    return accounts

# 💾 Save a single account to Firebase
def save_account(acc_no, data):
    db.collection('accounts').document(acc_no).set(data)

# 🗑️ Delete a single account from Firebase
def delete_account(acc_no):
    db.collection('accounts').document(acc_no).delete()

accounts = load_accounts()

# 🌐 UI Start
st.title("🏦 Muneeb's Secure Bank System (🔥 Firebase Version)")

menu = st.sidebar.selectbox("Select Option", ["Create Account", "Login"])

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
