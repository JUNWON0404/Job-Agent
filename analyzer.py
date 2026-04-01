import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# API 키 설정 오류 수정 (환경변수 이름만 넣어야 합니다)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_match_report(user_spec, job):
    # 모델명은 환경에 맞춰 'gemini-1.5-flash' 또는 'gemini-flash-latest' 사용
    model = genai.GenerativeModel('gemini-flash-latest')

    # 특정 개인의 경험이 아닌, 입력된 'user_spec' 자체를 기준으로 분석하도록 프롬프트 구성
    prompt = f"""
    당신은 건축공학과 전용 채용 컨설턴트입니다. 
    아래 제공된 [학생의 입력 정보]와 [건설워커 채용 공고]를 비교하여 객관적인 분석 보고서를 작성하세요.

    [학생의 입력 정보]
    {user_spec}

    [채용 공고 내용]
    제목: {job['title']}
    내용: {job['content']}

    [분석 요청 사항]
    1. 직무 적합도 점수: (100점 만점 기준)
    2. 주요 매칭 포인트: 학생이 입력한 자격증/기술 중 공고의 요구사항과 일치하는 핵심 요소 2~3가지
    3. 합격 전략 가이드: 이 학생이 해당 공고에 지원할 때 자소서나 면접에서 어떤 '강점'을 우선적으로 내세워야 할지 조언
    4. 부족한 점 보완: 공고의 필수/우대 조건 중 학생에게 부족한 부분이 있다면 무엇인지, 어떻게 단기 보완할지 제안

    ※ 주의: 반드시 제공된 [학생의 입력 정보] 내의 데이터로만 분석하고, 외부의 개인 정보를 추측하여 작성하지 마세요.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"분석 중 오류가 발생했습니다: {str(e)}"