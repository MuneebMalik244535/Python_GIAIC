# streamlit ko import karenge :
import streamlit as st # pip install streamlit
# function banayenge jis mien hum 3 cheezen add karenge
# values = user ka input , from_unit = jisko convert karna h , to_unit= jis mien convert karna h 
def Convert_units(values, from_unit , to_unit):
    conversion_formula = {
                "meters": {"kilometers": 0.001, "centimeters": 100, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
        "feet": {"meters": 0.3048, "centimeters": 30.48},
        "centimeters": {"meters": 0.01, "feet": 0.0328084},
    }
    if from_unit == to_unit:
        return values
    # calculation karenge yahan se :
    return values * conversion_formula.get(from_unit,{}).get(to_unit,{})
st.title("Simple Unit Converter")
st.sidebar.header("Select Conversion")
# lets define from_unit :
from_unit = st.sidebar.selectbox("From",["meters","kilometers","miles","centimeters","feet"])
to_unit = st.sidebar.selectbox("To",["meters","kilometers","miles","centimeters","feet"])
values = st.sidebar.number_input("Enter Your Value",min_value=0.0,format="%.2f")
# ab hum condition chalayenge : 34.4354645757
if st.sidebar.button("convert"):
    result = Convert_units(values,from_unit,to_unit)
    st.success(f"{values} {from_unit} ye jo user ne convert kiya h woh barabar h {result:.4f} {to_unit}")