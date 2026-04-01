import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# 타빌리 클라이언트 연결
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def fetch_real_time_jobs(keyword="건축공학 신입"):
    # 1. 타겟 사이트 지정 (건설워커, 링커리어 등 핵심 사이트만!)
    # 쿼리 예시: "site:worker.co.kr OR site:linkcareer.com 건축공학 채용"
    target_sites = "site:worker.co.kr OR site:linkcareer.com OR site:saramin.co.kr"
    refined_query = f"{target_sites} {keyword} 2026 채용공고"

    print(f"🚀 {refined_query} 로 정밀 검색을 시작합니다...")

    # 2. Tavily 검색 실행
    response = tavily.search(
        query=refined_query,
        search_depth="advanced",  # 상세 검색 모드
        max_results=3,  # 토큰 절약을 위해 알짜 공고 3개만!
        include_raw_content=False
    )

    jobs = []
    for result in response['results']:
        # 3. 데이터 정제 (불필요한 공백 제거 및 글자수 제한)
        content = result.get('content', '')[:500]
        jobs.append({
            "title": result['title'],
            "company": "채용 사이트 공고",
            "content": content,
            "link": result['url']
        })
    return jobs


# --- 에러 방지를 위한 코드 (중요!) ---
MOCK_JOBS = []  # app.py가 이 이름을 찾고 있어서 일단 만들어둡니다.