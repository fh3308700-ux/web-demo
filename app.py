import streamlit as st
import pandas as pd

# Sample data: Country information
data = {
    "Country": ["USA", "Canada", "Germany", "Australia", "India"],
    "Capital": ["Washington, D.C.", "Ottawa", "Berlin", "Canberra", "New Delhi"],
    "Population": [331002651, 37742154, 83783942, 25499884, 1380004385],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Streamlit app content
st.title("Country Information App")
st.write("This is a simple Streamlit app displaying information about different countries.")

# Display the DataFrame
st.write(df)

# Add a description or additional functionality
st.write("You can add more functionality here, such as interactive filters or graphs.")
