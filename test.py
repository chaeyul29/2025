import streamlit as st
import random

# 🎨 다크 모드 색상 팔레트
BG_COLOR = "#1E1E2F"        # 어두운 배경
CARD_COLOR = "#2C2C3E"      # 카드용 짙은 회색
TIP_COLOR = "#3B3B4F"       # 보너스 꿀팁용 진한 남색
PRIMARY_COLOR = "#8B5CF6"   # 보라색 포인트
TEXT_COLOR = "#EDEDED"      # 밝은 글씨

# MBTI 기본 학습법 템플릿
mbti_base = {
    "INTJ": "시험 전 전체 범위를 큰 틀에서 정리하고, 세부 목표를 하루 단위로 나눠 집중하세요.",
    "INTP": "핵심 개념 위주로 정리하고, 이론과 실제 문제를 연결해 이해하세요.",
    "ENTJ": "시간표를 짜고, 과목별로 학습 블록을 배치하며 중간 점검을 진행하세요.",
    "ENTP": "토론식 학습이나 스터디 그룹에서 아이디어를 주고받으세요.",
    "INFJ": "큰 그림을 먼저 이해하고, 중요한 키워드를 스스로에게 설명하며 학습하세요.",
    "INFP": "흥미 있는 부분부터 시작해 동기를 끌어올리고, 필수 과목으로 확장하세요.",
    "ENFJ": "함께 공부하며 설명하기를 통해 학습을 정리하세요.",
    "ENFP": "다양한 학습 자료를 활용하고, 짧고 집중된 세션으로 학습하세요.",
    "ISTJ": "체크리스트를 만들어 빠진 부분이 없도록 하고, 반복 학습으로 정확성을 높이세요.",
    "ISFJ": "계획표를 세워 꾸준히 실천하고, 필수 단원부터 시작해 안정감을 확보하세요.",
    "ESTJ": "명확한 목표를 설정하고 실질적인 예제를 중심으로 학습하세요.",
    "ESFJ": "함께 공부하며 서로 질문을 주고받고, 퀴즈 형식 복습을 활용하세요.",
    "ISTP": "실습 문제를 직접 풀고, 이론을 문제에 적용하며 학습하세요.",
    "ISFP": "관심 있는 주제부터 시작해 몰입하고, 시각 자료와 함께 학습하세요.",
    "ESTP": "프로젝트식 학습이나 문제풀이를 반복하고, 즉각적인 피드백을 활용하세요.",
    "ESFP": "즐거운 환경에서 공부하며, 게임화된 학습이나 퀴즈 앱을 활용하세요."
}

# 학습 환경
environments = ["🏠 조용한 개인 공간", "☕ 카페/활기찬 공간", "👫 친구랑 같이"]

# 성격 스타일
personalities = ["📋 계획형", "🎲 즉흥형", "🤝 협동형"]

# 조합별 추천 생성
recommendations = {}
for mbti, base_tip in mbti_base.items():
    for env in environments:
        for personality in personalities:
            tip = base_tip
            if "카페" in env:
                tip += " 카페에서는 짧고 집중된 세션을 활용하세요."
            elif "친구" in env:
                tip += " 친구와 함께 스터디 세션을 진행하면 동기부여가 됩니다."
            else:
                tip += " 조용한 개인 공간에서는 혼자 집중하면 효율이 높습니다."
            
            if "계획형" in personality:
                tip += " 하루 계획과 체크리스트를 세워 실천하세요."
            elif "즉흥형" in personality:
                tip += " 흥미와 직감을 따라 유연하게 학습하세요."
            else:
                tip += " 스터디 그룹에서 서로 가르치며 배우세요."

            recommendations[(mbti, env, personality)] = tip

# 랜덤 꿀팁
extra_tips = [
    "🌟 50분 공부 + 10분 휴식 루틴으로 집중력 유지!",
    "😴 시험 전날엔 충분한 수면이 최고의 공부법!",
    "🗣 기출문제를 소리 내어 설명하면 기억이 오래 남아요!",
    "📝 오답노트에 '틀린 이유'까지 기록하세요!"
]

# CSS로 전체 배경과 텍스트 색상 변경
st.markdown(
    f"""
    <style>
        body {{
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.markdown(f"<h1 style='color:{PRIMARY_COLOR}'>📘 맞춤형 시험기간 학습법 추천</h1>", unsafe_allow_html=True)
st.write("👉 MBTI + 학습 환경 + 성격 스타일을 선택하면 맞춤형 학습법이 나옵니다!")

# 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_base.keys()))
environment = st.selectbox("선호하는 학습 환경은?", environments)
personality = st.selectbox("성격적 학습 스타일은?", personalities)

# 결과 카드
key = (mbti, environment, personality)
st.markdown("---")
st.subheader("✨ 맞춤 학습법 카드")

if key in recommendations:
    st.markdown(
        f"""
        <div style="background-color:{CARD_COLOR};
                    padding:15px;
                    border-radius:12px;
                    font-size:16px;
                    color:{TEXT_COLOR};">
            {recommendations[key]}
        </div>
        """,
        unsafe_allow_html=True
    )

# 랜덤 꿀팁
st.subheader("🎁 오늘의 보너스 꿀팁")
st.markdown(
    f"<div style='background-color:{TIP_COLOR}; padding:12px; border-radius:10px; color:{TEXT_COLOR};'>{random.choice(extra_tips)}</div>",
    unsafe_allow_html=True
)
