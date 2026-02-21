import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.theme import Components, Colors, apply_chart_theme, init_page

init_page("Netflix Stock Analysis", "💹")

# Load custom CSS
try:
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
        st.warning("Custom CSS file not found. Using default styling.")
# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('netflix_analyzed.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df
df = load_data()

# Title
st.markdown(
    Components.page_header(
        "💹 Netflix Stock Analysis Dashboard"), unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    Components.section_header('Key Metrics', '🎯'), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Start Analysis Period",
        value=f"{df['Date'].min().strftime('%Y-%m-%d')}",
        delta="Start",
        card_type="info"
    ), unsafe_allow_html=True)
with col2:
    st.markdown(
        Components.metric_card(
        title="Total Trading Days",
        value=f"{len(df)}",
        delta="Trading Days",
        card_type="info"
    ), unsafe_allow_html=True)
with col3:
    st.markdown(
        Components.metric_card(
            title="End Analisys Period",
            value=f"{df['Date'].max().strftime('%Y-%m-%d')}",
            delta="End",
            card_type="info"
        ), unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    Components.section_header("Price Trend Visualization", "📈"),
    unsafe_allow_html=True
)

with st.container():
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['Close'], 
        name='Close Price',
        line=dict(color='#E50914', width=1.5)
    ))
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df['MA_30'], 
        name='30-Day MA',
        line=dict(color='orange', dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=df['Date'], 
        y=df['MA_90'], 
        name='90-Day MA',
        line=dict(color='green', dash='dot')
    ))
                                
    fig.update_layout(
        title='Netflix Stock Price Over Time',
        xaxis_title='Date',
        yaxis_title='Price (USD)'
    )
    fig = apply_chart_theme(fig)
    st.plotly_chart(fig, width='stretch', height=500)

st.markdown("---")
st.markdown(
    Components.section_header("Volume Analysis", "📇"),
    unsafe_allow_html=True
)

with st.container():
    fig2 = make_subplots(
        rows=2, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.1,
        subplot_titles=("Price", "Volume")
    )
    
    fig2.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Close'],
            name="Close Price",
            line=dict(color="#E50914")
        ),
        row=1, col=1
    )
    fig2.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Volume'],
            name="Volume",
            line=dict(color='darkgreen', width=2)
        ),
        row=2, col=1
    )
    fig2.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Volume_MA_30'],
            name="Vol MA 30",
            line=dict(color='yellow', width=2.5, dash='dash')
        ),
        row=2, col=1
    )
    fig2.update_layout(
        title_text="Netflix Stock Price and Trading Volume",
        showlegend=True
    )
    fig2 = apply_chart_theme(fig2)
    st.plotly_chart(fig2, width="stretch", height=600)

st.markdown("---")
st.markdown(
    Components.section_header("Price Statistics", "💰"),
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Starting Price",
        value=f"${df['Close'].iloc[0]:.2f}",
        delta="Start Price",
        card_type="success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="Ending Price",
        value=f"${df['Close'].iloc[-1]:.2f}",
        delta="End Price",
        card_type="warning"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="Average Close",
            value=f"${df['Close'].mean():.2f}",
            delta="Close Price",
            card_type="info"
        ), unsafe_allow_html=True
    )
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Overall Return",
        value=f"{((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0] * 100):.2f}%",
        delta="Return",
        card_type="info"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="Highest Price",
        value=f"${df['High'].max():.2f}",
        delta=f"{df.loc[df['High'].idxmax(), 'Date'].strftime('%Y-%m-%d')}",
        card_type="error"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="Lowest Price",
            value=f"${df['Low'].min():.2f}",
            delta=f"{df.loc[df['Low'].idxmin(), 'Date'].strftime('%Y-%m-%d')}",
            card_type="success"
        ), unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    Components.section_header("Returns & Volatility", "📇"),
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Average Daily Returns",
        value=f"{df['Daily_Return'].mean():.3f}%",
        delta="Average",
        card_type="info"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="Median Daily Return",
        value=f"{df['Daily_Return'].median():.3f}%",
        delta="Median",
        card_type="info"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="Daily Return Std Dev",
            value=f"{df['Daily_Return'].std():.3f}%",
            delta="Standard Deviation",
            card_type="warning"
        ), unsafe_allow_html=True
    )
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Best Day",
        value=f"+{df['Daily_Return'].max():.2f}%",
        delta=f"{df.loc[df['Daily_Return'].idxmax(), 'Date'].strftime('%Y-%m-%d')}",
        card_type="success"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="Worst Day",
        value=f"{df['Daily_Return'].min():.2f}%",
        delta=f"{df.loc[df['Daily_Return'].idxmin(), 'Date'].strftime('%Y-%m-%d')}",
        card_type="error"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="Average 30-Day Volatility",
            value=f"{df['Volatility_30'].mean():.3f}%",
            delta="Average",
            card_type="info"
        ), unsafe_allow_html=True
    )

st.markdown("---")
st.markdown(
    Components.section_header("Volume Statistics", "📊"),
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        Components.metric_card(
        title="Average Daily Volume",
        value=f"{df['Volume'].mean():,.0f}",
        delta="Average",
        card_type="info"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="Highest Volume",
        value=f"{df['Volume'].max():,.0f}",
        delta=f"{df.loc[df['Volume'].idxmax(), 'Date'].strftime('%Y-%m-%d')}",
        card_type="success"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="Lowest Volume",
            value=f"{df['Volume'].min():,.0f}",
            delta=f"{df.loc[df['Volume'].idxmin(), 'Date'].strftime('%Y-%m-%d')}",
            card_type="error"
        ), unsafe_allow_html=True
    )


st.markdown("---")
st.markdown(
    Components.section_header("Technical Indicators", "🎯"),
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        Components.metric_card(
        title="Current RSI",
        value=f"{df['RSI'].iloc[-1]:.2f}",
        delta="RSI",
        card_type="info"
    ), unsafe_allow_html=True)

with col2:
    st.markdown(
        Components.metric_card(
        title="7-Day MA",
        value=f"${df['MA_7'].iloc[-1]:.2f}",
        delta="7-Day",
        card_type="info"
    ), unsafe_allow_html=True)

with col3:
    st.markdown(
        Components.metric_card(
            title="30-Day MA",
            value=f"${df['MA_30'].iloc[-1]:.2f}",
            delta="30-Day",
            card_type="info"
        ), unsafe_allow_html=True
    )
with col4:
    st.markdown(
        Components.metric_card(
            title="90-Day MA",
            value=f"${df['MA_90'].iloc[-1]:.2f}",
            delta="90-Day",
            card_type="info"
        ), unsafe_allow_html=True
    )