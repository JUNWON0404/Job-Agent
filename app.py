import streamlit as st
from job_data import MOCK_JOBS
from analyzer import get_match_report

st.set_page_config(page_title="나의 AI 취업 비서", layout="wide")
st.title("🏗️ 맞춤형 채용 공고 에이전트")

# 왼쪽 사이드바: 내 정보 입력
st.sidebar.header("내 프로필 등록")
user_spec = st.sidebar.text_area("내 스펙을 입력하세요", "예: 건축공학 전공, 산업안전기사 자격증 보유, 안전관리 직무 희망")

# 메인 화면: 공고 분석
if st.button("내게 맞는 공고 찾기"):
    with st.spinner("에이전트가 공고를 분석 중입니다..."):
        cols = st.columns(len(MOCK_JOBS))

        for i, job in enumerate(MOCK_JOBS):
            with cols[i]:
                st.subheader(job['title'])
                st.write(f"🏢 {job['company']} | 📍 {job['location']}")

                # AI 분석 보고서 출력
                report = get_match_report(user_spec, job)
                st.info(report)