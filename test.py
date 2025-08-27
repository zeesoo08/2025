import streamlit as st

# 웹앱 제목
st.title("🦷 오늘의 양치 체크 앱 🪥✨")

st.write("오늘 하루 양치를 몇 번 했나요? 선택해보세요! 😁")

# 양치 횟수 선택 (1, 2, 3번)
brushing = st.radio(
    "양치 횟수를 선택하세요 👇",
    [1, 2, 3],
    index=0
)

# 버튼 클릭 후 결과 출력
if st.button("확인하기 ✅"):
    if brushing == 1:
        st.warning("🦷 노력해! 내일은 조금 더 해보자 💪")
        st.image(
          " https://everysmile.co.za/blog/what-are-the-signs-of-early-tooth-decay/이미지파일이름.jpg"

        "⚠️ 양치를 게을리하면 이렇게 될 수 있어요!",
            use_column_width=True
        )
    elif brushing == 2:
        st.info("😃 잘하고 있어! 조금만 더 하려고 노력하자 ✨")
    elif brushing == 3:
        st.success("👏 정말 잘했어! 입안이 개운하겠는걸?! 🌟🪥")
        st.balloons()  # 🎉 3번일 때만 폭죽 효과
        st.image(
            "https://images.pexels.com/photos/52527/teeth-smile-dental-health-mouth-52527.jpeg",  
            caption="✨ 건강하고 깨끗한 치아예요!",
            use_column_width=True
        )
