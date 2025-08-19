import streamlit as st

# MBTI별 직업 추천 데이터 예시
mbti_jobs = {
    "INTJ": ["과학자", "전략가", "데이터 분석가"],
    "INTP": ["철학자", "프로그래머", "연구원"],
    "ENTJ": ["CEO", "변호사", "경영 컨설턴트"],
    "ENTP": ["기업가", "광고 기획자", "언론인"],
    "INFJ": ["작가", "상담가", "심리학자"],
    "INFP": ["예술가", "작곡가", "사회복지사"],
    "ENFJ": ["교사", "코치", "인사 담당자"],
    "ENFP": ["배우", "기자", "마케터"],
    "ISTJ": ["회계사", "판사", "군인"],
    "ISFJ": ["간호사", "교사", "사회복지사"],
    "ESTJ": ["경영자", "공무원", "프로젝트 매니저"],
    "ESFJ": ["간호사", "상담사", "교육자"],
    "ISTP": ["엔지니어", "파일럿", "스포츠 코치"],
    "ISFP": ["디자이너", "음악가", "사진작가"],
    "ESTP": ["영업가", "스포츠 선수", "기업가"],
    "ESFP": ["배우", "MC", "이벤트 플래너"]
}

# Streamlit UI
st.title("🎯 MBTI 기반 진로 추천 사이트")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 추천 결과 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형에 추천하는 직업")
    jobs = mbti_jobs[selected_mbti]
    for job in jobs:
        st.write(f"- {job}")
