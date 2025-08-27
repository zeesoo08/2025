import streamlit as st

st.title("🦷 오늘의 양치 체크 앱 🪥✨")
st.write("오늘 하루 양치를 몇 번 했나요? 선택해보세요! 😁")

brushing = st.radio(
    "양치 횟수를 선택하세요 👇",
    [1, 2, 3],
    index=0
)

if st.button("확인하기 ✅"):
    if brushing == 1:
        st.warning("🦷 노력해! 내일은 조금 더 해보자 💪")
        st.image(
            "https://avangartclinic.com/how-d.../before.jpg",
            caption="⚠️ 이렇게 심하게 썩을 수 있어요!",
            use_column_width=True
        )
    elif brushing == 2:
        st.info("😃 잘하고 있어! 조금만 더 하려고 노력하자 ✨")
        st.image(
            "https://avangartclinic.com/how-d.../before.jpg",
            caption="❗ 충치가 진행될 수 있어요!",
            use_column_width=True
        )
    elif brushing == 3:
        st.success("👏 정말 잘했어! 입안이 개운하겠는걸?! 🌟🪥")
        st.balloons()
        st.image(
            "https://example.com/clean_teeth.jpg",
            caption="✨ 건강하고 깨끗한 치아예요!",
            use_column_width=True
        )
