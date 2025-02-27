import streamlit as st 
# UI banaonga :
st.title("My first Project")
st.write("Add given answer to create any story : ")
# user input banaonga :
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb:")
adjective = st.text_input("Enter an adjective:")
place = st.text_input("Enter a place:")
 # story generate karunga :
if st.button("generate"):
     create_story =f"Once upon a time in {place} there was {adjective} {noun} who loved to {verb}"
     st.subheader("Here is generated story")
     st.write(create_story)
