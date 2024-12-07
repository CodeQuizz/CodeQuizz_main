import streamlit as st
import matplotlib.pyplot as plt

# 세션 상태 초기화
if "final_score" not in st.session_state:
    st.session_state.final_score = 0

# 결과 페이지
def results_page():
    score = st.session_state.final_score
    st.title("📊 퀴즈 결과")
    st.markdown(f"#### **최종 점수:** {score}점")

    # 피드백 메시지
    feedback = ""
    if score == 5:
        feedback = "💯 **매우 잘하고 있습니다. 지식이 탄탄하시네요!**"
    elif score >= 4:
        feedback = "🌟 **지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다.**"
    elif score >= 3:
        feedback = "💪 **열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!**"
    elif score >= 2:
        feedback = "📚 **발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다. 파이팅!**"
    elif score >= 1:
        feedback = "👨‍🎓 **부족합니다. 충분한 공부를 통해 더 좋은 결과를 얻어봐요.**"
    else:
        feedback = "🔍 **다른 분야를 알아보는 것도 나쁘지 않은 선택입니다!**"

    st.success(feedback)

    st.markdown("### 점수 진행률")
    st.progress(score / 100)

    st.markdown("### 점수 시각화")
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.barh(['score'], [score], color='teal', alpha=0.8)
    ax.set_xlim(0, 5)
    ax.set_xlabel('Total score')
    ax.set_title('Quiz Score')
    st.pyplot(fig)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔙 문제로 돌아가기", on_click=lambda: st.session_state.update({"current_page": None})):
            st.session_state.current_page = ""  # 문제로 돌아가기
            st.rerun()  # 수정된 부분


# 결과 페이지 실행
if __name__ == "__main__":
    results_page()
