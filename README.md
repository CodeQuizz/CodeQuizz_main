# CodeQuizz_main

오픈소스 3조 코드 퀴즈🔥

코드퀴즈입니다.

20205151 김태호<br>
20212361 정은수<br>
20205275 홍성민<br>
20225204 윤예준<br>

# Programming Quiz Project

프로그래밍 지식을 테스트할 수 있는 퀴즈 웹 애플리케이션입니다. 사용자는 난이도별로 프로그래밍 관련 퀴즈를 풀고 결과를 분석할 수 있습니다.

## 프로젝트 구조

```project_root/
├── .github/                 # GitHub 관련 워크플로 및 설정
├── assets/                  # 이미지 및 기타 정적 파일
│   ├── coding.png           # 코딩 관련 이미지
│   └── How_To_Use.png       # 사용 방법 이미지
├── data/                    # JSON 데이터 파일들
│   ├── quiz_questions.json  # 퀴즈 질문 데이터
│   └── users.json           # 사용자 정보 데이터
├── myenv/                   # 가상환경 폴더 (일반적으로 .gitignore에 포함)
├── pages/                   # 개별 페이지 구성
│   ├── Login.py             # 로그인/회원가입 페이지
│   ├── Main.py              # 메인 퀴즈 페이지
│   └── Results.py           # 결과 분석 페이지
├── utils/                   # 유틸리티 모듈
├── .gitignore               # Git에서 무시할 파일 설정
├── LICENSE                  # 프로젝트 라이선스 정보
├── README.md                # 프로젝트 개요 및 설명
└── requirements.txt         # 프로젝트 의존성 목록
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
