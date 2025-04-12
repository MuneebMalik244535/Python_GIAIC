import streamlit as st
from auth import login_user, register_user
from crypto_utils import encrypt_data, decrypt_data
from data_store import store_user_data, get_user_data
from session_manager import init_session

init_session()

st.title("🔐 Secure Data Encryption System")
page = st.sidebar.radio("Menu", ["Login", "Register", "Store", "Retrieve"])

if page == "Register":
    st.subheader("📝 Register")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Register"):
        if register_user(u, p):
            st.success("User registered successfully!")
        else:
            st.error("Username already exists.")

elif page == "Login":
    st.subheader("🔑 Login")
    u = st.text_input("Username")
    p = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(u, p):
            st.success("Login successful")
            st.session_state.logged_in = True
            st.session_state.username = u
            st.session_state.attempts = 0
        else:
            st.error("Wrong credentials!")

elif page == "Store":
    if st.session_state.logged_in:
        st.subheader("📥 Store Data")
        text = st.text_area("Enter your secret message")
        if st.button("Encrypt & Store"):
            enc = encrypt_data(text)
            store_user_data(st.session_state.username, enc)
            st.success("Data encrypted and stored!")
    else:
        st.warning("Please login to store data.")

elif page == "Retrieve":
    if st.session_state.logged_in:
        st.subheader("📤 Retrieve Data")
        data_list = get_user_data(st.session_state.username)
        if data_list:
            for d in data_list:
                with st.expander("Encrypted Text"):
                    st.code(d)
                    if st.button(f"Decrypt {d[:10]}..."):
                        try:
                            st.success(decrypt_data(d))
                        except :
                            st.error("Decryption failed!")
        else:
            st.info("No data found.")
    else:
        st.warning("Please login to view data.")
