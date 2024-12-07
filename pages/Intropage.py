import streamlit as st
import base64
from streamlit_option_menu import option_menu

# 배경 이미지 또는 GIF 설정
def set_background(file_path, file_type="image"):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    
    background_style = f"""
    <style>
    .stApp {{
        background: url(data:{file_type}/{"gif" if file_type == "gif" else "jpeg"};base64,{encoded_string});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# 공통 '홈으로 돌아가기' 버튼 함수
def home_button():
    if st.button("홈으로 돌아가기"):
        st.session_state["page"] = "홈"

# 다국어 지원용 딕셔너리
LANG = {
    "ko": {
        "home": "홈",
        "quiz": "퀴즈",
        "login": "로그인",
        "welcome": "프로그래밍 두뇌 풀가동! 코딩 챌린지에 뛰어들어보세요!",
        "quiz_title": "퀴즈 시작 화면",
        "select_difficulty": "난이도를 선택하세요:",
        "difficulty_easy": "하",
        "difficulty_medium": "중",
        "difficulty_hard": "상",
        "login_title": "로그인",
        "signup_title": "회원가입",
        "change_lang": "언어 전환",
    },
    "en": {
        "home": "Home",
        "quiz": "Quiz",
        "login": "Login",
        "welcome": "Activate your programming brain! Dive into the coding challenge!",
        "quiz_title": "Quiz Start Screen",
        "select_difficulty": "Select difficulty:",
        "difficulty_easy": "Easy",
        "difficulty_medium": "Medium",
        "difficulty_hard": "Hard",
        "login_title": "Login",
        "signup_title": "Sign Up",
        "change_lang": "Change Language",
    }
}

def get_text(key, lang="ko"):
    return LANG[lang].get(key, key)

# 홈 화면
def show_home(lang="ko"):
    st.markdown(
        f"""
        <div style="text-align: center; padding-top: 55vh;">
            <h1 style="color: white; font-size: 7vw;">코딩 챌린지!</h1>
            <p style="color: lightgray; font-size: 2vw;">{get_text("welcome", lang)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# # 퀴즈 화면
# def show_quiz(lang="ko"):
#     st.title(get_text("quiz_title", lang))
#     st.write(get_text("select_difficulty", lang))
#     difficulty = st.radio(
#         "",
#         options=[get_text("difficulty_easy", lang), 
#                  get_text("difficulty_medium", lang), 
#                  get_text("difficulty_hard", lang)]
#     )
#     st.write(f"선택한 난이도: {difficulty}")
#     home_button()

# # 로그인 화면
# def show_login(lang="ko"):
#     tab1, tab2 = st.tabs([get_text("login_title", lang), get_text("signup_title", lang)])

#     with tab1:  # 로그인 탭
#         st.title(get_text("login_title", lang))
#         username = st.text_input("사용자 이름", key="login_username")
#         password = st.text_input("비밀번호", type="password", key="login_password")
#         if st.button("로그인"):
#             st.success(f"{username}님, 환영합니다!")

#     with tab2:  # 회원가입 탭
#         st.title(get_text("signup_title", lang))
#         new_username = st.text_input("새 사용자 이름", key="signup_username")
#         new_password = st.text_input("새 비밀번호", type="password", key="signup_password")
#         confirm_password = st.text_input("비밀번호 확인", type="password", key="confirm_password")
#         if st.button("회원가입"):
#             if new_password == confirm_password:
#                 st.success("회원가입이 완료되었습니다!")
#             else:
#                 st.error("비밀번호가 일치하지 않습니다.")
#     home_button()

# # 메인 로직
# def main():
#     # 배경 이미지 또는 GIF 설정
#     set_background("quiz image.jpg", file_type="image")  # GIF 파일일 경우 "gif"로 변경

#     # URL 기반 페이지 상태 읽기 및 설정
#     if "page" not in st.session_state:
#         query_params = st.query_params
#         page = query_params.get("page", ["홈"])[0]
        
#         # 페이지 값 유효성 검사
#         if page not in ["홈", "퀴즈", "로그인"]:
#             page = "홈"
        
#         st.session_state["page"] = page

#     # 언어 상태 초기화
#     if "lang" not in st.session_state:
#         st.session_state["lang"] = "ko"

#     # 사이드바 메뉴
#     lang = st.session_state["lang"]
#     valid_pages = ["홈", "퀴즈", "로그인"]  # 유효한 페이지 목록
#     with st.sidebar:
#         current_page = st.session_state["page"]
#         if current_page not in valid_pages:
#             current_page = "홈"  # 유효하지 않은 경우 기본값으로 설정

#         choice = option_menu(
#             "Menu", 
#             [get_text("home", lang), get_text("quiz", lang), get_text("login", lang)],
#             icons=['house', 'kanban', 'robot'],
#             menu_icon="cast", 
#             default_index=valid_pages.index(current_page),  # 항상 유효한 값을 사용
#             styles={
#                 "container": {"padding": "5!important", "background-color": "#2c2c2c"},
#                 "icon": {"color": "#FFD700", "font-size": "20px"},
#                 "nav-link": {
#                     "font-size": "16px",
#                     "text-align": "left",
#                     "margin": "0px",
#                     "color": "white",
#                     "--hover-color": "#4a4a4a"
#                 },
#                 "nav-link-selected": {"background-color": "#FFD700", "color": "black"},
#             }
#         )
#         st.session_state["page"] = choice

#         # 언어 전환 버튼
#         if st.button(get_text("change_lang", lang)):
#             st.session_state["lang"] = "en" if st.session_state["lang"] == "ko" else "ko"

#     # 페이지 선택 로직
#     lang = st.session_state["lang"]
#     if st.session_state["page"] == get_text("home", lang):
#         show_home(lang)
#     elif st.session_state["page"] == get_text("quiz", lang):
#         show_quiz(lang)
#     elif st.session_state["page"] == get_text("login", lang):
#         show_login(lang)

# if __name__ == "__main__":
#     main()
