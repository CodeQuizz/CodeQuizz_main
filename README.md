# CodeQuizz_main

오픈소스 3조 코드 퀴즈🔥

코드퀴즈입니다.

20205151 김태호<br>
정은수<br>
20205275 홍성민<br>
20225204 윤예준<br>

# Programming Quiz Project

프로그래밍 지식을 테스트할 수 있는 퀴즈 웹 애플리케이션입니다. 사용자는 난이도별로 프로그래밍 관련 퀴즈를 풀고 결과를 분석할 수 있습니다.

## 프로젝트 구조

```
project_root/
├── pages/
│   ├── 1_👋_Intro.py        # 인트로 페이지
│   ├── 2_🔐_Login.py        # 로그인/회원가입 페이지
│   ├── 3_📝_Quiz.py         # 메인 퀴즈 페이지
│   └── 4_📊_Results.py      # 결과 분석 페이지
├── utils/
│   ├── session_state.py     # 세션 관리
│   ├── quiz_data.py         # 퀴즈 데이터 관리
│   └── analytics.py         # 결과 분석
├── data/                    # JSON 데이터 파일들
├── assets/                  # 이미지 및 스타일 파일
└── Home.py                  # 메인 앱
```

## 시작하기

### 필수 요구사항

- Python 3.8 이상
- Git

### 설치 방법

1. 저장소 클론하기

```bash
git clone <repository-url>
cd <project-directory>
```

2. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

4. 애플리케이션 실행

```bash
streamlit run Home.py
```

### 개발 시 주의사항

1. 새로운 기능 개발 시

```bash
# 새로운 브랜치 생성
git checkout -b feature/기능이름

# 작업 완료 후
git add .
git commit -m "커밋 메시지"
git push origin feature/기능이름
```

2. 새로운 패키지 설치 시

```bash
pip install 패키지이름
pip freeze > requirements.txt
```

## 팀원 역할

- 윤예준: Intro 페이지
- 김태호: 로그인/회원가입 기능
- 정은수: 퀴즈 로직 및 데이터
- 홍성민: 결과 분석 및 시각화

## 기술 스택

- Frontend: Streamlit
- Data Visualization: Plotly
- Data Management: JSON files
- Version Control: Git
- Environment: venv

## 문의

프로젝트 관련 문의사항은 Issues 탭에 등록해주세요.
