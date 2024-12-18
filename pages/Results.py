# pages/Results.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def navbar():
    col1, col2, col3 = st.columns([6, 3, 1])
    with col1:
        st.markdown("🏠 Home > Login > Quiz > Results")
    with col2:
        if st.session_state.get("logged_in"):
            st.write(f"👤 {st.session_state.get('nickname', st.session_state['name'])}님")
    with col3:
        if st.session_state.get("logged_in"):
            if st.button("로그아웃"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.session_state["logged_in"] = False
                st.session_state["username"] = None
                st.session_state["name"] = None
                st.switch_page("pages/Login.py")

def main():
    navbar()
    if not st.session_state.get("logged_in", False):
        st.warning("로그인이 필요합니다.")
        if st.button("로그인 페이지로 이동"):
            st.switch_page("pages/Login.py")
        return

    st.title("📊 퀴즈 결과")
    
    score = st.session_state.get("score", 0)
    total_questions = len(st.session_state.get("selected_questions", []))
    wrong_answers = st.session_state.get("wrong_answers", [])
    
    if total_questions > 0:
        score_percentage = (score / total_questions) * 100
    else:
        score_percentage = 0

    st.markdown(f"#### 점수: {score}/{total_questions} ({score_percentage:.1f}%)")

    feedback = ""
    if score_percentage == 100:
        feedback = "💯 **매우 잘하고 있습니다. 지식이 탄탄하시네요!**"
    elif score_percentage >= 80:
        feedback = "🌟 **지식이 탄탄하시네요! 조금만 더 공부하시면 될 거 같습니다.**"
    elif score_percentage >= 60:
        feedback = "💪 **열심히 정진하시면 좋은 결과를 얻을 수 있을거에요!**"
    elif score_percentage >= 40:
        feedback = "📚 **발전 가능성이 있습니다. 충분히 공부하면 좋아질 수 있습니다.**"
    elif score_percentage >= 20:
        feedback = "👨‍🎓 **부족합니다. 충분한 공부를 통해 더 좋은 결과를 얻어봐요.**"
    else:
        feedback = "🔍 **다른 분야를 알아보는 것도 나쁘지 않은 선택입니다!**"

    st.success(feedback)

    st.markdown("### 점수 시각화")

    max_score = 100
    values = [score_percentage]

    angles = np.linspace(0, 2 * np.pi, 100, endpoint=True)
    radius = [score_percentage / max_score] * len(angles)

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, radius, color='teal', alpha=0.4)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(["0", "20", "40", "60", "80", "100"], fontsize=10)
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_title("Your Score", fontsize=15, y=1.1)

    st.pyplot(fig)

    st.markdown("### ❌ 틀린 문제 분석")
    if wrong_answers:
        for i, question in enumerate(wrong_answers):
            with st.expander(f"문제 {i + 1}", expanded=False):
                card = f"""
                <div style="background-color: #f8d7da; border-left: 5px solid #f5c6cb; padding: 10px; margin: 10px 0;">
                    <strong>문제:</strong> {question['question']}<br>
                    <strong>정답:</strong> {question['answer']}
                </div>
                """
                st.markdown(card, unsafe_allow_html=True)
    else:
        st.markdown("모든 문제를 맞추셨습니다! 🎉")


        st.markdown("### 교재 추천")
    def get_books(score_percentage):
        if score_percentage <= 20:
            return [
                {
                    "title": "(점프 투) 파이썬",
                    "author": "박응용",
                    "image": "https://contents.kyobobook.co.kr/sih/fit-in/400x0/pdt/9791163034735.jpg",
                    "청구기호": "005.133 박68ㅍ 2019",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "혼자 공부하는 파이썬",
                    "author": "윤인성",
                    "image": "https://image.yes24.com/goods/109625396/XL",
                    "청구기호": "005.133 윤69ㅎ",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "(으뜸) 파이썬",
                    "author": "박동규/강영민",
                    "image": "https://image.yes24.com/goods/89140722/XL",
                    "청구기호": "005.133 박24ㅍ",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
            ]
        elif score_percentage <= 60:
            return [
                {
                    "title": "파이썬 코딩의 기술 : 똑똑하게 코딩하는 법",
                    "author": "Slatkin Brett",
                    "image": "https://gimg.gilbut.co.kr/book/BN002890/rn_view_BN002890.jpg",
                    "청구기호": "005.133 Sl1eH",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "Python cookbook",
                    "author": "Beazley David M. Jones Brian K.",
                    "image": "https://contents.kyobobook.co.kr/sih/fit-in/400x0/pdt/9788992649681.jpg",
                    "청구기호": "005.133 B38pyH 2013",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "파이썬 알고리즘 인터뷰 = Coding interview : 95가지 알고리즘 문제 풀이로 완성하는 코딩 테스트",
                    "author": "박상길",
                    "image": "https://image.yes24.com/goods/91084402/XL",
                    "청구기호": "005.133 박51ㅍ",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
            ]
        else:
            return [
                {
                    "title": "파이썬 웹 프로그래밍 : Django(장고)로 배우는 쉽고 빠른 웹 개발",
                    "author": "김석훈",
                    "image": "https://www.hanbit.co.kr/data/books/B4329597070_l.jpg",
                    "청구기호": "005.133 김532ㅍ 2018",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "전문가를 위한 파이썬",
                    "author": "Ramalho Luciano",
                    "image": "https://contents.kyobobook.co.kr/sih/fit-in/458x0/pdt/9788968484988.jpg",
                    "청구기호": "005.133 R14fH",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
                {
                    "title": "슬기로운 파이썬 트릭 : 짧고 흥미로운 코드로 배우는 파이썬 실용 코딩",
                    "author": "Dan Bader",
                    "image": "https://contents.kyobobook.co.kr/sih/fit-in/400x0/pdt/9788966262342.jpg",
                    "청구기호": "005.133 B14pH",
                    "소장처": "일송기념도서관/(3층)사회/자연과학자료실/"
                },
            ]
    recommended_books = get_books(score_percentage)
    cols = st.columns(3)
    with st.expander("📖 추천 교재 보기"):
        cols = st.columns(3)
        for idx, book in enumerate(recommended_books):
            with cols[idx % 3]:
                st.image(book['image'], width=150)
                st.write(f"**{book['title']}**")
                st.write(f"**저자**: {book['author']}")
                st.write(f"**청구기호**: {book['청구기호']}")
                st.write(f"**소장처**: {book['소장처']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 다시 풀기"):
            st.session_state.quiz_started = False
            st.switch_page("pages/Main.py")
    with col2:
        if st.button("📝 인터랙티브 퀴즈"):
            st.switch_page("pages/Interactive.py")
    with col3:
        if st.button("🏠 홈으로"):
            st.session_state.quiz_started = False
            st.switch_page("pages/Main.py")

if __name__ == "__main__":
    main()