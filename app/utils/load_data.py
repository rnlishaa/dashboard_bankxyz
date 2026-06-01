import pandas as pd
import pickle
import os
import streamlit as st

# Path yang benar — naik 2 level dari utils/ ke root project
BASE_DIR     = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR     = os.path.join(BASE_DIR, 'data', 'processed')
ANALYSIS_DIR = os.path.join(BASE_DIR, 'analysis')

@st.cache_data
def load_main_data():
    """Load data utama yang sudah bersih"""
    path = os.path.join(DATA_DIR, 'data_final.pkl')
    return pd.read_pickle(path)

@st.cache_data
def load_ipa():
    """Load hasil IPA per dimensi"""
    path = os.path.join(ANALYSIS_DIR, 'ipa_results.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_emotion():
    """Load hasil analisis emosi"""
    path = os.path.join(ANALYSIS_DIR, 'emotion_results.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_competitive():
    """Load hasil competitive intelligence"""
    path = os.path.join(ANALYSIS_DIR, 'competitive_results.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)

@st.cache_data
def load_segments():
    """Load hasil analisis segmen"""
    path = os.path.join(ANALYSIS_DIR, 'segment_results.pkl')
    with open(path, 'rb') as f:
        return pickle.load(f)