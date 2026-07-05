import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.rfm import create_rfm


def show_rfm():

    # ==========================
    # PAGE HEADER
    # ==========================

    st.markdown("""
    <h1 style="
    color:#1E40AF;
    font-size:42px;
    font-weight:700;
    ">
    RFM Analysis
    </h1>
    """, unsafe_allow_html=True)

    # Load Data
    df = load_data()
    rfm = create_rfm(df)

    # ==========================
    # DATASET
    # ==========================

    st.markdown("""
    <h3 style="
    color:#111827;
    font-size:24px;
    font-weight:600;
    ">
    RFM Dataset
    </h3>
    """, unsafe_allow_html=True)

    st.dataframe(rfm.head(), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # KPI SECTION
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Avg Recency",
            round(rfm["Recency"].mean(), 1)
        )

    with col2:
        st.metric(
            "Avg Frequency",
            round(rfm["Frequency"].mean(), 1)
        )

    with col3:
        st.metric(
            "Avg Monetary",
            round(rfm["Monetary"].mean(), 1)
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # RECENCY DISTRIBUTION
    # ==========================

    st.markdown("""
    <h3 style="
    color:#1E40AF;
    text-align:center;
    font-weight:700;
    ">
    📅 Recency Distribution
    </h3>
    """, unsafe_allow_html=True)

    fig1 = px.histogram(
        rfm,
        x="Recency"
    )

    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#111827"),
        xaxis_title="Recency",
        yaxis_title="Count"
    )

    fig1.update_xaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    fig1.update_yaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    st.plotly_chart(fig1, use_container_width=True)

    # ==========================
    # FREQUENCY DISTRIBUTION
    # ==========================

    st.markdown("""
    <h3 style="
    color:#1E40AF;
    text-align:center;
    font-weight:700;
    ">
    🔄 Frequency Distribution
    </h3>
    """, unsafe_allow_html=True)

    fig2 = px.histogram(
        rfm,
        x="Frequency"
    )

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#111827"),
        xaxis_title="Frequency",
        yaxis_title="Count"
    )

    fig2.update_xaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    fig2.update_yaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    st.plotly_chart(fig2, use_container_width=True)

    # ==========================
    # MONETARY DISTRIBUTION
    # ==========================

    st.markdown("""
    <h3 style="
    color:#1E40AF;
    text-align:center;
    font-weight:700;
    ">
    💰 Monetary Distribution
    </h3>
    """, unsafe_allow_html=True)

    fig3 = px.histogram(
        rfm,
        x="Monetary"
    )

    fig3.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#111827"),
        xaxis_title="Monetary",
        yaxis_title="Count"
    )

    fig3.update_xaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    fig3.update_yaxes(
        title_font=dict(color="#111827", size=16),
        tickfont=dict(color="#111827")
    )

    st.plotly_chart(fig3, use_container_width=True)