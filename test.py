import streamlit as st

# 페이지 설정
st.set_page_config(page_title="양치 체크", page_icon="🪥", layout="centered")

# 스타일
st.markdown("""
    <style>
    .title { text-align: center; font-size: 40px; color: #2b6cb0; }
    .subtitle { text-align: center; font-size: 20px; color: #4a5568; margin-bottom: 30px; }
    .stButton>button { background-color: #2b6cb0; color: white; font-size: 16px; padding: 10px 20px; border-radius: 8px; border: none; }
    </style>
""", unsafe_allow_html=True)

# 제목 및 설명
st.markdown('<div class="title">🦷 오늘의 양치 체크</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">하루 3번 이상 양치하는 습관, 치아 건강의 시작입니다!</div>', unsafe_allow_html=True)

# 이미지
st.image("https://svgrepo.com/show/493416/man-brushing-his-teeth.svg", width=300, caption="거울 앞에서 양치하는 모습")

# 입력 받기
count = st.number_input("오늘 양치한 횟수를 입력하세요 🪥", min_value=0, max_value=10, step=1)

# 버튼 클릭 시 결과 출력
if st.button("결과 확인"):
    if count >= 3:
        st.balloons()
        st.success(f"🎉 잘했어요! 오늘 {count}회 양치했군요! 꾸준한 습관이 치아를 건강하게 해줍니다!")
        st.markdown("✨ 이렇게 열심히 관리하면 건강한 미소를 오래 유지할 수 있어요!")
    else:
        st.warning("🪥 하루 3번 양치를 목표로 해보세요!")
        st.info("💡 아침, 점심, 저녁 식사 후 양치를 권장합니다.")

# 하단 문구
st.markdown("---")
st.markdown("<center><small>🦷 건강한 미소는 꾸준한 관리에서 시작됩니다.</small></center>", unsafe_allow_html=True)
