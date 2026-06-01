import base64
import os

# ============================================================
# COLOR PALETTE
# ============================================================
TEAL_DARK   = "#007979"
NAVY_DARK   = "#093C5D"
TEAL_MED    = "#24B1B1"
BLUE_MED    = "#3B7597"
TEAL_LIGHT  = "#6FD1D7"
CYAN_ACCENT = "#5DF8D8"
WHITE       = "#FFFFFF"
GRAY_LIGHT  = "#F5F7FA"
GRAY_BORDER = "#E8ECF0"
GRAY_TEXT   = "#6B7280"
CREAM_LIGHT = "#FFF0E4"
CREAM_WARM  = "#FFE0C5"
SUCCESS     = "#10B981"
WARNING     = "#F59E0B"
DANGER      = "#EF4444"
INFO        = "#3B82F6"

GRAD_SIDEBAR  = f"linear-gradient(180deg, {TEAL_DARK}, {NAVY_DARK})"
GRAD_HEADER   = f"linear-gradient(135deg, {NAVY_DARK}, {BLUE_MED})"
GRAD_CARD     = f"linear-gradient(135deg, {TEAL_MED}, {TEAL_LIGHT})"
GRAD_POSITIVE = f"linear-gradient(135deg, {TEAL_MED}, {CYAN_ACCENT})"

CHART_COLORS = [TEAL_MED, BLUE_MED, TEAL_LIGHT, NAVY_DARK, CYAN_ACCENT, TEAL_DARK]

KUADRAN_COLORS = {
    "Prioritas Utama":  DANGER,
    "Pertahankan":      SUCCESS,
    "Prioritas Rendah": BLUE_MED,
    "Berlebihan":       WARNING,
}
SEGMENT_COLORS = {
    "Loyal Aman":  SUCCESS,
    "Latent Risk": WARNING,
    "At Risk":     DANGER,
}
NPS_COLORS = {
    "Promoter":  SUCCESS,
    "Passive":   WARNING,
    "Detractor": DANGER,
}

# ============================================================
# FONT
# ============================================================
def load_font_base64(font_path):
    with open(font_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def get_font_css():
    static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'fonts')
    fonts_needed = {
        'Poppins-Regular':  ('Poppins', '400'),
        'Poppins-Medium':   ('Poppins', '500'),
        'Poppins-SemiBold': ('Poppins', '600'),
        'Poppins-Bold':     ('Poppins', '700'),
        'CalSans-SemiBold': ('CalSans', '600'),
    }
    font_faces = ""
    for filename, (family, weight) in fonts_needed.items():
        for ext in ['ttf', 'otf']:
            path = os.path.join(static_dir, f'{filename}.{ext}')
            if os.path.exists(path):
                b64 = load_font_base64(path)
                fmt = 'truetype' if ext == 'ttf' else 'opentype'
                font_faces += f"""
                @font-face {{
                    font-family: '{family}';
                    font-weight: {weight};
                    src: url('data:font/{fmt};base64,{b64}') format('{fmt}');
                }}"""
                break
    return f"<style>{font_faces}\n* {{ font-family: 'Poppins', sans-serif !important; }}\nh1 {{ font-family: 'CalSans', 'Poppins', sans-serif !important; }}</style>"

# ============================================================
# GLOBAL CSS
# ============================================================
def get_global_css():
    return f"""<style>
    .stApp {{ background-color: {GRAY_LIGHT}; }}
    [data-testid="stSidebar"] {{ background: {GRAD_SIDEBAR}; }}
    [data-testid="stSidebar"] * {{ color: {WHITE} !important; }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    [data-testid="stSidebarContent"] {{ padding-top: 1rem; }}
    [data-testid="stMetric"] {{
        background: {GRAY_LIGHT};
        border-radius: 12px;
        padding: 16px;
        border-left: 4px solid {TEAL_MED};
    }}
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {TEAL_DARK}, {NAVY_DARK}) !important;
    }}
    [data-testid="stMetricValue"] {{ font-weight: 600 !important; }}
    [data-testid="stSidebar"] [data-testid="stMetric"] {{
        background: linear-gradient(135deg, #002765, #2CB5D4);
        border-radius: 12px;
        padding: 16px;
        border: none;
    }}
    [data-testid="stSidebar"] [data-testid="stMetricValue"] {{
        color: {WHITE} !important;
        font-weight: 700 !important;
        font-size: 2rem !important;
    }}
    [data-testid="stSidebar"] [data-testid="stMetricLabel"] {{
        color: {WHITE} !important;
        font-weight: 600 !important;
    }}
    [data-testid="stSidebar"] [data-testid="stSelectbox"] span,
    [data-testid="stSidebar"] .stSelectbox div {{
        color: {NAVY_DARK} !important;
    }}
    h1 {{
        background: linear-gradient(135deg, #002765, #2CB5D4) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 600 !important;
    }}
    h2, h3 {{ color: {NAVY_DARK}; font-weight: 600; }}
    hr {{ border-color: {GRAY_BORDER}; }}
    .dashboard-card {{
        background: {WHITE};
        border-radius: 16px;
        padding: 20px;
        border: 1px solid {GRAY_BORDER};
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    </style>"""

# ============================================================
# GABUNGAN — panggil ini di setiap halaman
# ============================================================
def get_full_css():
    return get_font_css() + get_global_css()