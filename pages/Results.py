import streamlit as st
import matplotlib.pyplot as plt

<<<<<<< HEAD
# 세션 상태 초기화
if "final_score" not in st.session_state:
    st.session_state.final_score = 0

# 결과 페이지
def results_page():
    score = st.session_state.final_score
    st.title("📊 퀴즈 결과")
    st.markdown(f"#### **최종 점수:** {score}점")
=======
def navbar():
    col1, col2, col3 = st.columns([6,3,1])
    with col1:
        st.markdown("🏠 Home > Login > Quiz > Results")
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
    if not st.session_state.get("logged_in", False):
        st.warning("로그인이 필요합니다.")
        if st.button("로그인 페이지로 이동"):
            st.switch_page("pages/Login.py")
        return

    st.title("📊 퀴즈 결과")
    
    # session_state를 통해서 로그인을 계속 유지합니다.
    score = st.session_state.get("score", 0)
    total_questions = len(st.session_state.get("selected_questions", []))
    if total_questions > 0:
        score_percentage = (score / total_questions) * 100
    else:
        score_percentage = 0

    st.markdown(f"#### 점수: {score}/{total_questions} ({score_percentage:.1f}%)")
>>>>>>> eb35fb288ca7fe09e4b55d87bfca796824ab0fd5

    feedback = ""
<<<<<<< HEAD
    if score == 5:
        feedback = "💯 **매우 잘하고 있습니다. 지식이 탄탄하시네요!**"
    elif score >= 4:
        feedback = "🌟 **지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다.**"
    elif score >= 3:
        feedback = "💪 **열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!**"
    elif score >= 2:
        feedback = "📚 **발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다. 파이팅!**"
    elif score >= 1:
=======
    if score_percentage == 100:
        feedback = "💯 **매우 잘하고 있습니다. 지식이 탄탄하시네요!**"
    elif score_percentage >= 80:
        feedback = "🌟 **지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다.**"
    elif score_percentage >= 60:
        feedback = "💪 **열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!**"
    elif score_percentage >= 40:
        feedback = "📚 **발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다.**"
    elif score_percentage >= 20:
>>>>>>> eb35fb288ca7fe09e4b55d87bfca796824ab0fd5
        feedback = "👨‍🎓 **부족합니다. 충분한 공부를 통해 더 좋은 결과를 얻어봐요.**"
    else:
        feedback = "🔍 **다른 분야를 알아보는 것도 나쁘지 않은 선택입니다!**"

    st.success(feedback)

    st.markdown("### 점수 진행률")
    st.progress(score_percentage / 100)

<<<<<<< HEAD
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
=======
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.barh(['점수'], [score_percentage], color='teal', alpha=0.8)
    ax.set_xlim(0, 100)
    ax.set_xlabel('점수 (%)')
    st.pyplot(fig)

    if st.button("🔄 다시 풀기"):
        st.switch_page("pages/Main.py")

if __name__ == "__main__":
    main()
>>>>>>> eb35fb288ca7fe09e4b55d87bfca796824ab0fd5
