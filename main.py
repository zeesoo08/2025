import streamlit as st

# MBTI 질문 예시
questions = [
    ("나는 사람들과 어울릴 때 에너지를 얻는다.", "E", "I"),
    ("계획을 세우는 것을 좋아한다.", "J", "P"),
    ("현실적인 것보다 상상하는 게 더 좋다.", "N", "S"),
    ("논리보다 감정을 더 중시한다.", "F", "T"),
]

def main():
    st.title("🌱 MBTI 기반 진로교육 웹앱")
    st.write("당신의 성격을 기반으로 진로를 탐색해보세요!")

    if "answers" not in st.session_state:
        st.session_state.answers = []

    # 검사 시작 버튼
    if st.button("MBTI 검사 시작하기"):
        st.session_state.answers = []
        st.session_state.page = "test"

    # 질문지 페이지
    if st.session_state.get("page") == "test":
        st.subheader("📝 MBTI 검사")
        for idx, (q, opt1, opt2) in enumerate(questions):
            answer = st.radio(q, [opt1, opt2], key=f"q{idx}")
            st.session_state.answers.append(answer)

        if st.button("결과 보기"):
            st.session_state.page = "result"

    # 결과 페이지
    if st.session_state.get("page") == "result":
        st.subheader("📊 결과")
        result = "".join(st.session_state.answers)
        st.write(f"당신의 MBTI는 **{result}** 입니다!")

        # 간단한 진로 추천 예시
        careers = {
            "ENTJ": ["리더십이 필요한 직업", "경영자", "정치가"],
            "INFJ": ["상담가", "작가", "교사"],
            "ISTP": ["엔지니어", "파일럿", "연구원"]
        }
        st.write("추천 진로: ", careers.get(result, ["다양한 분야에 도전해보세요!"]))

if __name__ == "__main__":
    main()
