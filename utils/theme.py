import streamlit as st

def apply_theme():

    st.markdown("""
    <style>

    /* =========================
       APP BACKGROUND
    ========================= */

    .stApp {
        background-color: #F3F4F6;
    }

    .block-container {
        padding-top: 2rem;
        max-width: 1400px;
    }
/* =========================
   TEXT INPUT
========================= */

.stTextInput input {
    background-color: white !important;
    color: #111827 !important;
    border: 2px solid #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 10px !important;
    font-size: 16px !important;
}

.stTextInput input:focus {
    border: 2px solid #1E40AF !important;
    box-shadow: 0 0 0 1px #1E40AF !important;
}

/* Placeholder */

.stTextInput input::placeholder {
    color: #111827 !important;
    opacity: 0.6 !important;
}
    /* =========================
       SIDEBAR
    ========================= */

    [data-testid="stSidebar"]{
        background: linear-gradient(
        180deg,
        #0F172A,
        #1E3A8A
        );
        border-right:1px solid #334155;
    }

    [data-testid="stSidebar"] *{
        color:white !important;
    }
/* =========================
   RECOMMENDATION CARD
========================= */

.recommend-card{
    background:white;
    padding:18px;
    border-radius:14px;
    margin-bottom:12px;
    border-left:6px solid #1E40AF;
    box-shadow:0px 4px 12px rgba(0,0,0,0.06);
    color:#111827;
    font-size:18px;
    font-weight:600;
}

.recommend-card:hover{
    transform:translateX(5px);
    transition:0.3s;
}
                

                /* =========================
   NUMBER INPUTS
========================= */

.stNumberInput input{
    background:white !important;
    color:#111827 !important;
    border:2px solid #CBD5E1 !important;
    border-radius:12px !important;
}

.stNumberInput input:focus{
    border:2px solid #1E40AF !important;
}

/* =========================
   SEGMENT CARDS
========================= */

.segment-high{
    background:linear-gradient(
    135deg,
    #10B981,
    #059669
    );
    color:white;
    padding:30px;
    border-radius:18px;
    text-align:center;
    font-size:28px;
    font-weight:700;
    margin-top:20px;
}

.segment-regular{
    background:linear-gradient(
    135deg,
    #3B82F6,
    #2563EB
    );
    color:white;
    padding:30px;
    border-radius:18px;
    text-align:center;
    font-size:28px;
    font-weight:700;
    margin-top:20px;
}

.segment-occasional{
    background:linear-gradient(
    135deg,
    #F59E0B,
    #D97706
    );
    color:white;
    padding:30px;
    border-radius:18px;
    text-align:center;
    font-size:28px;
    font-weight:700;
    margin-top:20px;
}

.segment-risk{
    background:linear-gradient(
    135deg,
    #EF4444,
    #DC2626
    );
    color:white;
    padding:30px;
    border-radius:18px;
    text-align:center;
    font-size:28px;
    font-weight:700;
    margin-top:20px;
}
    /* =========================
       HERO SECTION
    ========================= */

    .hero{
        background: linear-gradient(
        135deg,
        #2563EB,
        #1E40AF
        );
        padding:40px;
        border-radius:20px;
        text-align:center;
        color:white;
        margin-bottom:25px;
        box-shadow:0 8px 20px rgba(37,99,235,0.25);
    }

    .hero h1{
        font-size:48px;
        margin-bottom:10px;
    }

    .hero h3{
        color:white !important;
    }

    .hero p{
        color:white !important;
        opacity:.9;
    }

    /* =========================
       KPI CARDS
    ========================= */

    .kpi-card{
        background:white;
        padding:25px;
        border-radius:20px;
        text-align:center;
        border:1px solid #E5E7EB;
        box-shadow:0px 4px 15px rgba(0,0,0,0.08);
        transition:0.3s;
    }

    .kpi-card:hover{
        transform:translateY(-4px);
    }

    /* TITLE DARK BLUE */

    .kpi-title{
        color:#1E40AF;
        font-size:18px;
        font-weight:600;
        margin-bottom:15px;
    }

    /* VALUE BLACK */

    .kpi-value{
        color:#111827;
        font-size:30px;
        font-weight:700;
    }
        .kpi-card h4 {
            color: #111827 !important;
            font-weight: 600;
        }

        .chart-card ul,
        .chart-card li {
            color: #111827 !important;
        }
    /* =========================
       CONTENT CARDS
    ========================= */

    .chart-card{
        background:white;
        padding:25px;
        border-radius:20px;
        border:1px solid #E5E7EB;
        box-shadow:0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom:20px;
    }

    .chart-card h3{
        color:#1E40AF;
        font-size:20px;
        margin-bottom:15px;
    }

    .chart-card h4{
        color:#2563EB;
    }

    .chart-card p,
    .chart-card li{
        color:#374151;
        font-size:18px;
        line-height:1.8;
    }

    /* =========================
       BUTTONS
    ========================= */

    .stButton button{
        width:100%;
        border:none;
        border-radius:12px;
        padding:12px;
        font-size:16px;
        font-weight:600;
        color:white;
        background:linear-gradient(
        135deg,
        #2563EB,
        #1E40AF
        );
    }

    /* =========================
       INPUTS
    ========================= */

    .stTextInput input,
    .stNumberInput input{
        border-radius:12px !important;
    }

    /* =========================
       STREAMLIT METRICS
    ========================= */

    div[data-testid="stMetric"]{
        background:white;
        padding:20px;
        border-radius:18px;
        border:1px solid #E5E7EB;
        box-shadow:0px 4px 12px rgba(0,0,0,0.06);
    }

    div[data-testid="stMetricLabel"]{
        color:#1E40AF !important;
        font-size:16px !important;
        font-weight:600 !important;
    }

    div[data-testid="stMetricValue"]{
        color:#111827 !important;
        font-size:34px !important;
        font-weight:700 !important;
    }

    /* =========================
       HEADINGS
    ========================= */

    h1,h2,h3{
        color:#0F172A;
    }
.insight-card{
    background:white;
    padding:20px;
    border-radius:18px;
    border-left:6px solid #1E40AF;
    margin-bottom:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.06);
}
                
                /* =========================
   INPUT LABELS
========================= */

label {
    color: #111827 !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* Number Input Labels */

.stNumberInput label {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Text Input Labels */

.stTextInput label {
    color: #111827 !important;
    font-weight: 600 !important;
}
                div[data-testid="stNumberInput"] label {
    color: #111827 !important;
    font-weight: 600 !important;
}

div[data-testid="stTextInput"] label {
    color: #111827 !important;
    font-weight: 600 !important;
}
    </style>
    """, unsafe_allow_html=True)