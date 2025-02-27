import streamlit as st
import random
st.title("My First Password Generator App")
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890"
User_slider = st.slider("Select Your Password Length",4,20,8)
def Generate_Password(User_slider):
    
    password = ""
    for i in range(User_slider):
        password += random.choice(characters)
    return password
if st.button("Generate"):
    password = Generate_Password(User_slider)
    st.write("Here is Your Password : ",password)
     