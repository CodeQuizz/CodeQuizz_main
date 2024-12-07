import streamlit as st
import json
import random

# JSON 파일 로드 함수
@st.cache_data
def load_questions(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# JSON 파일 경로
QUESTION_FILE = "data/quiz_questions.json"

# 문제 데이터 로드
questions_data = load_questions(QUESTION_FILE)

# 세션 상태 초기화
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
if "current_page" not in st.session_state:
    st.session_state.current_page = "Main"

# 퀴즈 시작 함수
def start_quiz():
    st.session_state.quiz_started = True
    st.session_state.score = 0
    st.session_state.current_question = 0
    st.session_state.show_hint = False
    st.session_state.feedback = None
    st.session_state.selected_questions = questions_data[st.session_state.selected_level]
    random.shuffle(st.session_state.selected_questions)

# 메인 화면
def main_page():
    if not st.session_state.quiz_started:
        st.title("옵션")
        st.subheader("난이도 설정")
        st.session_state.selected_level = st.selectbox(
            "난이도를 선택하세요:", list(questions_data.keys())
        )
        if st.button("퀴즈 시작"):
            start_quiz()

    # 퀴즈 진행
    if st.session_state.quiz_started:
        if st.session_state.current_question < len(st.session_state.selected_questions):
            question_data = st.session_state.selected_questions[st.session_state.current_question]
            st.subheader(f"문제 {st.session_state.current_question + 1}/{len(st.session_state.selected_questions)}")
            st.write(question_data["question"])

            if st.session_state.show_hint:
                st.info(f"힌트: {question_data['hint']}")

            if st.button("힌트 보기", key=f"hint_{st.session_state.current_question}"):
                st.session_state.show_hint = True
                st.rerun()

            user_answer = st.text_input("답변 입력:", key=f"answer_{st.session_state.current_question}")

            if st.button("제출", key=f"submit_{st.session_state.current_question}"):
                correct = user_answer.strip().lower() == question_data["answer"].lower()
                if correct:
                    st.session_state.feedback = "정답입니다! 🎉"
                    st.session_state.score += 1
                else:
                    st.session_state.feedback = f"오답입니다. 정답은 '{question_data['answer']}' 입니다."
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
            st.success("모든 문제를 완료했습니다!")
            st.write(f"최종 점수: {st.session_state.score}/{len(st.session_state.selected_questions)}")

            if st.button("퀴즈 다시 풀기"):
                st.session_state.quiz_started = False  # 퀴즈 상태 초기화
                st.session_state.current_page = "Main"
                st.session_state.final_score = st.session_state.score  # 결과 페이지에 점수 전달
                st.rerun()

            if st.button("결과 페이지로 넘어가기"):
                st.session_state.current_page = "Results"  # 페이지 전환 설정
                st.session_state.final_score = st.session_state.score  # 결과 페이지에 점수 전달
                st.rerun()

# 페이지 전환
if st.session_state.current_page == "Main":
    main_page()
elif st.session_state.current_page == "Results":
    from pages.Results import results_page
    results_page()
