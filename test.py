import streamlit as st
import random

# MBTI 기본 학습법 템플릿
mbti_base = {
    "INTJ": "시험 전 전체 범위를 큰 틀에서 정리하고, 세부 목표를 하루 단위로 나눠 집중하세요.",
    "ENFP": "다양한 학습 자료를 활용하고, 짧고 집중된 세션으로 학습하세요.",
    "ISTJ": "체크리스트를 만들어 빠진 부분이 없도록 하고, 반복 학습으로 정확성을 높이세요.",
    "ESFP": "즐거운 환경에서 공부하며, 게임화된 학습이나 퀴즈 앱을 활용하세요."
    # 나머지 MBTI도 필요시 추가
}

# 학습 환경
environments = ["조용한 개인 공간", "카페/활기찬 공간", "친구랑 같이"]

# 성격 스타일
personalities = ["계획형", "즉흥형", "협동형"]

# 144개 조합 학습법 생성
recommendations = {}
for mbti, base_tip in mbti_base.items():
    for env in environments:
        for personality in personalities:
            tip = base_tip
            if env == "카페/활기찬 공간":
                tip += " 카페나 활기찬 공간에서 짧고 집중된 세션을 활용하세요."
            elif env == "친구랑 같이":
                tip += " 친구와 함께 스터디 세션을 진행하면 동기부여가 됩니다."
            else:
                tip += " 조용한 개인 공간에서 혼자 집중하면 효율이 높습니다."
            
            if personality == "계획형":
                tip += " 하루 학습 계획과 체크리스트를 세워 실천하세요."
            elif personality == "즉흥형":
                tip += " 흥미와 직감에 따라 유연하게 학습하세요."
            else:
                tip += " 스터디 그룹이나 설명하기를 통해 학습 내용을 공유하세요."
            
            # 색상 강조
            tip = tip.replace("전체 범위", "<span style='color:blue'>전체 범위</span>")
            tip = tip.replace("핵심 개념", "<span style='color:blue'>핵심 개념</span>")
            tip = tip.replace("체크리스트", "<span style='color:green'>체크리스트</span>")
            tip = tip.replace("스터디 그룹", "<span style='color:orange'>스터디 그룹</span>")
            
            recommendations[(mbti, env, personality)] = tip

# 랜덤 동기부여 메시지
motivation_msgs = [
    "🔥 오늘도 한 걸음! 작은 성취가 큰 변화를 만듭니다!",
    "💪 포기하지 마세요! 집중한 시간은 결코 배신하지 않습니다!",
    "✨ 지금 이 순간의 노력이 미래의 나를 만듭니다!",
    "🚀 끝까지 해내는 힘, 당신에게 있습니다!"
]

# 공통 랜덤 꿀팁
extra_tips = [
    "💡 50분 공부 + 10분 휴식 루틴으로 집중력 유지!",
    "💡 시험 전날엔 충분한 수면 확보가 최고의 공부법!",
    "💡 기출문제를 소리 내어 설명하면 기억이 오래남아요!",
    "💡 오답노트에 '틀린 이유'까지 기록하세요!"
]

# Streamlit 앱
st.title("📘 맞춤형 시험기간 학습법 & 동기부여")
st.write("👉 MBTI, 학습 환경, 성격 스타일 선택 → 맞춤 학습법 + 랜덤 동기부여!")

# 사용자 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_base.keys()))
environment = st.selectbox("선호하는 학습 환경은?", environments)
personality = st.selectbox("성격 스타일은?", personalities)

# 결과 출력
key = (mbti, environment, personality)
st.markdown("---")
st.subheader("✨ 맞춤 학습법 카드")

if key in recommendations:
    st.markdown(
        f"""
        <div style="background-color:#f0f8ff;
                    padding:15px;
                    border-radius:12px;
                    box-shadow:2px 2px 6px rgba(0,0,0,0.1);
                    font-size:16px;">
            {recommendations[key]}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("아직 이 조합에 대한 학습법 데이터가 없습니다. 기본적으로 기출문제와 요약 정리를 추천합니다.")

# 랜덤 동기부여 버튼
st.markdown("### 🎯 오늘의 동기부여 메시지")
if st.button("동기부여 받기!"):
    msg = random.choice(motivation_msgs)
    st.success(msg)
    st.balloons()  # 보너스 애니메이션

# 랜덤 꿀팁 버튼
st.markdown("### 🎁 오늘의 보너스 꿀팁")
if st.button("꿀팁 받기!"):
    st.info(random.choice(extra_tips))
