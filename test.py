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
st.markdown('<div class="subtitle">하루 3번 양치한 습관, 치아 건강의 시작입니다!</div>', unsafe_allow_html=True)

# 선택한 이미지 (예: 1번 거울 앞 양치 장면)
st.image("https://img.freepik.com/premium-vector/young-man-brushing-teeth-bathroom-oral-hygiene-care-dental-health_17140668.jpg", width=400)

# 양치 횟수 입력
count = st.number_input("오늘 양치한 횟수를 입력하세요 🪥", min_value=0, max_value=10, step=1)

# 버튼 클릭 시 결과 표시
if st.button("결과 확인"):
    if count == 3:
        st.balloons()
        st.success("🎉 완벽해요! 정확히 하루 3번 양치했어요!")
        st.markdown("✨ 이런 꾸준함이 치아 건강을 지켜줄 거예요!")
    else:
        st.warning("🪥 하루 3번 양치하는 것을 목표로 해보세요!")
        st.info("💡 아침, 점심, 저녁 식사 후 양치를 권장해요.")

# 하단 문구
st.markdown("---")
st.markdown("<center><small>🦷 건강한 미소는 꾸준한 관리에서 시작됩니다.</small></center>", unsafe_allow_html=True)
