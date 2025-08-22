import streamlit as st

st.title("🪥 양치 횟수 체크 앱")

st.write("하루 동안 양치를 몇 번 했나요?")

# 사용자로부터 양치 횟수 입력 받기
count = st.number_input("양치 횟수", min_value=0, max_value=10, step=1)

# 버튼을 눌러야 결과가 나오도록
if st.button("결과 확인"):
    if count <= 3:
        st.warning("⚠️ 하루에 양치를 3번 이하로 했어요. 조금 더 노력해요!")
    else:
        st.success("✅ 잘했어요! 오늘도 입속이 깨끗하네요 :)")

