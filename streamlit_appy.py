import streamlit as st

st.set_page_config(
    page_title="자기소개 페이지",
    page_icon="👋",
    layout="wide",
)

st.title("👋 자기소개 페이지")

st.markdown(
    "안녕하세요! 여기에 간단한 자기소개와 연락처, 관심사를 정리해보세요."
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://via.placeholder.com/250x250.png?text=Profile+Image",
        caption="프로필 이미지",
        width=250,
    )
    st.markdown("---")
    st.subheader("연락처")
    st.write("- 이메일: your.email@example.com")
    st.write("- 깃허브: [github.com/yourname](https://github.com/yourname)")
    st.write("- LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)")

with col2:
    st.subheader("소개")
    st.write(
        "여기에 간단한 자기소개를 작성하세요. 예: 이름, 현재 하는 일, 관심 분야, 목표 등을 소개할 수 있습니다."
    )

    st.subheader("기술 스택")
    st.write(
        "- Python\n- Streamlit\n- 데이터 분석\n- 웹 개발\n- 기타 관심 기술"
    )

    st.subheader("프로젝트/경험")
    st.write(
        "- 프로젝트 1: 간단한 설명\n- 프로젝트 2: 간단한 설명\n- 프로젝트 3: 간단한 설명"
    )

st.markdown("---")

st.subheader("추가 소개")
st.write(
    "여기에는 좀 더 자세한 자기소개, 취미, 학습 중인 분야, 앞으로 하고 싶은 일 등을 자유롭게 작성할 수 있습니다."
)
