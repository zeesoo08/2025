import streamlit as st

# 질문 예시 (심플하게 샘플만)
questions = [
    ("😎 나는 사람들과 함께 있을 때 에너지를 얻는다!", "E", "I"),
    ("📅 나는 즉흥적이기보다 계획적인 편이다!", "J", "P"),
    ("💭 나는 현실보다 상상에 더 끌린다!", "N", "S"),
    ("❤️ 나는 논리보다 감정을 더 중시한다!", "F", "T"),
]

careers = {
    "ENTJ": ["👑 리더십 직업", "💼 CEO", "🎤 정치가"],
    "INFJ": ["🧘 상담가", "📚 작가", "👩‍🏫 교사"],
    "ISTP": ["⚙️ 엔지니어", "✈️ 파일럿", "🔬 연구원"],
}


def main():
    st.set_page_config(page_title="MBTI Career Finder 🌈", layout="wide")

    st.markdown(
        """
        <h1 style='text-align: center; font-size: 60px;'>🌟 MBTI 기반 진로 탐험 🚀</h1>
        <p style='text-align: center; font-size: 24px;'>✨ 성격 유형을 통해 나만의 꿈을 찾아보자! ✨</p>
        """,
        unsafe_allow_html=True,
    )

    if "answers" not in st.session_state:
        st.session_state.answers = []

    if "page" not in st.session_state:
        st.session_state.page = "home"

    # 홈 화면
    if st.session_state.page == "home":
        st.markdown("### 🌍 어서오세요! ✨ MBTI 진로 탐험의 세계로 🧭")
        st.write("👉 버튼을 눌러서 검사를 시작하세요 🎉")
        if st.button("🔥 MBTI 검사 시작하기 🔥"):
            st.session_state.page = "test"
            st.session_state.answers = []

    # 검사 화면
    elif st.session_state.page == "test":
        st.markdown("## 📝 MBTI 검사 진행 중... 💡")
        for idx, (q, opt1, opt2) in enumerate(questions):
            st.session_state.answers.append(
                st.radio(q, [opt1, opt2], key=f"q{idx}")
            )

        if st.button("🌈 결과 확인하기 🚀"):
            st.session_state.page = "result"

    # 결과 화면
    elif st.session_state.page == "result":
        result = "".join(st.session_state.answers)
        st.markdown(
            f"<h2 style='text-align: center;'>🎉 당신의 MBTI 결과는: <span style='color: #FF5733'>{result}</span> 🎉</h2>",
            unsafe_allow_html=True,
        )

        st.markdown("## 🌟 추천 진로 ✨")
        st.success("💡 당신에게 어울리는 진로를 추천합니다!")

        rec = careers.get(result, ["🌈 다양한 분야에 도전해보세요!"])
        for r in rec:
            st.markdown(f"- {r}")

        # 🎨 화려한 풍선 애니메이션
        st.balloons()
        st.snow()


if __name__ == "__main__":
    main()
