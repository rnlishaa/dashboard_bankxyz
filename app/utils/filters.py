import streamlit as st

def render_filters(df):
    # ── BRANDING ──────────────────────────────────────────
    st.sidebar.markdown("""
        <div style="
            text-align: center;
            padding: 1rem 0 1.5rem 0;
            border-bottom: 1px solid rgba(255,255,255,0.2);
            margin-bottom: 1.5rem;
        ">
            <div style="
                font-size: 1.4rem;
                font-weight: 700;
                color: white;
                letter-spacing: 1px;
            ">BANK XYZ</div>
            <div style="
                font-size: 0.75rem;
                color: rgba(255,255,255,0.7);
                margin-top: 4px;
            ">Customer Experience Intelligence</div>
        </div>
    """, unsafe_allow_html=True)

    # ── FILTER DATA ───────────────────────────────────────
    st.sidebar.markdown(
        '<p style="color:white;font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Filter Data</p>',
        unsafe_allow_html=True
    )

    prov_list = ['Semua'] + sorted(df['PROV'].dropna().unique().tolist())
    prov = st.sidebar.selectbox("Provinsi", prov_list)

    if prov != 'Semua':
        df_prov = df[df['PROV'] == prov]
    else:
        df_prov = df

    cabang_list = ['Semua'] + sorted(df_prov['CABANG'].dropna().unique().tolist())
    cabang = st.sidebar.selectbox("Cabang", cabang_list)

    panel_list = ['Semua', 'Teller (KUOTA 50%)', 'CS (KUOTA 50%)']
    panel = st.sidebar.selectbox("Panel Layanan", panel_list)

    gender_list = ['Semua'] + sorted(df['S1'].dropna().unique().tolist())
    gender = st.sidebar.selectbox("Jenis Kelamin", gender_list)

    usia_order = [
        'Semua', '17 -19 tahun', '20 - 25 tahun',
        '26 - 30 tahun', '31 - 35 tahun', '36 - 40 tahun',
        '41 - 45 tahun', '46 - 50 tahun', '50 tahun dan ke atas'
    ]
    usia = st.sidebar.selectbox("Range Usia", usia_order)

    lama_order = [
        'Semua',
        '1 bulan s/d 3 bulan',
        '3 bulan s/d 11 bulan',
        '1 tahun s/d 2 tahun 11 bulan',
        '3 tahun s/d 4 tahun 11 bulan',
        '5 tahun atau lebih'
    ]
    lama = st.sidebar.selectbox("Lama Menjadi Nasabah", lama_order)

    df_filtered = df.copy()
    if prov   != 'Semua': df_filtered = df_filtered[df_filtered['PROV']   == prov]
    if cabang != 'Semua': df_filtered = df_filtered[df_filtered['CABANG'] == cabang]
    if panel  != 'Semua': df_filtered = df_filtered[df_filtered['PANEL']  == panel]
    if gender != 'Semua': df_filtered = df_filtered[df_filtered['S1']     == gender]
    if usia   != 'Semua': df_filtered = df_filtered[df_filtered['S2_2']   == usia]
    if lama   != 'Semua': df_filtered = df_filtered[df_filtered['S4']     == lama]

    st.sidebar.markdown("---")
    st.sidebar.metric("Total Responden", f"{len(df_filtered):,}")
    st.sidebar.caption(f"dari {len(df):,} total responden")

    return df_filtered