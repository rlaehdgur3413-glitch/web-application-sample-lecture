import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="등차수열 함수 해석",
    page_icon="🔢",
    layout="wide",
)

st.title("등차수열 함수 해석 수업")
st.write("이 페이지는 등차수열의 일반항과 합을 함수적으로 이해하기 위한 학습용 스트림릿 페이지입니다.")

st.markdown("---")

with st.expander("수업 목표"):
    st.write(
        "- 등차수열의 정의를 이해합니다.\n"
        "- 일반항 a(n)을 함수처럼 해석합니다.\n"
        "- 합 S(n)의 의미를 이해하고 계산합니다.\n"
        "- n에 따라 항과 누적 합이 어떻게 변하는지 확인합니다."
    )

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("등차수열 개념 정리")
    st.markdown(
        "등차수열은 인접한 두 항의 차이가 항상 일정한 수열입니다. "
        "첫째항을 $a_1$, 공차를 $d$라고 하면 일반항은 다음과 같습니다."
    )
    st.latex(r"a(n) = a_1 + (n-1)d")
    st.markdown(
        "합 함수 $S(n)$은 처음 $n$개 항의 합을 의미합니다. "
        "등차수열의 합 공식은 다음과 같습니다."
    )
    st.latex(r"S(n) = \frac{n}{2} \left( 2a_1 + (n-1)d \right)")
    st.markdown(
        "이 두 식을 통해 $n$을 입력하면 해당 항과 누적 합을 모두 계산할 수 있습니다. "
        "따라서 $a(n)$과 $S(n)$은 함수로 볼 수 있습니다."
    )
    st.markdown("### 예시 수열")
    st.write("예: $a_1 = 3$, $d = 2$ 이면 수열은 3, 5, 7, 9, ... 입니다.")

with col2:
    st.subheader("입력값 설정")
    a1 = st.number_input("첫째항 a₁", value=3, step=1)
    d = st.number_input("공차 d", value=2, step=1)
    n = st.number_input("개수 n", min_value=1, value=10, step=1)
    show_graph = st.checkbox("그래프 표시", value=True)

st.markdown("---")

st.subheader("계산 결과")

@st.cache_data
def arithmetic_terms(a1: int, d: int, n: int):
    terms = [a1 + (i - 1) * d for i in range(1, n + 1)]
    sums = [sum(terms[:i]) for i in range(1, n + 1)]
    return terms, sums

terms, sums = arithmetic_terms(a1, d, n)
last_term = terms[-1]
last_sum = sums[-1]

st.markdown(f"- 일반항 a(n): **{a1} + (n-1) × {d}**")
st.markdown(f"- 입력한 n = {n}일 때 a(n) = **{last_term}**")
st.markdown(f"- S(n) = **{last_sum}**")

st.markdown("### 첫 n개 항과 누적 합")
term_table = pd.DataFrame(
    {
        "n": list(range(1, n + 1)),
        "a(n)": terms,
        "S(n)": sums,
    }
)
st.dataframe(term_table)

if show_graph:
    st.markdown("### 함수 형태 시각화")
    st.line_chart(
        pd.DataFrame(
            {
                "a(n)": terms,
                "S(n)": sums,
            },
            index=list(range(1, n + 1)),
        )
    )

st.markdown("---")
st.subheader("학습 활동 아이디어")
st.write(
    "1. a₁과 d를 바꿔가며 a(n)과 S(n)의 변화 양상을 관찰합니다.\n"
    "2. 항의 개수를 늘릴 때 a(n)과 S(n)의 증가 속도를 비교합니다.\n"
)
st.write(
    "3. 문제 예시: 1) a₁=5, d=3 일 때 10번째 항을 구하시오. "
    "2) a₁=2, d=-1 일 때 처음 8개 합을 구하시오."
)

st.info(
    "이 페이지를 사용해 수업을 구성하면, 등차수열의 일반항과 합을 함수 개념으로 자연스럽게 연결할 수 있습니다."
)