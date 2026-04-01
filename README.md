# 🏗️ Job-Agent: 건축공학도를 위한 AI 채용 매칭 시스템

> **"당신의 스펙과 가장 잘 맞는 공고를 1초 만에 찾아드립니다."**
> 본 프로젝트는 고용24 채용 데이터를 기반으로, 제미나이(Gemini) AI가 사용자의 역량을 분석하여 최적의 건설/설계/안전 분야 공고를 매칭해주는 지능형 에이전트입니다.

---

## 🌟 주요 기능 (Core Features)

* **🎯 지능형 매칭 엔진**: 사용자의 전공, 자격증(건축기사, 산업안전기사 등), 경력을 분석하여 공고와의 적합성 점수 산출
* **⚡ 광속 배치 처리 (Batch)**: 여러 개의 채용 공고를 한 번에 분석하여 대기 시간 최소화
* **📑 AI 컨설팅 보고서**: 매칭 이유와 함께 합격 확률을 높이기 위한 맞춤형 보완 전략 제안
* **💻 직관적인 UI**: Streamlit을 활용한 웹 대시보드 제공

## 🛠️ 기술 스택 (Tech Stack)

* **Language**: Python 3.10+
* **AI Engine**: Google Gemini 2.0 / 2.5 Flash API
* **Framework**: Streamlit (Web UI)
* **Environment**: python-dotenv, Git / GitHub

## ⚙️ 시작하기 (How to Start)

팀원분들은 아래 순서대로 환경을 설정해 주세요.

### 1. 저장소 복제 (Clone)
```bash
git clone https://github.com/JUNWON0404/Job-Agent.git
cd Job-Agent 
```
### 2. 가상환경 구축 및 라이브러리 설치
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### 3. API 키 설정 (보안 주의!)
프로젝트 루트 폴더에 .env 파일을 생성하고 본인의 API 키를 입력하세요.
```
GEMINI_API_KEY=여러분의_API_키_입력
```

### 4. 실행
```
streamlit run app.py
```