import streamlit as st
import matplotlib.pyplot as plt

# Streamlit 스타일 커스터마이징
st.set_page_config(
    page_title="퀴즈 앱",
    page_icon="🎉",
    layout="wide",
)

# 목 데이터 설정 (유저 정보 및 점수)
mock_user_data = {
    "username": "홍성민",
}

# 점수 변수 설정 (여기서 점수를 변경할 수 있습니다)
quiz_score = 80  # 원하는 점수로 수정 가능
mock_user_data["score"] = quiz_score

# 초기 세션 상태 설정
if "current_page" not in st.session_state:
    st.session_state.current_page = "Intro"
if "username" not in st.session_state:
    st.session_state.username = mock_user_data["username"]

# 페이지 라우팅: 세션 상태 확인
def main():
    if st.session_state.current_page == "Intro":
        intro_page()
    elif st.session_state.current_page == "Results":
        results_page()

# Intro 페이지 함수
def intro_page():
    st.markdown("##### 👉 결과를 확인해 보세요!")

    with st.container():
        st.info("**로그인이 완료되었습니다.**")
        st.write(f"환영합니다, {st.session_state.username}님!")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("결과 페이지로 이동 🚀"):
            st.session_state.current_page = "Results"

# Results 페이지 함수
def results_page():
    username = st.session_state.username
    score = mock_user_data["score"]

    st.title("📊 퀴즈 결과")
    st.markdown(f"#### **사용자:** {username}")
    st.markdown(f"#### **점수:** {score}점")

    # 피드백 메시지
    feedback = ""
    if score == 100:
        feedback = "💯 **매우 잘하고 있습니다. 지식이 탄탄하시네요!**"
    elif score >= 80:
        feedback = "🌟 **지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다.**"
    elif score >= 60:
        feedback = "💪 **열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!**"
    elif score >= 40:
        feedback = "📚 **발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다. 파이팅!**"
    elif score >= 20:
        feedback = "👨‍🎓 **부족합니다. 충분한 공부를 통해 더 좋은 결과를 얻어봐요.**"
    else:
        feedback = "🔍 **다른 분야를 알아보는 것도 나쁘지 않은 선택입니다!**"

    st.success(feedback)

    st.markdown("### 점수 진행률")
    st.progress(score / 100)

    st.markdown("### 점수 시각화")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(['score'], [score], color='teal', alpha=0.8)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Total score')
    ax.set_title('Quiz Score')
    st.pyplot(fig)

    st.markdown(f"### 총점은 **{score}점** 입니다!")  # 총점 메시지 추가

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔙 Intro 페이지로 돌아가기"):
            st.session_state.current_page = "Intro"

# Streamlit 앱 실행
if __name__ == "__main__":
    main()
