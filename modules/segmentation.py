import streamlit as st

def show_segmentation():

    # ==========================
    # PAGE HEADER
    # ==========================

    st.markdown("""
    <h1 style="
    color:#1E40AF;
    font-size:42px;
    font-weight:700;
    ">
   Customer Segmentation
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h3 style="
    color:#111827;
    font-size:24px;
    font-weight:600;
    ">
    Enter Customer RFM Values
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # INPUTS
    # ==========================

    col1, col2, col3 = st.columns(3)

    with col1:
        recency = st.number_input(
            "Recency (Days)",
            min_value=0,
            value=30
        )

    with col2:
        frequency = st.number_input(
            "Frequency",
            min_value=0,
            value=10
        )

    with col3:
        monetary = st.number_input(
            "Monetary Value",
            min_value=0.0,
            value=500.0
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # PREDICT
    # ==========================

    if st.button("🎯 Predict Segment"):

        if frequency > 20 and monetary > 1000 and recency < 30:

            st.markdown("""
            <div class="segment-high">
            🟢 High-Value Customer
            </div>
            """, unsafe_allow_html=True)

        elif frequency > 10 and monetary > 500:

            st.markdown("""
            <div class="segment-regular">
            🔵 Regular Customer
            </div>
            """, unsafe_allow_html=True)

        elif recency > 100:

            st.markdown("""
            <div class="segment-risk">
            🔴 At-Risk Customer
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="segment-occasional">
            🟠 Occasional Customer
            </div>
            """, unsafe_allow_html=True)