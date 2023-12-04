import hmac
import streamlit as st

def check_password():
    # Form for user credentials
    def login_form():
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    # Verify user credentials
    def password_entered():
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(
                st.session_state["password"], st.secrets.passwords[st.session_state["username"]]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Validate credentials
    if st.session_state.get("password_correct", False):
        return True

    login_form()
    if "password_correct" in st.session_state:
        st.error("User not known or password incorrect")
    return False

if not check_password():
    st.stop()  # Stop the app if credentials are incorrect

# Main app code starts here
st.write("Your Streamlit app content goes here...")
