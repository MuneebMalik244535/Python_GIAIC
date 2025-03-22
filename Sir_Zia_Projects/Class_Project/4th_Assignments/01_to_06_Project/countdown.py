import streamlit as st
import time

st.title("⏳ Countdown Timer")
seconds = st.number_input("Enter seconds:", min_value=1, step=1)

if st.button("Start Timer"):
    for i in range(seconds, 0, -1):
        st.write(f"⏳ {i} seconds left")
        time.sleep(1)
        st.experimental_rerun()
    st.success("⏰ Time is up!")
