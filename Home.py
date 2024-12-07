import streamlit as st
import base64
import os

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

# 배경 이미지 설정 함수
def set_background(png_file_path):
    with open(png_file_path, "rb") as f:
        base64_png = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{base64_png}');
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# `assets` 폴더에 저장된 배경 이미지 파일 경로
assets_dir = "assets"
background_image_file = os.path.join(assets_dir, "coding.png")  # PNG 파일 이름은 필요에 따라 수정 가능

# 배경 이미지 설정
if os.path.exists(background_image_file):
    set_background(background_image_file)
else:
    st.error(f"Background image file not found in '{assets_dir}' directory!")

# CSS 스타일 설정
st.markdown(
    """
    <style>
    /* 기본 텍스트와 제목 스타일 */
    .stMarkdown, .stTitle, .stHeader {
        color: black !important;
    }

    /* Expander 헤더 전체 스타일 - 흰색 텍스트, 검은색 배경 */
    .stExpander > details > summary {
        color: white !important;         /* 텍스트 색상을 흰색으로 */
        background-color: black !important; /* 배경 색상을 검은색으로 */
        border-radius: 5px;              /* 둥근 모서리 */
        padding: 10px;                   /* 여백 추가 */
    }

    /* Expander 헤더 호버 효과 */
    .stExpander > details > summary:hover {
        background-color: #333333 !important; /* 호버 시 약간 밝은 검정 */
        color: white !important;              /* 호버 시에도 텍스트 색상 흰색 유지 */
    }

    /* Expander 내부 텍스트 색상 */
    .stExpander > div > div {
        color: black !important;  /* 내부 텍스트 색상 */
    }

    /* 버튼 텍스트 스타일 */
    .stButton button {
        color: white !important;       /* 버튼 텍스트 색상을 흰색으로 */
        background-color: black !important; /* 배경을 검은색으로 */
        border-radius: 5px;            /* 둥근 모서리 */
        padding: 10px 20px;            /* 버튼 크기 조정 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

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

