import streamlit as st
import base64
import os

st.set_page_config(page_title="Programming Quiz App", page_icon="🎯", layout="wide")

# 현재 위치를 알려주는 navbar
def navbar():
    col1, col2, col3 = st.columns([6, 3, 1])
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

# How To Use 설명서 이미지
def show_how_to_use():
    how_to_use_image_path = "assets/How To Use.png"  # 이미지 파일 경로
    if os.path.exists(how_to_use_image_path):
        # HTML div를 사용하여 이미지 가운데 정렬
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{base64.b64encode(open(how_to_use_image_path, 'rb').read()).decode()}" width="600">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("How to Use 설명서 이미지가 'assets' 폴더에 없습니다.")

# CSS 스타일 설정
st.markdown(
    """
    <style>
    /* 기본 텍스트와 제목 스타일 */
    .stMarkdown, .stTitle, .stHeader {
        color: black !important;
    }

    /* Expander 헤더 전체 스타일 */
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

    /* Expander 내부 텍스트 스타일 */
    .stExpander > div > div {
        color: black !important; /* 텍스트 색상을 검정 */
        background-color: rgba(240, 240, 240, 1) !important; /* 연한 회색 배경 */
        padding: 20px; /* 내부 여백 */
        border-radius: 10px; /* 둥근 모서리 */
        line-height: 1.6; /* 줄 간격 */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
        border: 1px solid rgba(200, 200, 200, 0.8); /* 부드러운 테두리 */
    }

    /* Expander 내부 텍스트 색상 및 가독성 */
    .stExpander > div > div p {
        color: #333333 !important; /* 짙은 회색 텍스트 */
        font-size: 16px; /* 글씨 크기 */
        font-family: Arial, sans-serif; /* 텍스트 폰트 */
    }

    /* Expander 내 제목 스타일 */
    .stExpander > div > div h3, 
    .stExpander > div > div h4 {
        color: #222222 !important; /* 더 짙은 회색 제목 */
        border-bottom: 2px solid #007bff; /* 파란색 강조선 */
        padding-bottom: 10px;
        margin-bottom: 15px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # 세션 상태 초기화
    if 'show_image' not in st.session_state:
        st.session_state.show_image = False  # 이미지 표시 여부 상태 초기화

    navbar()
    st.markdown("<h1 style='color: black;'>Welcome to Programming Quiz! 🚀</h1>", unsafe_allow_html=True)
    
    st.markdown(""" 
    ### 프로그래밍 실력을 테스트해보세요!
    다양한 난이도의 퀴즈로 실력을 향상시켜보세요.
    """)
    
    # How to Use 버튼 클릭 시 이미지 토글
    if st.button("How to Use (사용 방법)", use_container_width=True):
        st.session_state.show_image = not st.session_state.show_image  # 상태 토글

    # 이미지가 표시되어야 할 때
    if st.session_state.show_image:
        show_how_to_use()

    if st.button("시작하기 ▶️", use_container_width=True):
        st.switch_page("pages/Login.py")

if __name__ == "__main__":
    main()
