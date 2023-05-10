import streamlit as st

st.title("My Streamlit Test App")

st.write("Welcome to my test page!")

x = st.slider('Select a value:', 0, 100, 50)
st.write('You selected:', x)

if st.button('Double the value'):
    x *= 2
    st.write('New value:', x)
