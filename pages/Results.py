import streamlit as st
import matplotlib.pyplot as plt

def results_page():
    # 세션 상태 확인
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("결과를 보기 위해서는 로그인이 필요합니다.")
        return

    # 점수 계산
    total_questions = 5
    score_mapping = {0: 0, 1: 20, 2: 40, 3: 60, 4: 80, 5: 100}

    # 현재 점수가 세션에 없으면 기본값 설정
    current_score = st.session_state.get("current_score", 0)
    score = score_mapping.get(current_score, 0)

    # 피드백 메시지
    feedback = ""
    if score == 100:
        feedback = "매우 잘하고 있습니다. 지식이 탄탄하시네요!"
    elif score == 80:
        feedback = "지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다."
    elif score == 60:
        feedback = "열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!"
    elif score == 40:
        feedback = "발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다. 파이팅!"
    elif score == 20:
        feedback = "부족합니다. 충분한 공부를 통해 더 좋은 결과를 얻어봐요."
    else:  # score == 0
        feedback = "다른 분야를 알아보는 것도 나쁘지 않은 선택입니다!"

    # 결과 출력
    st.title("퀴즈 결과")
    st.write(f"**사용자:** {st.session_state.get('username', 'Unknown')}")
    st.write(f"**점수:** {score}점")
    st.write(feedback)

    # 시각화
    fig, ax = plt.subplots()
    ax.barh(['점수'], [score], color='indianred')
    ax.set_xlim(0, 100)
    ax.set_xlabel('점수')
    ax.set_title('퀴즈 점수 시각화')

    # Matplotlib 그래프를 Streamlit에 표시
    st.pyplot(fig)

    # "Intro 페이지로 돌아가기" 버튼 추가
    if st.button("Intro 페이지로 돌아가기"):
        st.experimental_set_query_params(page="Intro")

