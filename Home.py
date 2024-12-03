import streamlit as st

st.set_page_config(
    page_title="Programming Quiz App",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Welcome to Programming Quiz! 🚀")
    
    st.markdown("""
    ### Test Your Programming Knowledge!
    예시입니다 더 많은 기능과 UI를 구현해주세요 
    """)
    
    # Add a getting started button
    if st.button("Get Started ▶️", use_container_width=True):
        st.switch_page("pages/Login.py")

if __name__ == "__main__":
    main()