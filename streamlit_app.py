import streamlit as st
import sys
import os
from utils.theme import Components, Colors, apply_chart_theme, init_page


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
pages = [
    {
        "title": "Employee Analytics",
        "emoji": "🎯",
        "description": "Workforce insights, HR metrics & team performance",
        "path": "pages/1_🎯_Employee_Analytics_Dashboard.py",
        "color": "#4F46E5",
        "bg": "#EEF2FF",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/employee.png",
    },
    {
        "title": "Sales Performance",
        "emoji": "📊",
        "description": "Revenue trends, pipeline & sales KPIs",
        "path": "pages/2_📊_Sales_Performance_Dashboard.py",
        "color": "#059669",
        "bg": "#ECFDF5",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/sales.png",
    },
    {
        "title": "Healthcare Symptoms",
        "emoji": "🏥",
        "description": "Patient data, symptom patterns & health analytics",
        "path": "pages/3_🏥_Healthcare_Symptoms_Analytics_Dashboard.py",
        "color": "#DC2626",
        "bg": "#FEF2F2",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/healthcare.png",
    },
    {
        "title": "Madrid Weather",
        "emoji": "🌤️",
        "description": "Daily weather patterns & climate analysis for Madrid",
        "path": "pages/4_🌤️_Madrid_Daily_Weather_Analysis_Dashboard.py",
        "color": "#D97706",
        "bg": "#FFFBEB",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/weather.png",
    },
    {
        "title": "Netflix Stock",
        "emoji": "💹",
        "description": "Stock price history, trends & financial metrics",
        "path": "pages/5_💹_Netflix_Stock_Analysis_Dashboard.py",
        "color": "#E50914",
        "bg": "#FFF1F2",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/stocks.png",
    },
    {
        "title": "Retail Inventory",
        "emoji": "📦",
        "description": "Stock levels, turnover rates & supply chain insights",
        "path": "pages/6_📦_Retail_Inventory_Analysis_Dashboard.py",
        "color": "#7C3AED",
        "bg": "#F5F3FF",
        "image": "https://raw.githubusercontent.com/luis-c2255/blank-app/main/utils/retail.png",
    },
]
st.markdown("""
    <style>
        /* Stylize the search input */
        div[data-testid="stSidebarNavSearch"] input {
            border: 1px solid #4cc9a6 !important;
            border-radius: 5px;
        }
        /* Highlight the navigation links to look like buttons */
        [data-testid="stSidebarNav"] ul {
            padding-top: 2rem;
        }
        [data-testid="stSidebarNav"] li {
            background-color: #1a2c42; /* Darker blue background */
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #4cc9a6; /* Your Mint Leaf color */
            transition: 0.3s;
        }
        [data-testid="stSidebarNav"] li:hover {
            background-color: #4cc9a6;
            transform: translateX(5px);
        }
        [data-testid="stSidebarNav"] span {
            color: white !important;
            font-weight: bold;
        }
        .card {
            border-radius: 16px;
            padding: 2rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            border: 1.5px solid transparent;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            position: relative;
            overflow: hidden;
            pointer-events: none;
        }
        .card-emoji { font-size: 2.5rem; line-weight: 1; }
        .card-title  { font-size: 1.2rem; font-weight: 700; margin: 0; }
        .card-desc { font-size: 0.875rem; margin: 0; opacity: 0.75; line-height: 1.5; }
        .card-arrow {
            position: absolute;
            right: 1.5rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 1.25rem;
            opacity: 0.4;
        }
        .card-wrapper {
            position: relative;
            border-radius: 16px;
            margin-bottom: 1rem;
        }
        .card-wrapper:hover .card {
            transform: translateY(-4px);
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);
        }
        .card-wrapper:hover .card-arrow { opacity: 0.9; }
        /* The invisible Streamlit button stretched over the card */
        .card-wrapper .stButton {
            position: absolute !important;
            inset: 0 !important;
            z-index: 10 !important;
        }
        .card-wrapper .stButton > button {
            width: 100% !important;
            height: 100% !important;
            opacity: 0 !important;
            cursor: pointer !important;
            border-radius: 16px !important;
        }
        </style>
""", unsafe_allow_html=True)

st.markdown(
    Components.page_header("📊 Multiple Analysis Dashboard"), unsafe_allow_html=True)
    
for row_start in range(0, len(pages), 2):
    row_pages = pages[row_start : row_start +2]
    cols = st.columns(2, gap="medium")
    
    for col, page in zip(cols, row_pages):
        with col:
            st.markdown(f"""
            <div class="card-wrapper">
                <div class="card" style="border-color:{page['color']}22;">
                <img src="{page['image']}"
                    style="width:100%; height: 160px; object-fit:cover; border-radius:10px; margin-bottom:0.5rem;">
                <div style="background:{page['bg']}; padding:0.5rem; border-radius:8px; color:{page['color']};">
                    <span class="card-emoji">{page['emoji']}</span>
                    <p class="card-title">{page['title']}</p>
                    <p class="card-desc">{page['description']}</p>
                </div>
                <span class="card-arrow">→</span>
            </div>
        """, unsafe_allow_html=True)
        if st.button("navigate", key=f"btn_{page['path']}"):
            st.switch_page(page['path'])
        st.markdown("</div", unsafe_allow_html=True)

# Load custom CSS
try:
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Custom CSS file not found. Using default styling.")

# ============================================
# FOOTER
# ============================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>📊 Multiple Analysis Dashboard</strong></p>
    <p>Multiple Dashboards from several datasets analyzed</p>
    <p style='font-size: 0.9rem;'>Navigate using the sidebar to explore different datasets</p>
</div>
""", unsafe_allow_html=True)