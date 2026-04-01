import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# 타빌리 클라이언트 연결
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def fetch_real_time_jobs(keyword="건축설계 신입 채용"):
    print(f"🔎 '{keyword}'로 실시간 공고 검색 중...")

    # AI 에이전트를 위해 최적화된 검색 실행
    response = tavily.search(
        query=keyword,
        search_depth="advanced",
        max_results=5,
        include_raw_content=True
    )

    jobs = []
    for result in response['results']:
        jobs.append({
            "title": result['title'],
            "company": "실시간 검색 결과",
            "content": result['content'],
            "link": result['url']
        })

    return jobs


# --- 에러 방지를 위한 코드 (중요!) ---
MOCK_JOBS = []  # app.py가 이 이름을 찾고 있어서 일단 만들어둡니다.