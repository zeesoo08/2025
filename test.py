if st.button("결과 확인"):
    if count == 3:
        st.balloons()
        st.success("🎉 완벽해요! 정확히 하루 3번 양치했어요!")
        st.markdown("✨ 이런 꾸준함이 치아 건강을 지켜줄 거예요!")
    elif count > 3:
        st.balloons()
        st.success("🎉 아주 잘했어요! 3회 이상 양치하는 습관 최고에요!")
        st.markdown("✨ 계속 이렇게만 해 주세요! 치아 건강 만점입니다!")
    else:
        st.warning("🪥 하루 3번 양치하는 것을 목표로 해보세요!")
        st.info("💡 아침, 점심, 저녁 식사 후 양치를 권장해요.")
