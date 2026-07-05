import streamlit as st
from utils.theme import apply_theme

# -----------------------------------
# PAGE CONFIG (MUST BE FIRST)
# -----------------------------------
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------------
# CUSTOM THEME
# -----------------------------------
apply_theme()

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.image(
    "assets/logo.png",
    width=180
)

st.sidebar.markdown("""
# 🛒 Shopper Spectrum
### Retail Analytics Platform
""")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "EDA Dashboard",
        "RFM Analysis",
        "Product Recommendation",
        "Customer Segmentation",
        "Insights"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Customer Segmentation & Product Recommendation System"
)

# -----------------------------------
# PAGE ROUTING
# -----------------------------------

if page == "Home":
    from modules.home import show_home
    show_home()

elif page == "EDA Dashboard":
    from modules.eda import show_eda
    show_eda()

elif page == "RFM Analysis":
    from modules.rfm_analysis import show_rfm
    show_rfm()

elif page == "Product Recommendation":
    from modules.recommendation import show_recommendation
    show_recommendation()

elif page == "Customer Segmentation":
    from modules.segmentation import show_segmentation
    show_segmentation()

elif page == "Insights":
    from modules.insights import show_insights
    show_insights()

 