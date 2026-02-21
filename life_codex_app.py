import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Life Architecture Codex",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom Styling (Parchment & Ink Aesthetic)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&display=swap');
    
    .main {
        background-color: #f4ecd8;
        color: #3e2723;
        font-family: 'Noto Serif KR', serif;
    }
    
    .stApp {
        background-image: radial-gradient(#d4c4a8 0.5px, transparent 0.5px);
        background-size: 20px 20px;
    }

    .codex-card {
        background: rgba(255, 255, 255, 0.4);
        border: 2px solid #3e2723;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        transition: transform 0.3s ease;
    }

    .codex-card:hover {
        transform: scale(1.02);
        background: rgba(255, 255, 255, 0.6);
    }

    h1, h2, h3 {
        color: #3e2723 !important;
        font-family: 'Noto Serif KR', serif;
    }

    .stButton>button {
        background-color: transparent;
        color: #3e2723;
        border: 1px solid #3e2723;
        font-family: 'Noto Serif KR', serif;
        width: 100%;
        text-align: left;
    }

    .stButton>button:hover {
        background-color: #3e2723;
        color: #f4ecd8;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Structure
steps = [
    {"id": "01", "name": "환경 입력 (Input)", "icon": "⚙️", "detail": "외부 환경 변수 수집 및 필터링 없는 데이터 진입."},
    {"id": "02", "name": "직관 기반 가설 설정", "icon": "⚡", "detail": "경험적 데이터베이스를 활용한 즉각적인 모델링."},
    {"id": "03", "name": "1차 확률 부여", "icon": "🎲", "detail": "실행 가용성을 판단하기 위한 Prior Probability 할당."},
    {"id": "04", "name": "행동 실행", "icon": "🚀", "detail": "물리적 환경에 대한 시스템 투사 (Action)."},
    {"id": "05", "name": "결과 관측", "icon": "👁️", "detail": "Telemetry 데이터 수집 및 기대값과의 오차 측정."},
    {"id": "06", "name": "충돌 여부 체크", "icon": "⚠️", "detail": "외부 구조와의 마찰 감지 - 분기점(Branching)."},
    {"id": "07", "name": "데이터 검색 / 재계산", "icon": "🔍", "detail": "충돌 시에만 발동하는 지연 로딩(Lazy Loading) 학습."},
    {"id": "08", "name": "구조 업데이트", "icon": "🛠️", "detail": "시스템 하드와이어링 및 Armory 스크립트 갱신."},
    {"id": "09", "name": "APM 감소 / 자원 확보", "icon": "💎", "detail": "인지 비용 최적화 및 유휴 자원 생성."}
]

# 4. App Layout
st.title("📜 Codex: Life Architecture")
st.markdown("*\"Cognitio, Actio, et Optimizatio\" — 최적화를 위한 자아 설계 지침서*")
st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔄 Algorithm Loop")
    # Interactive Buttons for each step
    for step in steps:
        if st.button(f"{step['id']}. {step['icon']} {step['name']}"):
            st.session_state.active_step = step

with col2:
    st.subheader("📋 Engineering Specification")
    if 'active_step' in st.session_state:
        step = st.session_state.active_step
        st.markdown(f"""
        <div style="border: 4px double #3e2723; padding: 30px; background-color: #fdfaf1; border-radius: 15px;">
            <h1 style="font-size: 50px; opacity: 0.2; margin-bottom: -10px;">{step['id']}</h1>
            <h2>{step['icon']} {step['name']}</h2>
            <hr style="border-top: 2px solid #3e2723;">
            <p style="font-size: 18px; line-height: 1.6; font-style: italic;">"{step['detail']}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        # Functional Element: Notes
        st.text_area(f"[{step['name']}] 관련 현재 상태 기록", placeholder="여기에 현재 충돌 내역이나 업데이트할 로직을 적으세요...")
        if st.button("Save to Codex"):
            st.success("데이터가 시스템 구조에 동기화되었습니다.")
    else:
        st.info("알고리즘 단계를 선택하여 상세 설계도를 확인하십시오.")

# 5. Engineering Sketch (SVG Visual)
st.markdown("---")
st.markdown("### 🖋️ Structural Visualization")
svg_code = """
<svg width="100%" height="150" viewBox="0 0 800 150" xmlns="http://www.w3.org/2000/svg">
  <path d="M50 75 Q 200 10, 400 75 T 750 75" fill="none" stroke="#3e2723" stroke-width="2" stroke-dasharray="5,5" />
  <circle cx="50" cy="75" r="10" fill="#3e2723" />
  <circle cx="400" cy="75" r="30" fill="none" stroke="#3e2723" stroke-width="1" />
  <circle cx="750" cy="75" r="10" fill="#3e2723" />
  <text x="45" y="105" font-family="serif" font-size="12" fill="#3e2723">INPUT</text>
  <text x="375" y="125" font-family="serif" font-size="12" fill="#3e2723">PROCESSING</text>
  <text x="730" y="105" font-family="serif" font-size="12" fill="#3e2723">OUTPUT</text>
</svg>
"""
st.markdown(svg_code, unsafe_allow_html=True)

st.caption("© 2026 LIFE ARCHITECTURE PROJECT | Python Backend Framework")