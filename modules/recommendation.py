import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from utils.data_loader import load_data


def show_recommendation():

    # ==========================
    # PAGE HEADER
    # ==========================

    st.markdown("""
    <h1 style="
    color:#1E40AF;
    font-size:42px;
    font-weight:700;
    ">
    Product Recommendation System
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#111827;
    font-size:24px;
    font-weight:600;
    ">
    Find Similar Products Using Collaborative Filtering
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # LOAD DATA
    # ==========================

    df = load_data()

    # Remove missing values

    df = df.dropna(subset=["CustomerID", "Description"])

    # ==========================
    # CUSTOMER PRODUCT MATRIX
    # ==========================

    customer_product = pd.pivot_table(
        df,
        index="CustomerID",
        columns="Description",
        values="Quantity",
        aggfunc="sum",
        fill_value=0
    )

    # ==========================
    # COSINE SIMILARITY
    # ==========================

    similarity_matrix = cosine_similarity(
        customer_product.T
    )

    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=customer_product.columns,
        columns=customer_product.columns
    )

    # ==========================
    # PRODUCT LIST
    # ==========================

    products = sorted(
        df["Description"]
        .dropna()
        .unique()
    )

    product_name = st.selectbox(
        "Select Product",
        products
    )

    # ==========================
    # RECOMMENDATION FUNCTION
    # ==========================

    def get_recommendations(product):

        try:

            similar_products = (
                similarity_df[product]
                .sort_values(ascending=False)
                .iloc[1:6]
            )

            return similar_products.index.tolist()

        except:
            return []

    # ==========================
    # BUTTON
    # ==========================

    if st.button("🔍 Get Recommendations"):

        recommendations = get_recommendations(
            product_name
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <h2 style="
        color:#1E40AF;
        font-weight:700;
        ">
        Recommended Products
        </h2>
        """, unsafe_allow_html=True)

        if len(recommendations) == 0:

            st.warning(
                "No recommendations found."
            )

        else:

            for product in recommendations:

                st.markdown(f"""
                <div class="recommend-card">
                    ⭐ {product}
                </div>
                """, unsafe_allow_html=True)