# Bank XYZ — Customer Experience Intelligence Dashboard

Dashboard analisis kepuasan nasabah Bank XYZ berbasis Streamlit.

## Struktur Folder

```
dashboard_bankxyz/
├── app/
│   ├── main.py              ← entry point Streamlit
│   ├── utils/               ← modul helper
│   └── static/              ← font & shapefile peta
├── data/
│   ├── processed/           ← data bersih (.pkl, .csv)
│   └── raw/                 ← data mentah (.xlsx)
├── analysis/                ← hasil analisis (.pkl)
├── .streamlit/
│   └── config.toml
└── requirements.txt
```

## Cara Run Lokal

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## Deploy ke Streamlit Community Cloud

1. Push repo ini ke GitHub
2. Buka https://share.streamlit.io
3. Pilih repo → set **Main file path** ke `app/main.py`
4. Klik Deploy
