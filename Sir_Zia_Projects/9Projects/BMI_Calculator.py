import streamlit as st 
st.title("BMI Calculator")
weight = st.number_input("Enter Your weight Here : (meter)",min_value=1.0,format="%.2f")
height = st.number_input("Enter Your height Here : (kg)",min_value=0.5,format="%.2f")
def Calculation(weight,height):
    if height > 0 :
        return round(weight/(height ** 2),2)
    else:
        return None

if st.button("Lets Calculate"):
    bmi = Calculation(weight,height)
    if bmi:
        st.write(f"Your BMI is : {bmi}")
        if bmi < 18.5:
            st.warning("You are **Underweight**.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a **Normal weight**. ✅")
        elif 24.9 <= bmi < 29.9:
            st.warning("You are **Overweight**.")
    else :
        st.error("You are so Obessed")
else :
    st.error("Invalid Please add Correct")                        
            
            
    