import streamlit as st
import json
from pathlib import Path

# 현재 위치를 알려주는 navbar
def navbar():
    col1, col2, col3 = st.columns([6, 3, 1])
    with col1:
        st.markdown("🏠 Home > Login")

# 사용자 정보를 불러오는 함수
def load_users():
    users_file = Path("data/users.json")
    if users_file.exists():
        with open(users_file, "r") as f:
            return json.load(f)
    return {}

# 메인 함수
def main():
    navbar()
    st.title("Programming Quiz Login 🔐")
    
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state.get("logged_in", False):
        st.success(f"환영합니다, {st.session_state['nickname']}님!")  # 별명 표시
        if st.button("퀴즈 시작하기"):
            st.switch_page("pages/Main.py")
    else:
        username = st.text_input("아이디")
        password = st.text_input("비밀번호", type="password")
        nickname = st.text_input("별명", help="로그인 시 사용할 별명을 입력하세요.")  # 별명 입력 추가
        
        if st.button("로그인"):
            users = load_users()
            if username in users and users[username]["password"] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["name"] = users[username]["name"]
                
                # 별명을 저장하고 표시할 수 있도록 세션 상태에 추가
                st.session_state["nickname"] = nickname if nickname else users[username]["name"]
                st.success(f"환영합니다, {st.session_state['nickname']}님!")
                st.rerun()
            else:
                st.error("아이디 또는 비밀번호가 잘못되었습니다.")

if __name__ == "__main__":
    main()
