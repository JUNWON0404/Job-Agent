import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. .env 파일에 있는 API 키 로드
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ .env 파일에서 API 키를 찾을 수 없습니다. 파일 경로와 변수명을 확인해주세요!")
else:
    genai.configure(api_key=api_key)

    print("--- 🤖 사용 가능한 Gemini 모델 목록 ---")
    try:
        # 2. 내 API 키로 접근 가능한 모델 리스트 가져오기
        for m in genai.list_models():
            # 텍스트 생성이 가능한 모델만 필터링
            if 'generateContent' in m.supported_generation_methods:
                # 출력되는 이름(m.name)을 잘 보세요!
                # 예: models/gemini-1.5-flash-002 또는 models/gemini-2.0-flash 등
                print(f"모델명: {m.name}")
    except Exception as e:
        print(f"❌ 목록을 가져오는데 실패했습니다: {e}")