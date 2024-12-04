import streamlit as st
import json
from pathlib import Path

def load_users():
    users_file = Path("data/users.json")
    if users_file.exists():
        with open(users_file, "r") as f:
            return json.load(f)
    return {}

def main():
    st.title("Login Page 🔐")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        if submit:
            users = load_users()
            if username in users and users[username]["password"] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")

if __name__ == "__main__":
    main()
