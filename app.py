import streamlit as st
# MOCK_JOBS 대신 실시간 검색 함수를 가져옵니다.
from job_data import fetch_real_time_jobs, MOCK_JOBS
from analyzer import get_match_report

st.set_page_config(page_title="나의 AI 취업 비서", layout="wide")
st.title("🏗️ 실시간 AI 채용 공고 에이전트")

# --- 왼쪽 사이드바: 정보 입력 ---
st.sidebar.header("👤 내 프로필 등록")
user_spec = st.sidebar.text_area(
    "내 스펙 및 희망 직무",
    "예: 건축공학 전공, 건축기사 자격증 보유, BIM 설계 직무 희망",
    height=200
)

st.sidebar.markdown("---")
st.sidebar.header("🔍 검색 설정")
# 검색 키워드를 사용자가 직접 정할 수 있게 합니다.
search_keyword = st.sidebar.text_input("검색 키워드", "건축공학 신입 채용")

# --- 메인 화면: 공고 분석 ---
if st.button("🚀 실시간 공고 사냥 시작"):
    if not user_spec or len(user_spec) < 10:
        st.warning("먼저 왼쪽 사이드바에 상세한 스펙을 입력해 주세요!")
    else:
        with st.spinner(f"'{search_keyword}' 관련 최신 공고를 Tavily가 찾고 있습니다..."):
            # 1. 실시간 데이터 가져오기
            real_jobs = fetch_real_time_jobs(search_keyword)

            if not real_jobs:
                st.error("앗! 검색 결과가 없습니다. 키워드를 조금 바꿔보세요.")
            else:
                st.success(f"현재 가장 핫한 공고 {len(real_jobs)}개를 찾았습니다!")

                # 2. 결과 출력 (가로 칸 나누기 대신 세로 리스트 방식이 가독성이 좋습니다)
                for i, job in enumerate(real_jobs):
                    with st.container():
                        st.markdown(f"### {i + 1}. {job['title']}")
                        col1, col2 = st.columns([1, 4])

                        with col1:
                            st.write(f"🏢 **회사**: {job['company']}")
                            st.write(f"🔗 [공고 원문 보기]({job['link']})")

                        with col2:
                            # AI 분석 보고서 출력
                            # analyzer.py의 get_match_report가 job['content']를 잘 쓰도록 전달합니다.
                            with st.expander("🤖 AI 매칭 분석 보고서 보기", expanded=True):
                                report = get_match_report(user_spec, job)
                                st.write(report)
                        st.markdown("---")

# 초기 화면 안내
if not st.session_state.get('searched', False):
    st.info("왼쪽에 스펙을 입력하고 버튼을 누르면, 실시간으로 채용 정보를 긁어와 분석해 드립니다.")