import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# API 키 설정 오류 수정 (환경변수 이름만 넣어야 합니다)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_match_report(user_spec, job):
    # 모델 설정 (Flash-Lite 등 최신 모델 권장)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # 전문가급 프롬프트 설계
    prompt = f"""
    당신은 대한민국 최고의 '건설/건축 전문 커리어 컨설턴트'이자 헤드헌터입니다.
    사용자의 스펙과 채용 공고의 본문을 분석하여, 단순한 매칭을 넘어 '전략적 합격 가이드'를 제시하세요.

    [사용자 프로필]
    {user_spec}

    [채용 공고 상세]
    - 공고명: {job['title']}
    - 회사: {job.get('company', '정보 없음')}
    - 본문 내용: {job.get('content', '상세 내용 없음')}

    ---
    [분석 지침]
    1. 역량 일치도: 건축기사, 건설안전기사 등 필수 자격증 유무와 BIM(Revit), 공정관리 역량을 최우선으로 검토하세요.
    2. 직무 적합성: 사용자의 희망 직무와 공고의 실제 업무 내용(NCS 직무 체계 기준)이 얼마나 일치하는지 분석하세요.
    3. 실질적 조언: 단순히 부족한 점을 나열하지 말고, 면접에서 강조할 '강점'과 서류에서 보완할 '키워드'를 제안하세요.

    [출력 형식 (Markdown 적용)]
    ## 📊 매칭 적합도: [0~100점]%

    ### ✅ 핵심 매칭 포인트 (Strong Points)
    * (사용자의 역량 중 공고와 가장 잘 맞는 부분 3가지를 구체적으로 언급)

    ### ⚠️ 전략적 보완점 (Gap Analysis)
    * (현재 부족한 자격증이나 기술적 경험을 짚어주고, 어떻게 대체 보완할지 제시)

    ### 💡 1급 비밀 합격 팁
    * (이 회사 혹은 이 직무 면접에서 반드시 어필해야 할 '건축학적 인사이트' 한 줄 제안)
    ---
    결과는 건축공학 전공자에게 신뢰감을 줄 수 있도록 전문 용어를 사용하여 정중하게 작성하세요.
    """

    # AI 호출 및 결과 반환
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ 분석 중 오류가 발생했습니다: {str(e)}"