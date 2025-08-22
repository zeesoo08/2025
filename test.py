import streamlit as st

# 페이지 설정
st.set_page_config(page_title="양치 체크", page_icon="🪥", layout="centered")

# 사용자 정의 스타일
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
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

# 타이틀
st.markdown('<div class="title">🦷 오늘의 양치 체크</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">치아 건강을 위해 하루 3번 이상 양치했는지 확인해보세요!</div>', unsafe_allow_html=True)

# 애니메이션 이미지
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTZkZjg4MGEwNzk3Nzc4NzQ1ODUzNjA2ZTY2NTRjNDViYjNjOGVmMCZjdD1n/WS7h9vfJ3gyUElFxYJ/giphy.gif", width=300)

# 입력
count = st.number_input("오늘 양치한 횟수를 입력하세요 🪥", min_value=0, max_value=10, step=1)

# 버튼 누르면 결과 보여주기
if st.button("결과 확인"):
    if count <= 3:
        st.error("😬 하루에 양치를 3번 이하로 했어요! 조금 더 노력해봐요!")
        st.info("💡 하루 3번 이상 양치하면 충치 예방에 도움이 돼요.")
    else:
        st.success("😁 완벽해요! 오늘도 상쾌한 입속을 유지했네요!")

# 하단 문구
st.markdown("---")
st.markdown("<center><small>🦷 건강한 치아는 꾸준한 관리에서 시작됩니다.</small></center>", unsafe_allow_html=True)
