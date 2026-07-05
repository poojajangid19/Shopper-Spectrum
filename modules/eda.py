import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

def show_eda():


    st.markdown("""
<h1 style='
color:#1E40AF;
font-weight:700;
margin-bottom:20px;
'>
EDA Dashboard
</h1>
""", unsafe_allow_html=True)

    df = load_data()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Sales"] = df["Quantity"] * df["UnitPrice"]

    # Monthly Sales
    df["Month"] = df["InvoiceDate"].dt.to_period("M").astype(str)

    monthly_sales = (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        monthly_sales,
        x="Month",
        y="Sales",
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # Top Products
    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top Selling Products"
    )

    st.plotly_chart(fig2, use_container_width=True)


