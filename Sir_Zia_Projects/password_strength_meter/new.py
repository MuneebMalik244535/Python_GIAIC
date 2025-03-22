import streamlit as st 
import random
import re
import string
# fucntion banaonga jis mien user ka input check karunga 
def Check_Password(password):
    # score , feedback = 
    score = 0
    feedback = []
    # (1) password ki length check karenge
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Sorry Apka password chota h thora big likhen ")
    # (2) uppercase or lowercase
    if  re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    else:
        feedback.append("Please Use Capital and Small Letters")
    # (3) special character !@#$%^&*()?":>"
    if re.search(r"[!@#$%^&*()?><:/.,]",password):
        score += 1 
    else:
        feedback.append("Please use special character")
    # (4) number check karenge 
    if re.search(r"\d",password):   # \d = 123456789
        score += 1
    else:
        feedback.append("Please use number")
    return score,feedback

st.title("Please Check Your Password Strength")
user_input = st.text_input("Add Your Password",type="password")         
if st.button("Check"):
    if user_input:
        score , feedback = Check_Password(user_input)
        if score == 4:
          st.success("Your Password is Good")
        elif score == 3:
         st.warning("Please Make Your Password strengthfull")
        else:
         st.error("Your Password is Not Good")
         for message in   feedback:
          st.warning(message)
            
    