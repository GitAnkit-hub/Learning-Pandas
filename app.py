import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, world!")

x = st.slider("Select a value", 1, 10)
st.write(x, "squared is", x * x)