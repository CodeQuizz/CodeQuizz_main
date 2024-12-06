import streamlit as st

st.set_page_config(page_title="Programming Quiz App", page_icon="🎯", layout="wide")
#현재 위치를 알려주는 navbar
def navbar():
    col1, col2, col3 = st.columns([6,3,1])
    with col1:
        st.markdown("🏠 Home")
    with col2:
        if st.session_state.get("logged_in"):
            st.write(f"👤 {st.session_state['name']}님")
    with col3:
        if st.session_state.get("logged_in"):
            if st.button("로그아웃"):
                st.session_state["logged_in"] = False
                st.session_state["username"] = None
                st.session_state["name"] = None
                st.rerun()

def main():
    navbar()
    st.title("Welcome to Programming Quiz! 🚀")
    
    st.markdown("""
    ### 프로그래밍 실력을 테스트해보세요!
    다양한 난이도의 퀴즈로 실력을 향상시켜보세요.
    """)
    
    if st.button("시작하기 ▶️", use_container_width=True):
        st.switch_page("pages/Login.py")

if __name__ == "__main__":
    main()

