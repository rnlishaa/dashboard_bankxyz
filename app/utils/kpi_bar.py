import streamlit as st
import pandas as pd
from utils.theme import (WHITE, GRAY_BORDER, GRAY_LIGHT, NAVY_DARK,
                          TEAL_MED, SUCCESS, WARNING, DANGER)

def render_kpi(label, value, sub=None, color=TEAL_MED, icon=""):
    """Render satu kartu KPI"""
    sub_html = f'<div style="font-size:0.75rem; color:{color}; margin-top:2px;">{sub}</div>' if sub else ""
    st.markdown(f"""
    <div style="
        background: {WHITE};
        border-radius: 12px;
        padding: 16px 20px;
        border: 1px solid {GRAY_BORDER};
        border-top: 4px solid {color};
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 100%;
    ">
        <div style="font-size:0.8rem; color:#6B7280; font-weight:500; margin-bottom:6px;">{icon} {label}</div>
        <div style="font-size:1.5rem; font-weight:600; color:{NAVY_DARK};">{value}</div>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)

def render_kpi_scorecard(df):
    """KPI bar untuk halaman Scorecard"""
    n = len(df)
    nps = df['G1A'].notna().sum()
    pct_promoter = (df['G1A'] >= 9).sum() / nps * 100 if nps > 0 else 0
    pct_detractor = (df['G1A'] <= 6).sum() / nps * 100 if nps > 0 else 0
    nps_score = round(pct_promoter - pct_detractor, 1)
    mean_kep = df['E1A'].mean()
    n_failure = df['service_failure'].sum()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Total Responden", f"{n:,}", "nasabah aktif", TEAL_MED)
    with c2:
        render_kpi("NPS Score", f"{nps_score}", f"{pct_promoter:.1f}% Promoter",
                   SUCCESS if nps_score >= 50 else WARNING)
    with c3:
        render_kpi("Kepuasan Overall", f"{mean_kep:.2f} / 6",
                   f"{mean_kep/6*100:.1f}% dari maksimal", TEAL_MED)
    with c4:
        render_kpi("Service Failure", f"{n_failure} nasabah",
                   f"{n_failure/n*100:.1f}% dari total",
                   DANGER if n_failure > 0 else SUCCESS)

def render_kpi_prioritas(df, hasil_ipa):
    """KPI bar untuk halaman Prioritas Layanan"""
    n = len(df)
    total_prioritas = sum(
        len(ipa[ipa['kuadran'] == 'Prioritas Utama'])
        for ipa in hasil_ipa.values()
    )
    dimensi_kritis = max(
        hasil_ipa.items(),
        key=lambda x: len(x[1][x[1]['kuadran'] == 'Prioritas Utama'])
    )[0]
    max_gap = max(
        ipa[ipa['kuadran'] == 'Prioritas Utama']['gap'].max()
        for ipa in hasil_ipa.values()
        if len(ipa[ipa['kuadran'] == 'Prioritas Utama']) > 0
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Total Responden", f"{n:,}", "nasabah aktif", TEAL_MED)
    with c2:
        render_kpi("Atribut Prioritas Utama", f"{total_prioritas}", "perlu perbaikan segera", DANGER)
    with c3:
        render_kpi("Dimensi Terkritis", dimensi_kritis, "atribut prioritas terbanyak", WARNING)
    with c4:
        render_kpi("Gap Terbesar", f"{max_gap:.3f}", "kepentingan - kepuasan", DANGER)

def render_kpi_cabang(df):
    """KPI bar untuk halaman Profil Cabang"""
    n_cabang = df['CABANG'].nunique()
    rata_per_cabang = df.groupby('CABANG')[['rata_teller','rata_cs','rata_atm',
                                             'rata_fisik','rata_sekuriti','rata_brand']].mean().mean(axis=1)
    cabang_terbaik = rata_per_cabang.idxmax()
    cabang_masalah = rata_per_cabang.idxmin()
    waktu_teller = df['TL5'].mean(skipna=True)
    waktu_cs = df['CS5'].mean(skipna=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Total Cabang", f"{n_cabang}", "kantor cabang", TEAL_MED)
    with c2:
        render_kpi("Cabang Terbaik", cabang_terbaik[:20], "skor tertinggi", SUCCESS)
    with c3:
        render_kpi("Perlu Perhatian", cabang_masalah[:20], "skor terendah", DANGER)
    with c4:
        render_kpi("Waktu Tunggu Rata-rata",
                   f"Teller {waktu_teller:.0f} mnt | CS {waktu_cs:.0f} mnt",
                   "waktu aktual", WARNING)

def render_kpi_emosi(df, emotion_results):
    """KPI bar untuk halaman Peta Emosi"""
    n = len(df)
    df_emosi = emotion_results['df_emosi']
    df_korelasi = emotion_results['df_korelasi']

    positif = df_emosi[df_emosi['kategori'] == 'positif']['mean_xyz'].mean()
    negatif = df_emosi[df_emosi['kategori'] == 'negatif']['mean_xyz'].mean()
    pct_positif = positif / 6 * 100
    emosi_dominan = df_emosi[df_emosi['kategori'] == 'positif'].sort_values('mean_xyz', ascending=False).iloc[0]['emosi']
    emosi_nps = df_korelasi.iloc[0]['emosi']

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Total Responden", f"{n:,}", "nasabah aktif", TEAL_MED)
    with c2:
        render_kpi("Emosi Positif Dominan", emosi_dominan, "dirasakan paling kuat", SUCCESS)
    with c3:
        render_kpi("% Emosi Positif", f"{pct_positif:.1f}%", "dari skala maksimal", TEAL_MED)
    with c4:
        render_kpi("Emosi Penentu NPS", emosi_nps, "korelasi tertinggi dengan NPS", WARNING)

def render_kpi_segmentasi(df):
    """KPI bar untuk halaman Segmentasi"""
    n = len(df)
    loyal = (df['loyalty_segment_display'] == 'Loyal Aman').sum()
    latent = (df['loyalty_segment_display'] == 'Latent Risk').sum()
    at_risk = (df['loyalty_segment_display'] == 'At Risk').sum()
    multi = df['A1AX'].apply(lambda x: pd.notna(x) and str(x).strip() != '').sum()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("Loyal Aman", f"{loyal:,}", f"{loyal/n*100:.1f}% dari total", SUCCESS)
    with c2:
        render_kpi("Latent Risk", f"{latent:,}", f"{latent/n*100:.1f}% dari total", WARNING)
    with c3:
        render_kpi("At Risk", f"{at_risk:,}", f"{at_risk/n*100:.1f}% dari total", DANGER)
    with c4:
        render_kpi("Multi-Banking", f"{multi:,}", f"{multi/n*100:.1f}% pakai bank lain", TEAL_MED)

def render_kpi_kompetitor(df, competitive_results):
    """KPI bar untuk halaman Kompetitor"""
    n = len(df)
    nps_xyz = competitive_results['nps_xyz']
    nps_komp = competitive_results['nps_komp']
    gap_nps = nps_xyz - nps_komp if nps_komp else 0
    df_bench = competitive_results['df_benchmark']
    best_dim = df_bench.loc[df_bench['gap'].idxmax(), 'dimensi']
    kompetitor_utama = df['A1XX'].value_counts()
    kompetitor_utama = kompetitor_utama[kompetitor_utama.index.str.strip() != ''].index[0] if len(kompetitor_utama) > 0 else "N/A"

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        render_kpi("NPS XYZ", f"{nps_xyz}", "vs kompetitor", SUCCESS)
    with c2:
        render_kpi("NPS Kompetitor", f"{nps_komp}", f"gap +{gap_nps:.1f} untuk XYZ", TEAL_MED)
    with c3:
        render_kpi("Dimensi Paling Unggul", best_dim, "gap terbesar vs kompetitor", SUCCESS)
    with c4:
        render_kpi("Kompetitor Utama", kompetitor_utama[:25], "paling banyak digunakan", WARNING)