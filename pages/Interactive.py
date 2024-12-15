import streamlit as st
import json
import random

def navbar():
    col1, col2, col3 = st.columns([6, 3, 1])
    with col1:
        st.markdown("🏠 Home > Login > Quiz > Interactive")
    with col2:
        if st.session_state.get("logged_in"):
            st.write(f"👤 {st.session_state['name']}님")
    with col3:
        if st.session_state.get("logged_in"):
            if st.button("로그아웃"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.session_state["logged_in"] = False
                st.switch_page("pages/Login.py")

# 코드 조각 데이터
CODING_PUZZLES = {
    "피보나치 함수": {
        "description": "피보나치 수열을 계산하는 함수를 완성하세요.",
        "pieces": [
            "def fibonacci(n):",
            "    if n <= 1:",
            "        return n",
            "    return fibonacci(n-1) + fibonacci(n-2)"
        ],
        "answer": [0, 1, 2, 3],
        "hint": "재귀 함수를 사용하며, 기본 케이스는 n이 1 이하일 때입니다."
    },
    "버블정렬": {
        "description": "버블 정렬 알고리즘을 완성하세요.",
        "pieces": [
            "def bubble_sort(arr):",
            "    for i in range(len(arr)):",
            "        for j in range(len(arr)-1-i):",
            "            if arr[j] > arr[j+1]:",
            "                arr[j], arr[j+1] = arr[j+1], arr[j]"
        ],
        "answer": [0, 1, 2, 3, 4],
        "hint": "인접한 두 원소를 비교하여 순서가 잘못되어 있으면 교환합니다."
    }
}

# 디버깅 퀴즈 데이터
DEBUG_PUZZLES = {
    "리스트 합계 함수": {
        "description": "이 함수에는 버그가 있습니다. 올바른 답을 선택하세요.",
        "buggy_code": """
def sum_list(numbers):
    total = 0
    for i in range(len(numbers)-1):
        total += numbers[i]
    return total
        """,
        "options": [
            "range(len(numbers)-1)를 range(len(numbers))로 수정",
            "total = 1로 초기화",
            "return total + numbers[-1] 사용",
            "for 문을 while 문으로 변경"
        ],
        "correct": 0,
        "explanation": "현재 코드는 마지막 요소를 건너뛰고 있습니다. range(len(numbers))로 수정해야 합니다."
    }
}

def init_session_state():
    if 'current_order' not in st.session_state:
        st.session_state.current_order = []
    if 'selected_puzzle' not in st.session_state:
        st.session_state.selected_puzzle = None
    if 'debug_feedback' not in st.session_state:
        st.session_state.debug_feedback = None
    if 'show_hint' not in st.session_state:
        st.session_state.show_hint = False

def show_code_preview(pieces, order):
    st.markdown("### 현재 코드")
    if order:
        code = "\n".join([pieces[i] for i in order if i < len(pieces)])
        st.code(code, language='python')
    else:
        st.info("코드 조각을 선택하면 여기에 미리보기가 표시됩니다.")

def main():
    navbar()
    if not st.session_state.get("logged_in", False):
        st.warning("로그인이 필요합니다.")
        if st.button("로그인 페이지로 이동"):
            st.switch_page("pages/Login.py")
        return

    init_session_state()
    
    st.title("🧩 인터랙티브 코딩 퀴즈")
    
    tab1, tab2 = st.tabs(["코드 조각 맞추기", "디버깅 퀴즈"])
    
    with tab1:
        st.subheader("코드 조각 맞추기")
        puzzle_name = st.selectbox(
            "퍼즐 선택",
            options=list(CODING_PUZZLES.keys()),
            key="puzzle_selector"
        )
        
        puzzle = CODING_PUZZLES[puzzle_name]
        st.markdown(f"**목표:** {puzzle['description']}")

        if st.button("힌트 보기", key="hint_button"):
            st.session_state.show_hint = True

        if st.session_state.show_hint:
            st.info(f"💡 힌트: {puzzle['hint']}")
        
        st.markdown("### 코드 조각을 순서대로 선택하세요")
        current_order = []
        for i in range(len(puzzle['pieces'])):
            remaining_pieces = [j for j in range(len(puzzle['pieces'])) 
                              if j not in current_order]
            if remaining_pieces:
                options = [f"{j+1}. {puzzle['pieces'][j]}" for j in remaining_pieces]
                options.insert(0, "선택하세요")
                selected = st.selectbox(
                    f"위치 {i+1}",
                    options=options,
                    key=f"pos_{i}"
                )
                if selected != "선택하세요":
                    index = int(selected.split('.')[0]) - 1
                    current_order.append(index)
        
        st.session_state.current_order = current_order
        show_code_preview(puzzle['pieces'], current_order)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("정답 확인", disabled=len(current_order) != len(puzzle['pieces'])):
                if current_order == puzzle['answer']:
                    st.success("🎉 정답입니다!")
                    st.session_state.score = 1
                    st.session_state.selected_questions = [{
                        "question": puzzle['description'],
                        "answer": "\n".join(puzzle['pieces'])
                    }]
                    st.session_state.wrong_answers = []
                else:
                    st.error("다시 시도해보세요.")
                    st.session_state.wrong_answers = [{
                        "question": puzzle['description'],
                        "answer": "\n".join(puzzle['pieces'])
                    }]
        with col2:
            if st.button("초기화"):
                st.session_state.current_order = []
                st.rerun()
    
    with tab2:
        st.subheader("디버깅 퀴즈")
        debug_puzzle = list(DEBUG_PUZZLES.values())[0]
        
        st.markdown(f"**문제:** {debug_puzzle['description']}")
        st.code(debug_puzzle['buggy_code'], language='python')
        
        selected_answer = st.radio(
            "버그를 고치기 위한 올바른 해결책은?",
            debug_puzzle['options']
        )
        
        if st.button("답변 제출"):
            answer_index = debug_puzzle['options'].index(selected_answer)
            if answer_index == debug_puzzle['correct']:
                st.success("🎉 정답입니다!")
                st.info(f"설명: {debug_puzzle['explanation']}")
                st.session_state.score = 1
                st.session_state.selected_questions = [{
                    "question": debug_puzzle['description'],
                    "answer": debug_puzzle['options'][debug_puzzle['correct']]
                }]
                st.session_state.wrong_answers = []
            else:
                st.error("다시 시도해보세요.")
                st.session_state.wrong_answers = [{
                    "question": debug_puzzle['description'],
                    "answer": debug_puzzle['options'][debug_puzzle['correct']]
                }]

    # 결과 페이지로 이동 버튼
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 다시 시도"):
            st.session_state.current_order = []
            st.session_state.show_hint = False
            st.rerun()
    with col2:
        if st.button("📊 결과 보기"):
            st.switch_page("pages/Results.py")
    with col3:
        if st.button("🏠 홈으로"):
            st.switch_page("pages/Main.py")

if __name__ == "__main__":
    main()