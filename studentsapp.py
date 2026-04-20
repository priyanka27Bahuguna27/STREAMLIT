import streamlit as st

st.title("My First App")

name = st.text_input("Enter your name:")

if name:
    st.write("Hello! Creating a simple web application using Streamlit.")
    st.write("Hello", name)

    age = st.number_input("Enter your age:", min_value=0, max_value=120)
    marks = st.number_input("Enter marks:", min_value=0, max_value=100)

    st.write("Your age is:", age)
    st.write("Your marks are:", marks)