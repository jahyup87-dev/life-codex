import streamlit as st
import pandas as pd
import json
import os

# 1. Page Configuration & Theme Hardwiring
# 어떤 기기에서도 동일한 느낌을 주기 위해 레이아웃과 초기 설정을 고정합니다.
st.set_page_config(
    page_title="Life Architecture Codex",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Strong Custom Styling (System Theme Override)
# 시스템 설정에 관계없이 항상 '코덱스' 감성을 유지하도록 배경색과 글자색을 강제로 지정합니다.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&display=swap');
    
    /* 전체 배경 강제 지정 */
    .stApp {
        background-color: #f4ecd8 !important;
        background-image: radial-gradient(#d4c4a8 0.5px, transparent 0.5px) !important;
        background-size: 20px 20px !important;
    }
    
    /* 텍스트 색상 강제 지정 */
    h1, h2, h3, p, span, div, label {
        color: #3e2723 !important;
        font-family: 'Noto Serif KR', serif !important;
    }

    /* 버튼 스타일 (다크모드에서도 배경 유지) */
    .stButton>button {
        background-color: rgba(255, 255, 255, 0.5) !important;
        color: #3e2723 !important;
        border: 1px solid #3e2723 !important;
        border-radius: 5px !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        background-color: #3e2723 !important;
        color: #f4ecd8 !important;
        border: 1px solid #3e2723 !important;
    }

    /* 입력창 스타일 보강 */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.7) !important;
        color: #3e2723 !important;
        border: 1px solid #3e2723 !important;
    }

    /* 상세 정보 카드 내부 스타일 */
    .detail-card {
        border: 4px double #3e2723;
        padding: 30px;
        background-color: #fdfaf1;
        border-radius: 15px;
        box-shadow: inset 0 0 50px rgba(62, 39, 35, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Structure & Persistence Logic
DATA_FILE = "codex_data.json"

def load_codex_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_codex_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("🔄 Algorithm Loop")
    for step in steps:
        if st.button(f"{step['id']}. {step['icon']} {step['name']}", key=step['id']):
            st.session_state.active_step = step

with col2:
    st.subheader("📋 Engineering Specification")
    if 'active_step' in st.session_state:
        step = st.session_state.active_step
        st.markdown(f"""
        <div class="detail-card">
            <h1 style="font-size: 50px; opacity: 0.1; margin-bottom: -20px; color: #3e2723;">{step['id']}</h1>
            <h2 style="color: #3e2723;">{step['icon']} {step['name']}</h2>
            <hr style="border-top: 2px solid #3e2723; opacity: 0.3;">
            <p style="font-size: 18px; line-height: 1.6; font-style: italic; color: #3e2723;">"{step['detail']}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        codex_data = load_codex_data()
        step_id = step['id']
        current_note = codex_data.get(step_id, "")

        new_note = st.text_area(f"[{step['name']}] 관련 현재 상태 기록", value=current_note, height=200, placeholder="여기에 현재 충돌 내역이나 업데이트할 로직을 적으세요...")
        
        if st.button("Save to Codex (동기화)"):
            codex_data[step_id] = new_note
            save_codex_data(codex_data)
            st.success("데이터가 시스템 구조에 동기화되었습니다! 💾")
    else:
        st.info("알고리즘 단계를 선택하여 상세 설계도를 확인하십시오.")

st.markdown("---")
st.caption("© 2026 LIFE ARCHITECTURE PROJECT | v1.1.0 - Multi-device Consistency Update")
