import streamlit as st
import json
import random
import time

# 페이지의 현재 위치를 알려주는 UX 추가
def navbar():
    col1, col2, col3 = st.columns([6,3,1])
    with col1:
        st.markdown("🏠 Home > Login > Quiz")
    with col2:
        if st.session_state.get("logged_in"):
            st.write(f"👤 {st.session_state['name']}님")

    with col3:
        if st.session_state.get("logged_in"):
            st.markdown(
                """
                <div style="display: flex; justify-content: flex-end; align-items: center;">
                    <button style="
                        border: none;
                        padding: 5px 10px;
                        font-size: 14px;
                        cursor: pointer;
                        border-radius: 4px;
                        white-space: nowrap;
                    " onclick="window.location.reload()">로그아웃</button>
                </div>
                """,
                unsafe_allow_html=True,
            )

# 현재 난이도 표시
def show_current_level():
    if st.session_state.get("selected_level"):
        level_colors = {
            "초급": "#4CAF50",  # 초록색
            "중급": "#FFA500",  # 주황색
            "고급": "#FF4500"   # 빨간색
        }
        selected_color = level_colors.get(st.session_state["selected_level"], "#000000")
        st.markdown(
            f"""
            <div style="
                border-radius: 10px; 
                padding: 6px 8px; 
                background-color: {selected_color}; 
                text-align: center; 
                display: inline-block; 
                color: white;
                background-color: {selected_color};
                font-size: 13px;
            ">
                {st.session_state['selected_level']}
            </div>
            """,
            unsafe_allow_html=True
        )


# 현재 난이도 표시
def show_current_level():
    if st.session_state.get("selected_level"):
        level_colors = {
            "초급": "#4CAF50",  # 초록색
            "중급": "#FFA500",  # 주황색
            "고급": "#FF4500"   # 빨간색
        }
        selected_color = level_colors.get(st.session_state["selected_level"], "#000000")
        st.markdown(
            f"""
            <div style="
                border-radius: 10px; 
                padding: 6px 8px; 
                background-color: {selected_color}; 
                text-align: center; 
                display: inline-block; 
                color: white;
                background-color: {selected_color};
                font-size: 13px;
            ">
                {st.session_state['selected_level']}
            </div>
            """,
            unsafe_allow_html=True
        )


@st.cache_data
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

QUESTION_FILE = "data/quiz_questions.json"
questions_data = load_questions(QUESTION_FILE)

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "feedback" not in st.session_state:
    st.session_state.feedback = None
if "wrong_answers" not in st.session_state:
    st.session_state.wrong_answers = []  # 틀린 문제 저장
# 타이머 추가했습니다.
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.show_hint = False
    st.session_state.feedback = None
    st.session_state.selected_questions = questions_data[st.session_state.selected_level]
    random.shuffle(st.session_state.selected_questions)
    st.session_state.wrong_answers = []  # 틀린 문제 초기화
    st.session_state.start_time = time.time()

def main():
    navbar()
    if not st.session_state.get("logged_in", False):
        st.warning("로그인이 필요합니다.")
        if st.button("로그인 페이지로 이동"):
            st.switch_page("pages/Login.py")
        return

    if not st.session_state.quiz_started:
        st.title("퀴즈 옵션")
        st.subheader("난이도 설정")
        st.session_state.selected_level = st.selectbox(
            "난이도를 선택하세요:", list(questions_data.keys())
        )
        if st.button("퀴즈 시작"):
            start_quiz()

    if st.session_state.quiz_started:
        elapsed = int(time.time() - st.session_state.start_time)
        mins = elapsed // 60 
        secs = elapsed % 60
        st.markdown(f"⏱️ 경과 시간: {mins:02d}분 {secs:02d}초")

        show_current_level()

        if st.session_state.current_question < len(st.session_state.selected_questions):
            question_data = st.session_state.selected_questions[st.session_state.current_question]
            st.subheader(f"문제 {st.session_state.current_question + 1}/{len(st.session_state.selected_questions)}")
            st.markdown(
                f"<p style='font-size: 18px; '>{question_data['question']}</p>",
                unsafe_allow_html=True
            )

            if st.session_state.show_hint:
                st.info(f"힌트: {question_data['hint']}")

            if st.button("힌트 보기"):
                st.session_state.show_hint = True
                st.rerun()

            user_answer = st.text_input("답변 입력:")

            if st.button("제출"):
                correct = user_answer.strip().lower() == question_data["answer"].lower()
                if correct:
                    st.session_state.feedback = "정답입니다! 🎉"
                    st.session_state.score += 1
                else:
                    st.session_state.feedback = f"오답입니다. 정답은 '{question_data['answer']}' 입니다."
                    st.session_state.wrong_answers.append(question_data)  # 틀린 문제 저장
                st.rerun()

            if st.session_state.feedback:
                if "정답입니다" in st.session_state.feedback:
                    st.success(st.session_state.feedback)
                else:
                    st.error(st.session_state.feedback)

                if st.button("다음 문제"):
                    st.session_state.current_question += 1
                    st.session_state.show_hint = False
                    st.session_state.feedback = None
                    st.rerun()
        else:
            st.balloons()
            st.success("모든 문제를 완료했습니다!")
            st.markdown(
                f"<p style='font-weight: bold;'>최종 점수: {st.session_state.score}/{len(st.session_state.selected_questions)}</p>",
                unsafe_allow_html=True
            )
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("퀴즈 다시 풀기"):
                    st.session_state.quiz_started = False
                    st.rerun()
            with col2:
                if st.button("결과 페이지로"):
                    st.switch_page("pages/Results.py")

if __name__ == "__main__":
    main()
