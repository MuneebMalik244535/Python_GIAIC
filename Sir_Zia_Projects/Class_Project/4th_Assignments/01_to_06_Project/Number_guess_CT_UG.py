import streamlit as st 
import random 
# UI banaonga:
st.title("Number Guessing Game")
random_number = random.randint(1,3)
user_input = st.number_input("Input Your Number",min_value=1,max_value=3,step=1)
st.subheader("Lets check")
if st.button("check the number"):
    if user_input < random_number:
        st.warning("its too much low think just a little bigger")
    elif user_input > random_number:
        st.warning("Its too much bigger think just little bit small")
    else :
        st.success("Congratulations you guess right number")        