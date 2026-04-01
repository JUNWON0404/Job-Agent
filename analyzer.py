import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("model = genai.GenerativeModel('gemini-flash-latest')"))


def get_match_report(user_spec, job):
    model = genai.GenerativeModel('gemini-flash-latest')

    prompt = f"""
    당신은 커리어 컨설턴트입니다. 아래 사용자의 스펙과 채용 공고를 비교해서 분석해주세요.

    [사용자 스펙]: {user_spec}
    [채용 공고]: {job['title']} - {job['description']} (필수사항: {job['requirements']})

    결과를 다음 형식으로 출력하세요:
    1. 매칭 점수: (0~100점)
    2. 추천 이유: (짧게 3가지)
    3. 보완하면 좋은 점: (1가지)
    """

    response = model.generate_content(prompt)
    return response.text