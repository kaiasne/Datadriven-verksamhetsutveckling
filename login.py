import streamlit as st
import subprocess

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "123" and password == "123":
            st.success("Logged in as {}".format(username))
            # Redirect to another Streamlit application
            redirect_to_another_app()
        else:
            st.error("Invalid username or password")

def redirect_to_another_app():
    # Run another Streamlit application using subprocess
    subprocess.run(["streamlit", "run", "main_STREAMLIT.py"])

# Run the login function to start the login page
login()