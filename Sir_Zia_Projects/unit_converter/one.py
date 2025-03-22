import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def convert_units(category, from_unit, to_unit, value):
    conversion_factors = {
        "Length": {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000},
        "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462},
        "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32},
    }
    
    if category in conversion_factors and from_unit in conversion_factors[category] and to_unit in conversion_factors[category]:
        factor_from = conversion_factors[category][from_unit]
        factor_to = conversion_factors[category][to_unit]
        
        if callable(factor_from):
            value_in_base = factor_from(value)
        else:
            value_in_base = value / factor_from
        
        if callable(factor_to):
            converted_value = factor_to(value_in_base)
        else:
            converted_value = value_in_base * factor_to
        
        return converted_value
    else:
        return None

st.title("Functional Unit Converter")
category = st.selectbox("Select a category", ["Length", "Weight", "Temperature"])
units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters"],
    "Weight": ["Kilograms", "Grams", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit"]
}
from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, from_unit, to_unit, value)
    if result is not None:
        st.success(f"Converted Value: {result:.2f} {to_unit}")
        
        # Generate Graph
        x_vals = np.linspace(0, value, 100)
        y_vals = [convert_units(category, from_unit, to_unit, x) for x in x_vals]
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, linestyle='-', marker='o', color='b')
        ax.set_xlabel(f"Value in {from_unit}")
        ax.set_ylabel(f"Value in {to_unit}")
        ax.set_title("Unit Conversion Graph")
        ax.grid(True)
        
        st.pyplot(fig)
    else:
        st.error("Invalid conversion selection.")
