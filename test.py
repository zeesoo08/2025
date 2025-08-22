import streamlit as st

# 페이지 설정
st.set_page_config(page_title="양치 체크", page_icon="🪥", layout="centered")

# 사용자 정의 스타일
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        color: #2b6cb0;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #4a5568;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #2b6cb0;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀 & 설명
st.markdown('<div class="title">🦷 오늘의 양치 체크</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">하루 3번 양치하는 습관, 치아 건강을 지켜줍니다!</div>', unsafe_allow_html=True)

# ✅ 양치 이미지 추가
st.image("https://img.freepik.com/free-vector/young-man-brushing-teeth_1308-104614.jpg", width=400, caption="오늘도 양치 잘했나요?")

# 입력 받기
count = st.number_input("오늘 양치한 횟수를 입력하세요 🪥", min_value=0, max_value=10, step=1)

# 결과 확인 버튼
if st.button("결과 확인"):
    if count == 3:
        st.balloons()
        st.success("🎉 완벽해요! 하루 3번 양치 성공!")
        st.markdown("✨ 꾸준한 습관이 치아 건강을 지켜줘요!")
    else:
        st.warning("🪥 하루에 3번 양치하는 걸 목표로 해보세요!")
        st.info("💡 아침, 점심, 저녁 식사 후 양치를 권장합니다.")

# 하단 문구
st.markdown("---")
st.markdown("<center><small>🦷 치아는 평생 함께해야 할 소중한 친구입니다.</small></center>", unsafe_allow_html=True)
