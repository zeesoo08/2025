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
    elif brushing == 2:
        st.info("😃 잘하고 있어! 조금만 더 하려고 노력하자 ✨")
    elif brushing == 3:
        st.success("👏 정말 잘했어! 입안이 개운하겠는걸?! 🌟🪥")
        st.balloons()  # 🎉 3번일 때만 폭죽 효과

        # 3번일 때만 퀴즈 표시
        st.subheader("❓ 왜 양치를 해야 할까요?")
        quiz_answer = st.radio(
            "정답을 선택하세요 👇",
            [
                "1. 양치는 치아에 쌓인 플라크와 세균을 제거하는 데 도움을 줍니다.",
                "2. 정기적인 양치를 통해 잇몸 건강을 유지하고 질병을 예방할 수 있습니다.",
                "3. 양치를 통해 세균을 제거하면 신선한 입냄새를 유지할 수 있습니다.",
                "4. 양치를 통해 구강 건강을 유지하는 것은 전반적인 건강을 지키는 데도 중요합니다."
            ],
            index=None
        )

        if quiz_answer:
            st.success("🎉 정답입니다! 말씀하신 이유 모두 양치가 꼭 필요한 이유예요 🦷✨")
