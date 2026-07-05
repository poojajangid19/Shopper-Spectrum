import streamlit as st
import pandas as pd
import plotly.express as px


def show_insights():

    # ==========================
    # PAGE HEADER
    # ==========================

    st.markdown("""
    <h1 style="
    color:#1E40AF;
    font-size:42px;
    font-weight:700;
    ">
    Customer Insights
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#111827;
    font-size:24px;
    font-weight:600;
    ">
    Customer Segment Analysis & Business Recommendations
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # DATA
    # ==========================

    cluster_data = pd.DataFrame({
        "Segment": [
            "High-Value",
            "Regular",
            "Occasional",
            "At-Risk"
        ],
        "Customers": [
            800,
            1800,
            1200,
            500
        ]
    })

    total_customers = cluster_data["Customers"].sum()

    # ==========================
    # KPI CARDS
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">
                High-Value
            </div>
            <div class="kpi-value">
                800
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">
                Regular
            </div>
            <div class="kpi-value">
                1800
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">
                Occasional
            </div>
            <div class="kpi-value">
                1200
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">
                At-Risk
            </div>
            <div class="kpi-value">
                500
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # CHART SECTION
    # ==========================

    st.markdown("""
    <h2 style="
    color:#1E40AF;
    font-weight:700;
    ">
    Customer Segment Distribution
    </h2>
    """, unsafe_allow_html=True)

    fig = px.pie(
        cluster_data,
        names="Segment",
        values="Customers",
        hole=0.55
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(
            color="#111827",
            size=14
        ),
        showlegend=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # BUSINESS RECOMMENDATIONS
    # ==========================

    st.markdown("""
    <h2 style="
    color:#1E40AF;
    font-weight:700;
    ">
    Business Recommendations
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card">
        <h4>🟢 High-Value Customers</h4>
        <p>
        Offer loyalty rewards, premium memberships,
        VIP benefits, and exclusive products.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card">
        <h4>🔵 Regular Customers</h4>
        <p>
        Encourage repeat purchases through
        discounts, bundles, and personalized offers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card">
        <h4>🟠 Occasional Customers</h4>
        <p>
        Use targeted email marketing and
        personalized recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card">
        <h4>🔴 At-Risk Customers</h4>
        <p>
        Launch win-back campaigns,
        retention offers, and special discounts.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # SUMMARY CARD
    # ==========================

    st.markdown(f"""
    <div class="chart-card">
        <h3>Total Customers Analyzed</h3>
        <h2 style="color:#1E40AF;">
            {total_customers:,}
        </h2>
    </div>
    """, unsafe_allow_html=True)


    