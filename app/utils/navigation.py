import streamlit as st
from utils.theme import NAVY_DARK, GRAY_BORDER

def render_navigation(current_page=""):
    
    pages = [
        ("Scorecard",            "pages/1_Scorecard.py"),
        ("Prioritas Layanan",    "pages/2_Prioritas_Layanan.py"),
        ("Profil Cabang",        "pages/3_Profil_Cabang.py"),
        ("Peta Emosi",           "pages/4_Peta_Emosi.py"),
        ("Segmentasi Loyalitas", "pages/5_Segmentasi_Loyalitas.py"),
        ("Intelijen Kompetitor", "pages/6_Kompetitor.py"),
    ]

    # CSS untuk styling page_link
    st.markdown("""
    <style>
    [data-testid="stPageLink"] {
        background: white;
        border-radius: 8px;
        border: 1px solid #E8ECF0;
        padding: 4px 8px;
        font-size: 0.85rem;
        font-weight: 500;
        color: #093C5D !important;
        text-decoration: none;
    }
    [data-testid="stPageLink"]:hover {
        background: #F5F7FA;
    }
    [data-testid="stPageLink"] p {
        color: #093C5D !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Container navigasi
    st.markdown("""
    <div style="background:#F5F7FA;padding:6px;border-radius:12px;
        margin-bottom:16px;border:1px solid #E8ECF0;">
    """, unsafe_allow_html=True)

    cols = st.columns(len(pages))
    for i, (label, path) in enumerate(pages):
        with cols[i]:
            st.page_link(path, label=label)

    st.markdown("</div>", unsafe_allow_html=True)