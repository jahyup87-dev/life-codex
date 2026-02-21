import streamlit as st
import json
import os
from datetime import datetime

# 1. Page Configuration & Theme
st.set_page_config(
    page_title="Life Architecture Codex",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Strong Custom Styling (Codex Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;700&display=swap');
    
    .stApp {
        background-color: #f4ecd8 !important;
        background-image: radial-gradient(#d4c4a8 0.5px, transparent 0.5px) !important;
        background-size: 20px 20px !important;
    }
    
    h1, h2, h3, p, span, div, label, .stMarkdown {
        color: #3e2723 !important;
        font-family: 'Noto Serif KR', serif !important;
    }

    .stButton>button {
        background-color: rgba(255, 255, 255, 0.5) !important;
        color: #3e2723 !important;
        border: 1px solid #3e2723 !important;
        border-radius: 5px !important;
    }

    .stButton>button:hover {
        background-color: #3e2723 !important;
        color: #f4ecd8 !important;
    }

    .detail-card {
        border: 4px double #3e2723;
        padding: 25px;
        background-color: #fdfaf1;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    .log-entry {
        border-left: 3px solid #3e2723;
        padding-left: 15px;
        margin-bottom: 15px;
        background-color: rgba(62, 39, 35, 0.03);
        padding-top: 5px;
        padding-bottom: 5px;
    }

    .log-timestamp {
        font-size: 0.8rem;
        font-weight: bold;
        color: #795548 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Archiving Logic (Folder-like Structure in JSON)
DATA_FILE = "codex_archive.json"

def load_archive():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_to_archive(step_id, content):
    archive = load_archive()
    if step_id not in archive:
        archive[step_id] = []
    
    # 신규 로그 생성 (타임스탬프 포함)
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "content": content
    }
    # 최신 기록이 위로 오도록 삽입
    archive[step_id].insert(0, new_entry)
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(archive, f, ensure_ascii=False, indent=4)

# 4. Algorithm Structure
steps = [
    {"id": "01", "name": "환경 입력 (Input)", "icon": "⚙️", "detail": "외부 환경 변수 수집 및 데이터 진입."},
    {"id": "02", "name": "직관 기반 가설 설정", "icon": "⚡", "detail": "내재된 DB를 활용한 즉각적인 모델링."},
    {"id": "03", "name": "1차 확률 부여", "icon": "🎲", "detail": "실행 가용성 판단을 위한 사전 확률 할당."},
    {"id": "04", "name": "행동 실행", "icon": "🚀", "detail": "물리적 환경에 대한 시스템 투사."},
    {"id": "05", "name": "결과 관측", "icon": "👁️", "detail": "실측 데이터 수집 및 오차 측정."},
    {"id": "06", "name": "충돌 여부 체크", "icon": "⚠️", "detail": "구조적 마찰 감지 및 분기점 판별."},
    {"id": "07", "name": "데이터 검색 / 재계산", "icon": "🔍", "detail": "충돌 시 발동하는 집중 학습."},
    {"id": "08", "name": "구조 업데이트", "icon": "🛠️", "detail": "시스템 하드와이어링 및 개선."},
    {"id": "09", "name": "APM 감소 / 자원 확보", "icon": "💎", "detail": "인지 비용 최적화 및 유휴 자원 생성."}
]

# 5. App Layout
st.title("📜 Codex: Temporal Archive")
st.markdown("*\"Historia est Magistra Vitae\" — 기록은 최적화의 스승이다*")
st.divider()

col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("🔄 Optimization Loop")
    for step in steps:
        if st.button(f"{step['id']}. {step['icon']} {step['name']}", key=step['id'], use_container_width=True):
            st.session_state.active_step = step

with col2:
    if 'active_step' in st.session_state:
        step = st.session_state.active_step
        st.markdown(f"""
        <div class="detail-card">
            <h1 style="font-size: 40px; opacity: 0.1; margin-bottom: -15px;">{step['id']}</h1>
            <h2>{step['icon']} {step['name']}</h2>
            <p style="font-style: italic; opacity: 0.8;">"{step['detail']}"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # New Entry Section
        st.subheader("🖋️ New Record")
        new_content = st.text_area("발생한 충돌이나 업데이트할 로직을 기록하세요", height=100, key=f"input_{step['id']}")
        if st.button("Archive to Codex (기록 저장)"):
            if new_content.strip():
                save_to_archive(step['id'], new_content)
                st.success(f"{datetime.now().strftime('%H:%M:%S')} 기록이 아카이브에 영구 저장되었습니다.")
                st.rerun()
            else:
                st.warning("내용을 입력해주세요.")

        # History Section (The Archive)
        st.write("---")
        st.subheader("📚 Evolution History")
        archive = load_archive()
        history = archive.get(step['id'], [])
        
        if not history:
            st.info("아직 저장된 기록이 없습니다. 첫 번째 발자취를 남겨보세요.")
        else:
            for entry in history:
                st.markdown(f"""
                <div class="log-entry">
                    <div class="log-timestamp">{entry['timestamp']}</div>
                    <div style="white-space: pre-wrap;">{entry['content']}</div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("좌측 알고리즘 루프에서 단계를 선택하여 아카이브를 탐색하십시오.")

st.markdown("---")
st.caption(f"SYSTEM ARCHIVE ACTIVE | {datetime.now().year} LIFE ARCHITECTURE PROJECT")
