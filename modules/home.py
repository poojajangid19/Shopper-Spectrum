import streamlit as st
from utils.data_loader import load_data

def show_home():

    df = load_data()

    # KPI Calculations
    total_customers = df["CustomerID"].nunique()
    total_products = df["StockCode"].nunique()
    total_transactions = df["InvoiceNo"].nunique()

    revenue = (
        df["Quantity"] *
        df["UnitPrice"]
    ).sum()

    # ==========================
    # HERO SECTION
    # ==========================

    st.markdown("""
    <div class="hero">

    <h1>🛒 Shopper Spectrum</h1>

    <h3>
    Customer Segmentation & Product Recommendation Platform
    </h3>

    <p>
    Transform Retail Data into Actionable Business Insights using
    RFM Analysis, Machine Learning and Collaborative Filtering
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ==========================
    # KPI SECTION
    # ==========================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">👥 Customers</div>
            <div class="kpi-value">{total_customers:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">📦 Products</div>
            <div class="kpi-value">{total_products:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">🧾 Transactions</div>
            <div class="kpi-value">{total_transactions:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 Revenue</div>
            <div class="kpi-value">${revenue:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # PROJECT OVERVIEW
    # ==========================

    st.markdown("""
    <div class="chart-card">

    <h3>📌 Project Overview</h3>

    <p>
    Shopper Spectrum is an E-Commerce Analytics Platform designed to
    analyze customer purchasing behavior, identify valuable customer
    segments, and generate personalized product recommendations.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # BUSINESS OBJECTIVES
    # ==========================

    st.markdown("""
<h2 style="
color:#1E40AF;
font-weight:700;
margin-bottom:20px;
">
🎯 Business Objectives
</h2>
""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="chart-card">

        <h4>👥 Customer Segmentation</h4>

        <ul>
            <li>Identify High-Value Customers</li>
            <li>Detect At-Risk Customers</li>
            <li>Improve Customer Retention</li>
            <li>Support Marketing Campaigns</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="chart-card">

        <h4>🎯 Product Recommendations</h4>

        <ul>
            <li>Personalized Shopping Experience</li>
            <li>Cross-Selling Opportunities</li>
            <li>Increase Conversion Rate</li>
            <li>Boost Revenue Growth</li>
        </ul>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

       # ==========================
    # TECHNOLOGY STACK
    # ==========================

    st.markdown("""
    <h2 style="
    color:#1E40AF;
    font-weight:700;
    margin-bottom:20px;
    ">
    🛠 Technology Stack
    </h2>
    """, unsafe_allow_html=True)

    tech1, tech2, tech3, tech4 = st.columns(4)

    with tech1:
        st.markdown("""
        <div class="kpi-card">
            <h4 style="color:#111827;">🐍 Python</h4>
        </div>
        """, unsafe_allow_html=True)

    with tech2:
        st.markdown("""
        <div class="kpi-card">
            <h4 style="color:#111827;">📊 Pandas</h4>
        </div>
        """, unsafe_allow_html=True)

    with tech3:
        st.markdown("""
        <div class="kpi-card">
            <h4 style="color:#111827;">🤖 Scikit-Learn</h4>
        </div>
        """, unsafe_allow_html=True)

    with tech4:
        st.markdown("""
        <div class="kpi-card">
            <h4 style="color:#111827;">🚀 Streamlit</h4>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # PROJECT FEATURES
    # ==========================

    st.markdown("""
    <h2 style="
    color:#1E40AF;
    font-weight:700;
    margin-bottom:20px;
    ">
    ✨ Key Features
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chart-card">

    <ul style="
    color:#111827;
    font-size:16px;
    line-height:2;
    ">

    <li>✅ Customer Segmentation using RFM Analysis</li>

    <li>✅ KMeans Clustering</li>

    <li>✅ Product Recommendation System</li>

    <li>✅ Interactive EDA Dashboard</li>

    <li>✅ Customer Insights</li>

    <li>✅ Real-Time Predictions</li>

    <li>✅ Business Intelligence Dashboard</li>

    </ul>

    </div>
    """, unsafe_allow_html=True)