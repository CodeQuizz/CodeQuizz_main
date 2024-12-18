import streamlit as st
import base64
import os
import json
import calendar
from datetime import datetime, date

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
            if st.button("\ub85c\uadf8\uc544\uc6c3", key="logout_button"):
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

# How To Use 설명서 이미지
def show_how_to_use():
    how_to_use_image_path = "assets/How To Use.png"  # 이미지 파일 경로
    if os.path.exists(how_to_use_image_path):
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

def check_attendance():
    # 로그인 여부 확인
    if not st.session_state.get("logged_in"):
        st.markdown('<p style="color:black;">🚨 로그인 후 이용 가능합니다. 🚨</p>', unsafe_allow_html=True)
        return

    # 사용자 데이터 파일 경로
    attendance_file = "data/attendance.json"

    # 출석 기록 로드 (없으면 생성)
    try:
        with open(attendance_file, "r") as f:
            attendance_records = json.load(f)
    except FileNotFoundError:
        attendance_records = {}

    username = st.session_state['username']
    today = date.today().isoformat()

    # 오늘 이미 출석체크했는지 확인
    if username in attendance_records and today in attendance_records[username]:
        st.markdown('<p style="color:black;">✅ 오늘은 이미 출석 체크하셨습니다! ✅</p>', unsafe_allow_html=True)
        
        # 달력 표시
        show_attendance_calendar(attendance_records.get(username, []))
        return

    # 출석 체크 처리
    if username not in attendance_records:
        attendance_records[username] = []

    attendance_records[username].append(today)

    # 출석 기록 저장
    with open(attendance_file, "w") as f:
        json.dump(attendance_records, f, indent=4)

    # 연속 출석 일수 계산
    consecutive_days = calculate_consecutive_attendance(attendance_records[username])

    # 달력 표시
    show_attendance_calendar(attendance_records[username])

    st.success(f"출석 체크 완료! 🎉\n" 
               f"현재 연속 출석 일수: {consecutive_days}일 👍")

def show_attendance_calendar(attendance_dates):
    # 출석 날짜를 날짜 객체로 변환
    attendance_dates = [datetime.fromisoformat(date_str).date() for date_str in attendance_dates]

    # 현재 연도와 월 가져오기
    now = datetime.now()
    year = now.year
    month = now.month

    # 오늘 날짜 가져오기
    today = date.today()

    # 달력 생성
    cal = calendar.monthcalendar(year, month)
    
    # 달력 HTML 생성
    st.markdown(f"<h2 style='color: black;'>{year}년 {month}월 출석 현황</h2>", unsafe_allow_html=True)
    
    # 달력 테이블 생성
    calendar_html = "<table style='width:100%; border-collapse: collapse; background-color: black;'>"
    calendar_html += "<tr style='background-color: #333;'>"
    for day in ['월', '화', '수', '목', '금', '토', '일']:
        calendar_html += f"<th style='border: 1px solid #ddd; padding: 8px; color: white;'>{day}</th>"
    calendar_html += "</tr>"

    for week in cal:
        calendar_html += "<tr>"
        for day in week:
            if day == 0:  # 빈 날짜
                calendar_html += "<td style='border: 1px solid #ddd; padding: 8px; background-color: black;'></td>"
            else:
                current_date = date(year, month, day)
                
                # 스타일 설정
                if current_date in attendance_dates:
                    # 출석 체크한 날짜
                    style = "background-color: yellow; color: black; font-weight: bold;"
                elif current_date == today:
                    # 오늘 날짜
                    style = "background-color: white; color: black; font-weight: bold;"
                else:
                    # 다른 날짜
                    style = "background-color: black; color: white;"
                
                calendar_html += f"<td style='border: 1px solid #ddd; padding: 8px; {style}'>{day}</td>"
        calendar_html += "</tr>"
    
    calendar_html += "</table>"
    
    st.markdown(calendar_html, unsafe_allow_html=True)

def main():
    # 세션 상태 초기화
    if 'show_image' not in st.session_state:
        st.session_state.show_image = False  # 이미지 표시 여부 상태 초기화

    # 배경 이미지 설정
    assets_dir = "assets"
    background_image_file = os.path.join(assets_dir, "coding.png")
    if os.path.exists(background_image_file):
        set_background(background_image_file)

    navbar()

    st.markdown("<h1 style='color: black;'>Welcome to Programming Quiz! 🚀</h1>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color: black;'>
    ### 프로그래밍 실력을 테스트해보세요!
    다양한 난이도의 퀴즈로 실력을 향상시켜보세요.
    </p>
    """, unsafe_allow_html=True)
    
    # How to Use 버튼 클릭 시 이미지 토글
    if st.button("How to Use (사용 방법)", use_container_width=True, key="how_to_use_button"):
        st.session_state.show_image = not st.session_state.show_image  # 상태 토글

    if st.session_state.show_image:
        show_how_to_use()

    # 출석 체크 버튼 추가
    if st.button("📅 출석 체크", use_container_width=True, key="attendance_check_button"):
        check_attendance()

    # 시작하기 버튼
    if st.button("시작하기 ▶️", use_container_width=True, key="start_quiz_button"):
        st.switch_page("pages/Login.py")

if __name__ == "__main__":
    main()