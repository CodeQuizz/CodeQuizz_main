import streamlit as st
import base64
import os

# 페이지 설정
st.set_page_config(
    page_title="Programming Quiz App",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    # 페이지 제목을 h1 태그로 추가하고 스타일을 적용
    st.markdown("<h1 style='color: black;'>Welcome to Programming Quiz! 🚀</h1>", unsafe_allow_html=True)
    
    # 설명 섹션 - 텍스트 색상 명시적으로 설정
    st.markdown(
        """<h3 style='color: black;'>Test Your Programming Knowledge!</h3>""",
        unsafe_allow_html=True
    )

    # 사용 방법 버튼
    with st.expander("📘 How to use"):
        st.markdown(
            """<p style='color: black;'>
            1. <b>Get Started ▶️ 버튼 클릭</b>: 퀴즈를 시작하려면 이 버튼을 누르세요.<br>
            2. <b>로그인</b>: 사용자 계정으로 로그인하거나 새로운 계정을 등록하세요.<br>
            3. <b>퀴즈 풀이</b>: 프로그래밍 관련 문제를 풀고 결과를 확인하세요.<br>
            4. <b>결과 확인</b>: 점수와 피드백을 확인하여 실력을 분석하세요.
            </p>""",
            unsafe_allow_html=True
        )

    # 시작 버튼
    if st.button("Get Started ▶️", use_container_width=True):
        st.write("Redirecting to Login Page...")  # 실제 페이지 이동 기능은 사용자 맞춤 코드로 수정 필요

if __name__ == "__main__":
    main()
