import streamlit as st
import pandas as pd
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except Exception:
    HAS_MATPLOTLIB = False

st.set_page_config(
    page_title="등차수열 함수 해석",
    page_icon="🔢",
    layout="wide",
)

st.title("등차수열 함수 해석 수업")
st.write("이 페이지는 등차수열의 일반항과 합을 함수적으로 이해하기 위한 학습용 스트림릿 페이지입니다.")

st.markdown("---")

st.markdown("---")
st.markdown("### 함수 형태 시각화")

# 입력값 설정 (시각화에 사용되는 값)
st.subheader("입력값 설정")
a1 = st.number_input("첫째항 a₁", value=3, step=1)
d = st.number_input("공차 d", value=2, step=1)
n = st.number_input("개수 n", min_value=1, value=10, step=1)
show_graph = st.checkbox("그래프 표시", value=True)

col_a, col_s = st.columns(2)

with col_a:
    st.subheader("a_n = 3n - 1 (점)")
    st.write("정의역: 자연수 n = 1,2,3,...")
    ns = list(range(1, n + 1))
    an3 = [3 * i - 1 for i in ns]
    df_an3 = pd.DataFrame({"n": ns, "a_n = 3n - 1": an3})
    st.dataframe(df_an3)
    if HAS_MATPLOTLIB:
        fig, ax = plt.subplots()
        ax.scatter(ns, an3, color="tab:blue")
        ax.set_xlabel("n")
        ax.set_ylabel("a_n")
        ax.set_title("a_n = 3n - 1 (점 그래프)")
        # show only integer ticks for natural numbers
        if len(ns) <= 30:
            ax.set_xticks(ns)
        else:
            ax.set_xticks(ns[:: max(1, len(ns)//30)])
        ax.set_xlim(min(ns) - 0.5, max(ns) + 0.5)
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)
    else:
        st.warning("`matplotlib`이 설치되어 있지 않아 점 그래프를 선 그래프로 대체합니다.")
        st.line_chart(pd.DataFrame({"a_n": an3}, index=ns))

with col_s:
    st.subheader("S(n) = p·n·(n-20) (포물선)")
    st.write("원점과 n=20에서 0이 되는 포물선을 그립니다. p는 음수(p < 0)로 설정하세요 — 아래로 볼록입니다.")
    p = st.number_input("스케일 p (음수)", min_value=-100.0, max_value=-0.01, value=-1.0, step=0.1)
    n_intercept = 20
    max_n = max(n, n_intercept)
    ns0 = list(range(0, max_n * 2 + 1))
    Sn = [p * i * (i - n_intercept) for i in ns0]
    st.markdown(f"$S(n) = {p} \cdot n (n - {n_intercept})$")
    df_sn = pd.DataFrame({"n": ns0, "S(n)": Sn})
    st.dataframe(df_sn)
    if HAS_MATPLOTLIB:
        fig2, ax2 = plt.subplots()
        # discrete points only for natural n
        ax2.scatter(ns0, Sn, color='tab:red')
        ax2.scatter([0, n_intercept], [0, 0], color='black', s=50, zorder=5)
        # annotate positions
        ymax = max(Sn) if len(Sn) > 0 else 1
        ax2.annotate('origin', xy=(0, 0), xytext=(0, ymax * 0.05 if ymax != 0 else 0.1))
        ax2.annotate('n=20', xy=(n_intercept, 0), xytext=(n_intercept, ymax * 0.05 if ymax != 0 else 0.1))
        ax2.set_xlabel('n')
        ax2.set_ylabel('S(n)')
        ax2.set_title('S(n) = p n (n-20) — discrete n')
        if len(ns0) <= 30:
            ax2.set_xticks(ns0)
        else:
            ax2.set_xticks(ns0[:: max(1, len(ns0)//30)])
        ax2.set_xlim(min(ns0) - 0.5, max(ns0) + 0.5)
        ax2.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig2)
    else:
        st.warning("`matplotlib`이 설치되어 있지 않아 포물선을 선 그래프로 대체합니다.")
        st.line_chart(pd.DataFrame({"S(n)": Sn}, index=ns0))

st.markdown("---")
st.subheader("S(n) 시각화 — 원점과 지정된 n-절편 통과")
st.write("원점(0,0)과 사용자가 지정한 n-절편을 지나는 이차함수 형태로 S(n)을 그립니다.")

# 사용자 입력: n-절편과 스케일 계수 p
n_intercept = st.number_input("n-절편 (n-intercept)", min_value=1, value=20, step=1)
p_scale = st.number_input("스케일 계수 p (양수 — 위로 볼록)", min_value=0.01, value=1.0, step=0.1)

# 시각화 범위 설정
max_n = max(n, int(n_intercept))
ns0 = list(range(0, max_n * 2 + 1))

# S(n) = p * n * (n - n_intercept)  -> 원점과 n_intercept에서 0
Sn = [p_scale * i * (i - int(n_intercept)) for i in ns0]

st.markdown(f"$S(n) = {p_scale} \cdot n (n - {int(n_intercept)})$")
df_sn = pd.DataFrame({"n": ns0, "S(n)": Sn})
st.dataframe(df_sn)

if HAS_MATPLOTLIB:
    fig2, ax2 = plt.subplots()
    # discrete points only
    ax2.scatter(ns0, Sn, color='tab:red')
    ax2.scatter([0, int(n_intercept)], [0, 0], color='black', s=50, zorder=5)
    ax2.set_xlabel('n')
    ax2.set_ylabel('S(n)')
    ax2.set_title('S(n) — origin and n-intercept')
    if len(ns0) <= 30:
        ax2.set_xticks(ns0)
    else:
        ax2.set_xticks(ns0[:: max(1, len(ns0)//30)])
    ax2.set_xlim(min(ns0) - 0.5, max(ns0) + 0.5)
    ax2.grid(True, linestyle='--', alpha=0.5)
    st.pyplot(fig2)
else:
    st.warning("`matplotlib`이 설치되어 있지 않아 포물선 세부 표시는 제한됩니다. 선 그래프로 대체합니다.")
    st.line_chart(pd.DataFrame({"S(n)": Sn}, index=ns0))
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