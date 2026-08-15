import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import time


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Hotel Booking AI | Prediction",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# DESIGN SYSTEM
# ============================================================

COLORS = {
    "background": "#07111F",
    "surface": "#0D1B2A",
    "surface_light": "#12243A",

    "primary": "#3B82F6",
    "primary_light": "#60A5FA",
    "secondary": "#8B5CF6",

    "text": "#F8FAFC",
    "text_muted": "#94A3B8",
    "text_soft": "#64748B",

    "border": "rgba(148, 163, 184, 0.12)"
}


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("hotel_booking_xgboost_pipeline.pkl")


try:
    model = load_model()
    model_loaded = True
    model_error = None

except Exception as e:
    model = None
    model_loaded = False
    model_error = str(e)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(f"""

<style>

:root {{

    --bg: {COLORS["background"]};
    --surface: {COLORS["surface"]};
    --surface-light: {COLORS["surface_light"]};

    --primary: {COLORS["primary"]};
    --primary-light: {COLORS["primary_light"]};
    --secondary: {COLORS["secondary"]};

    --text: {COLORS["text"]};
    --muted: {COLORS["text_muted"]};
    --soft: {COLORS["text_soft"]};

    --border: {COLORS["border"]};

}}


/* ============================================================
   STREAMLIT
============================================================ */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    background: transparent !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}


/* ============================================================
   APP BACKGROUND
============================================================ */

.stApp {{

    background:

        radial-gradient(
            circle at 10% 5%,
            rgba(59,130,246,0.10),
            transparent 25%
        ),

        radial-gradient(
            circle at 90% 25%,
            rgba(139,92,246,0.08),
            transparent 25%
        ),

        var(--bg);

    color: var(--text);

}}


/* ============================================================
   SIDEBAR
============================================================ */

[data-testid="stSidebar"] {{

    background:

        linear-gradient(
            180deg,
            #0B1728 0%,
            #0D1B2A 55%,
            #111C35 100%
        ) !important;

    border-right:
        1px solid
        rgba(96,165,250,0.12);

    box-shadow:
        10px 0 40px
        rgba(0,0,0,0.25);

}}


[data-testid="stSidebar"] > div:first-child {{
    padding-top: 1.5rem;
}}


/* ============================================================
   SIDEBAR BRAND
============================================================ */

.sidebar-brand {{

    padding: 20px;

    margin: 5px 5px 20px;

    border-radius: 18px;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.10),
            rgba(139,92,246,0.08)
        );

    border:
        1px solid
        rgba(96,165,250,0.15);

    animation:
        fadeInLeft 0.7s ease-out both;

}}


.sidebar-brand-title {{

    font-size: 18px;

    font-weight: 900;

    color: #F8FAFC;

}}


.sidebar-brand-title span {{

    background:

        linear-gradient(
            90deg,
            #60A5FA,
            #818CF8,
            #A78BFA
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}}


.sidebar-brand-subtitle {{

    margin-top: 5px;

    font-size: 10px;

    color: #64748B;

    letter-spacing: 1px;

}}


/* ============================================================
   SIDEBAR NAV
============================================================ */

[data-testid="stSidebarNav"] {{
    padding: 10px;
}}


[data-testid="stSidebarNav"]::before {{

    content: "HOTEL BOOKING AI";

    display: block;

    color: #F8FAFC;

    font-size: 18px;

    font-weight: 900;

    letter-spacing: -0.5px;

    padding: 10px 14px 18px;

    border-bottom:
        1px solid
        rgba(148,163,184,0.08);

    margin-bottom: 12px;

}}


[data-testid="stSidebarNav"] a {{

    display: flex;

    align-items: center;

    border-radius: 12px;

    padding: 12px 14px;

    margin: 6px 0;

    color: #94A3B8 !important;

    background: transparent;

    border:
        1px solid
        transparent;

    transition:
        all 0.3s ease;

}}


[data-testid="stSidebarNav"] a:hover {{

    color: #F8FAFC !important;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.10),
            rgba(139,92,246,0.06)
        );

    border:
        1px solid
        rgba(96,165,250,0.18);

    transform:
        translateX(4px);

}}


[data-testid="stSidebarNav"]
a[aria-current="page"] {{

    color: #FFFFFF !important;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.18),
            rgba(139,92,246,0.12)
        );

    border:
        1px solid
        rgba(96,165,250,0.28);

    box-shadow:
        0 8px 30px
        rgba(59,130,246,0.12);

}}


/* ============================================================
   MAIN CONTAINER
============================================================ */

.prediction-container {{

    max-width: 1350px;

    margin: auto;

    padding: 20px 40px 60px;

}}


/* ============================================================
   HERO
============================================================ */

.prediction-hero {{

    position: relative;

    overflow: hidden;

    padding: 55px 65px;

    margin-bottom: 30px;

    border-radius: 30px;

    background:

        linear-gradient(
            135deg,
            #0B1728 0%,
            #0D1B2A 55%,
            #111C35 100%
        );

    border:
        1px solid
        var(--border);

    box-shadow:
        0 30px 80px
        rgba(0,0,0,0.30);

    animation:
        heroEntrance 0.9s
        cubic-bezier(.2,.8,.2,1)
        both;

}}


.prediction-hero::before {{

    content: "";

    position: absolute;

    width: 300px;

    height: 300px;

    right: 15%;

    bottom: -230px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle,
            rgba(96,165,250,0.15),
            transparent 70%
        );

    animation:
        floatingGlow 5s ease-in-out infinite;

}}


.prediction-hero::after {{

    content: "";

    position: absolute;

    width: 420px;

    height: 420px;

    right: -160px;

    top: -190px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle,
            rgba(59,130,246,0.24),
            transparent 68%
        );

    filter: blur(10px);

    animation:
        pulseGlow 4s ease-in-out infinite;

}}


.prediction-content {{

    position: relative;

    z-index: 2;

}}


.prediction-badge {{

    display: inline-flex;

    align-items: center;

    gap: 9px;

    padding: 8px 15px;

    border-radius: 50px;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.20);

    color:
        var(--primary-light);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 2px;

    animation:
        fadeInUp 0.8s 0.15s both;

}}


.prediction-dot {{

    width: 7px;

    height: 7px;

    border-radius: 50%;

    background:
        var(--primary-light);

    box-shadow:
        0 0 12px
        rgba(96,165,250,0.8);

    animation:
        dotPulse 1.6s infinite;

}}


.prediction-hero h1 {{

    margin: 22px 0 15px;

    font-size: clamp(42px, 5vw, 64px);

    line-height: 1.05;

    letter-spacing: -3px;

    font-weight: 900;

    color: var(--text);

    animation:
        fadeInUp 0.8s 0.25s both;

}}


.prediction-hero h1 span {{

    background:

        linear-gradient(
            90deg,
            #60A5FA,
            #818CF8,
            #A78BFA
        );

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

    background-size: 200% auto;

    animation:
        gradientMove 4s linear infinite;

}}


.prediction-description {{

    max-width: 800px;

    color: var(--muted);

    font-size: 16px;

    line-height: 1.8;

    animation:
        fadeInUp 0.8s 0.4s both;

}}


/* ============================================================
   FORM SECTION
============================================================ */

.form-section {{

    margin: 25px 0;

    padding: 30px;

    border-radius: 22px;

    background:

        linear-gradient(
            145deg,
            rgba(13,27,42,0.92),
            rgba(10,22,38,0.75)
        );

    border:
        1px solid
        var(--border);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.18);

    animation:
        fadeInUp 0.7s
        cubic-bezier(.2,.8,.2,1)
        both;

    transition:
        transform 0.3s ease,
        border-color 0.3s ease;

}}


.form-section:hover {{

    transform:
        translateY(-2px);

    border-color:
        rgba(96,165,250,0.18);

}}


/* ============================================================
   FORM HEADER
============================================================ */

.form-header {{

    display: flex;

    align-items: center;

    gap: 15px;

    margin-bottom: 28px;

    padding-bottom: 20px;

    border-bottom:
        1px solid
        rgba(148,163,184,0.08);

}}


.form-icon {{

    width: 52px;

    height: 52px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 14px;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.14);

    font-size: 22px;

    animation:
        iconFloat 3s ease-in-out infinite;

}}


.form-title {{

    color: var(--text);

    font-size: 20px;

    font-weight: 850;

}}


.form-subtitle {{

    margin-top: 5px;

    color: var(--soft);

    font-size: 12px;

}}


/* ============================================================
   INPUTS
============================================================ */

[data-testid="stWidgetLabel"] label {{

    color:
        #CBD5E1 !important;

    font-size:
        12px !important;

    font-weight:
        700 !important;

}}


div[data-baseweb="select"] > div {{

    background:
        #0D1B2A !important;

    border:
        1px solid
        rgba(148,163,184,0.15) !important;

    border-radius:
        10px !important;

    transition:
        all 0.25s ease;

}}


div[data-baseweb="select"] > div:hover {{

    border-color:
        rgba(96,165,250,0.45) !important;

    transform:
        translateY(-1px);

}}


div[data-baseweb="select"] span {{

    color:
        #F8FAFC !important;

}}


input {{

    background:
        #0D1B2A !important;

    color:
        #F8FAFC !important;

    border:
        1px solid
        rgba(148,163,184,0.15) !important;

    border-radius:
        10px !important;

    transition:
        all 0.25s ease;

}}


input:hover {{

    border-color:
        rgba(96,165,250,0.35) !important;

}}


input:focus {{

    border-color:
        #60A5FA !important;

    box-shadow:
        0 0 0 2px
        rgba(96,165,250,0.12) !important;

}}


/* ============================================================
   BUTTON
============================================================ */

.predict-button-container {{

    max-width:
        600px;

    margin:
        40px auto;

}}


.stButton > button {{

    width:
        100%;

    min-height:
        60px;

    border:
        none !important;

    border-radius:
        15px !important;

    background:

        linear-gradient(
            135deg,
            #2563EB,
            #6366F1
        ) !important;

    background-size:
        200% auto !important;

    color:
        white !important;

    font-size:
        15px !important;

    font-weight:
        850 !important;

    box-shadow:
        0 15px 35px
        rgba(59,130,246,0.20);

    transition:
        all 0.3s ease;

    animation:
        buttonEntrance 0.7s ease-out both;

}}


.stButton > button:hover {{

    transform:
        translateY(-4px)
        scale(1.01);

    background-position:
        right center !important;

    box-shadow:
        0 20px 50px
        rgba(59,130,246,0.38);

}}


.stButton > button:active {{

    transform:
        translateY(0)
        scale(0.98);

}}


/* ============================================================
   LOADING
============================================================ */

.loading-box {{

    max-width:
        600px;

    margin:
        30px auto;

    padding:
        35px;

    text-align:
        center;

    border-radius:
        20px;

    background:
        rgba(59,130,246,0.06);

    border:
        1px solid
        rgba(96,165,250,0.15);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.20);

    animation:
        loadingAppear 0.5s ease-out both;

}}


.loader {{

    width:
        48px;

    height:
        48px;

    margin:
        auto;

    border:
        4px solid
        rgba(96,165,250,0.15);

    border-top:
        4px solid
        #60A5FA;

    border-right:
        4px solid
        #818CF8;

    border-radius:
        50%;

    animation:
        spin 0.8s linear infinite;

}}


.loading-text {{

    margin-top:
        18px;

    color:
        #CBD5E1;

    font-size:
        14px;

    font-weight:
        700;

}}


/* ============================================================
   LOADING STEPS
============================================================ */

.loading-steps {{

    margin-top:
        25px;

    display:
        flex;

    flex-direction:
        column;

    gap:
        10px;

    text-align:
        left;

}}


.loading-step {{

    padding:
        10px 14px;

    border-radius:
        10px;

    color:
        #64748B;

    font-size:
        12px;

    background:
        rgba(255,255,255,0.02);

    transition:
        all 0.3s ease;

}}


.loading-step.active {{

    color:
        #60A5FA;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.15);

    animation:
        stepPulse 1.2s infinite;

}}


.loading-step.completed {{

    color:
        #93C5FD;

    background:
        rgba(59,130,246,0.05);

}}


/* ============================================================
   RESULT
============================================================ */

.result-wrapper {{

    margin-top:
        40px;

    padding:
        42px;

    border-radius:
        25px;

    text-align:
        center;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.10),
            rgba(139,92,246,0.08)
        );

    border:
        1px solid
        rgba(96,165,250,0.22);

    box-shadow:
        0 25px 60px
        rgba(0,0,0,0.20);

    animation:
        resultEntrance
        0.8s
        cubic-bezier(.16,1,.3,1)
        both;

    position:
        relative;

    overflow:
        hidden;

}}


.result-wrapper::before {{

    content:
        "";

    position:
        absolute;

    width:
        250px;

    height:
        250px;

    left:
        -120px;

    top:
        -120px;

    border-radius:
        50%;

    background:
        radial-gradient(
            circle,
            rgba(96,165,250,0.16),
            transparent 70%
        );

    animation:
        pulseGlow 4s ease-in-out infinite;

}}


.result-label {{

    color:
        var(--muted);

    font-size:
        10px;

    font-weight:
        800;

    letter-spacing:
        2.5px;

    animation:
        fadeInUp 0.5s 0.2s both;

}}


.result-probability {{

    margin:
        12px 0;

    font-size:
        58px;

    font-weight:
        900;

    background:

        linear-gradient(
            90deg,
            #60A5FA,
            #818CF8,
            #A78BFA
        );

    background-size:
        200% auto;

    -webkit-background-clip:
        text;

    -webkit-text-fill-color:
        transparent;

    animation:
        probabilityGlow 3s linear infinite,
        fadeInScale 0.7s 0.25s both;

}}


.probability-caption {{

    color:
        #64748B;

    font-size:
        11px;

    margin-top:
        -5px;

    animation:
        fadeInUp 0.5s 0.35s both;

}}


.result-status {{

    display:
        inline-block;

    margin-top:
        18px;

    padding:
        10px 22px;

    border-radius:
        50px;

    background:
        rgba(59,130,246,0.12);

    border:
        1px solid
        rgba(96,165,250,0.22);

    color:
        #F8FAFC;

    font-size:
        12px;

    font-weight:
        900;

    letter-spacing:
        1px;

    animation:
        statusPop 0.6s 0.45s both;

}}


.result-main {{

    margin-top:
        22px;

    color:
        #F8FAFC;

    font-size:
        20px;

    font-weight:
        800;

    animation:
        fadeInUp 0.5s 0.55s both;

}}


.result-message {{

    margin-top:
        10px;

    color:
        var(--soft);

    font-size:
        13px;

    animation:
        fadeInUp 0.5s 0.65s both;

}}


/* ============================================================
   RESULT METRICS
============================================================ */

.result-metrics {{

    display:
        grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap:
        15px;

    max-width:
        800px;

    margin:
        35px auto 0;

}}


.result-metric {{

    padding:
        20px;

    border-radius:
        15px;

    background:
        rgba(255,255,255,0.035);

    border:
        1px solid
        rgba(255,255,255,0.07);

    transition:
        all 0.3s ease;

    animation:
        metricEntrance 0.6s
        cubic-bezier(.2,.8,.2,1)
        both;

}}


.result-metric:nth-child(1) {{
    animation-delay: 0.65s;
}}

.result-metric:nth-child(2) {{
    animation-delay: 0.75s;
}}

.result-metric:nth-child(3) {{
    animation-delay: 0.85s;
}}


.result-metric:hover {{

    transform:
        translateY(-7px);

    border-color:
        rgba(96,165,250,0.30);

    background:
        rgba(59,130,246,0.07);

    box-shadow:
        0 12px 30px
        rgba(59,130,246,0.10);

}}


.metric-value {{

    color:
        #F8FAFC;

    font-size:
        18px;

    font-weight:
        850;

}}


.metric-label {{

    margin-top:
        7px;

    color:
        #64748B;

    font-size:
        9px;

    font-weight:
        800;

    letter-spacing:
        1.5px;

}}


.prediction-note {{

    margin-top:
        30px;

    color:
        #64748B;

    font-size:
        11px;

    animation:
        fadeInUp 0.5s 1s both;

}}


/* ============================================================
   FOOTER
============================================================ */

.footer {{

    margin-top:
        90px;

    padding:
        30px 0;

    border-top:
        1px solid
        rgba(148,163,184,0.08);

    text-align:
        center;

}}


.footer-title {{

    color:
        var(--text);

    font-size:
        17px;

    font-weight:
        800;

}}


.footer-text {{

    margin-top:
        6px;

    color:
        #475569;

    font-size:
        11px;

}}


/* ============================================================
   ANIMATIONS
============================================================ */

@keyframes heroEntrance {{

    from {{
        opacity: 0;
        transform:
            translateY(30px)
            scale(0.97);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0)
            scale(1);
    }}

}}


@keyframes fadeInUp {{

    from {{
        opacity: 0;
        transform:
            translateY(20px);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0);
    }}

}}


@keyframes fadeInScale {{

    from {{
        opacity: 0;
        transform:
            scale(0.75);
    }}

    to {{
        opacity: 1;
        transform:
            scale(1);
    }}

}}


@keyframes fadeInLeft {{

    from {{
        opacity: 0;
        transform:
            translateX(-20px);
    }}

    to {{
        opacity: 1;
        transform:
            translateX(0);
    }}

}}


@keyframes buttonEntrance {{

    from {{
        opacity: 0;
        transform:
            translateY(15px);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0);
    }}

}}


@keyframes loadingAppear {{

    from {{
        opacity: 0;
        transform:
            scale(0.95);
    }}

    to {{
        opacity: 1;
        transform:
            scale(1);
    }}

}}


@keyframes resultEntrance {{

    0% {{
        opacity: 0;
        transform:
            translateY(40px)
            scale(0.92);
    }}

    60% {{
        opacity: 1;
        transform:
            translateY(-5px)
            scale(1.01);
    }}

    100% {{
        opacity: 1;
        transform:
            translateY(0)
            scale(1);
    }}

}}


@keyframes statusPop {{

    from {{
        opacity: 0;
        transform:
            scale(0.7);
    }}

    to {{
        opacity: 1;
        transform:
            scale(1);
    }}

}}


@keyframes metricEntrance {{

    from {{
        opacity: 0;
        transform:
            translateY(25px);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0);
    }}

}}


@keyframes spin {{

    to {{
        transform:
            rotate(360deg);
    }}

}}


@keyframes dotPulse {{

    0%, 100% {{
        opacity: 1;
        transform:
            scale(1);
    }}

    50% {{
        opacity: 0.45;
        transform:
            scale(1.5);
    }}

}}


@keyframes pulseGlow {{

    0%, 100% {{
        opacity: 0.5;
        transform:
            scale(1);
    }}

    50% {{
        opacity: 0.9;
        transform:
            scale(1.12);
    }}

}}


@keyframes floatingGlow {{

    0%, 100% {{
        transform:
            translate(0, 0);
    }}

    50% {{
        transform:
            translate(-30px, -20px);
    }}

}}


@keyframes iconFloat {{

    0%, 100% {{
        transform:
            translateY(0);
    }}

    50% {{
        transform:
            translateY(-4px);
    }}

}}


@keyframes stepPulse {{

    0%, 100% {{
        opacity: 1;
    }}

    50% {{
        opacity: 0.6;
    }}

}}


@keyframes gradientMove {{

    0% {{
        background-position:
            0% center;
    }}

    100% {{
        background-position:
            200% center;
    }}

}}


@keyframes probabilityGlow {{

    0% {{
        background-position:
            0% center;
    }}

    100% {{
        background-position:
            200% center;
    }}

}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 800px) {{

    .prediction-container {{
        padding: 15px;
    }}

    .prediction-hero {{
        padding: 40px 25px;
    }}

    .prediction-hero h1 {{
        font-size: 43px;
    }}

    .form-section {{
        padding: 22px;
    }}

    .result-metrics {{
        grid-template-columns:
            1fr;
    }}

}}

</style>

""")


# ============================================================
# SIDEBAR BRAND
# ============================================================

st.html("""

<div class="sidebar-brand">

    <div class="sidebar-brand-title">
        Hotel Booking <span>AI</span>
    </div>

    <div class="sidebar-brand-subtitle">
        MACHINE LEARNING PLATFORM
    </div>

</div>

""")


# ============================================================
# HERO
# ============================================================

st.html("""

<div class="prediction-container">

    <section class="prediction-hero">

        <div class="prediction-content">

            <div class="prediction-badge">

                <span class="prediction-dot"></span>

                AI PREDICTION ENGINE

            </div>

            <h1>
                Cancellation <span>Prediction</span>
            </h1>

            <p class="prediction-description">

                Enter the reservation details below and let the
                XGBoost machine learning model estimate the
                probability that this hotel booking will be cancelled.

            </p>

        </div>

    </section>

</div>

""")


# ============================================================
# BOOKING INFORMATION
# ============================================================

st.html("""

<div class="prediction-container">

<section class="form-section">

    <div class="form-header">

        <div class="form-icon">
            📅
        </div>

        <div>

            <div class="form-title">
                Booking Information
            </div>

            <div class="form-subtitle">
                Basic reservation details
            </div>

        </div>

    </div>

""")


col1, col2, col3 = st.columns(3)


with col1:

    hotel = st.selectbox(
        "Hotel",
        ["Resort Hotel", "City Hotel"]
    )

    lead_time = st.number_input(
        "Lead Time (days)",
        min_value=0,
        max_value=1000,
        value=100
    )

    arrival_year = st.selectbox(
        "Arrival Year",
        [2015, 2016, 2017],
        index=1
    )

    arrival_month = st.selectbox(
        "Arrival Month",
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ],
        index=6
    )


with col2:

    arrival_day = st.number_input(
        "Arrival Day of Month",
        min_value=1,
        max_value=31,
        value=15
    )

    weekend_nights = st.number_input(
        "Weekend Nights",
        min_value=0,
        max_value=20,
        value=1
    )

    week_nights = st.number_input(
        "Week Nights",
        min_value=0,
        max_value=50,
        value=3
    )

    adults = st.number_input(
        "Adults",
        min_value=0,
        max_value=20,
        value=2
    )


with col3:

    children = st.number_input(
        "Children",
        min_value=0.0,
        max_value=20.0,
        value=0.0,
        step=1.0
    )

    babies = st.number_input(
        "Babies",
        min_value=0,
        max_value=10,
        value=0
    )

    meal = st.selectbox(
        "Meal",
        ["BB", "HB", "FB", "SC", "Undefined"]
    )

    market_segment = st.selectbox(
        "Market Segment",
        [
            "Online TA",
            "Offline TA/TO",
            "Direct",
            "Groups",
            "Corporate",
            "Complementary",
            "Aviation",
            "Undefined"
        ]
    )


st.html("""

</section>

</div>

""")


# ============================================================
# CUSTOMER & RESERVATION
# ============================================================

st.html("""

<div class="prediction-container">

<section class="form-section">

    <div class="form-header">

        <div class="form-icon">
            👤
        </div>

        <div>

            <div class="form-title">
                Customer & Reservation Details
            </div>

            <div class="form-subtitle">
                Customer behavior and reservation attributes
            </div>

        </div>

    </div>

""")


col1, col2, col3 = st.columns(3)


with col1:

    distribution_channel = st.selectbox(
        "Distribution Channel",
        [
            "TA/TO",
            "Direct",
            "Corporate",
            "GDS"
        ]
    )

    repeated_guest = st.selectbox(
        "Repeated Guest",
        ["No", "Yes"]
    )

    previous_cancellations = st.number_input(
        "Previous Cancellations",
        min_value=0,
        max_value=100,
        value=0
    )

    previous_bookings_not_canceled = st.number_input(
        "Previous Bookings Not Canceled",
        min_value=0,
        max_value=100,
        value=0
    )


with col2:

    booking_changes = st.number_input(
        "Booking Changes",
        min_value=0,
        max_value=50,
        value=0
    )

    deposit_type = st.selectbox(
        "Deposit Type",
        [
            "No Deposit",
            "Non Refund",
            "Refundable"
        ]
    )

    customer_type = st.selectbox(
        "Customer Type",
        [
            "Transient",
            "Transient-Party",
            "Contract",
            "Group"
        ]
    )

    reserved_room_type = st.selectbox(
        "Reserved Room Type",
        list("ABCDEFGHLP")
    )


with col3:

    assigned_room_type = st.selectbox(
        "Assigned Room Type",
        list("ABCDEFGHLP")
    )

    adr = st.number_input(
        "ADR",
        min_value=-10.0,
        max_value=1000.0,
        value=100.0,
        step=0.01
    )

    waiting_list = st.number_input(
        "Waiting List (days)",
        min_value=0,
        max_value=400,
        value=0
    )

    required_car_parking_spaces = st.number_input(
        "Required Car Parking Spaces",
        min_value=0,
        max_value=10,
        value=0
    )


st.html("""

</section>

</div>

""")


# ============================================================
# ADDITIONAL FEATURES
# ============================================================

st.html("""

<div class="prediction-container">

<section class="form-section">

    <div class="form-header">

        <div class="form-icon">
            ⚙️
        </div>

        <div>

            <div class="form-title">
                Additional Features
            </div>

            <div class="form-subtitle">
                Additional attributes required by the prediction model
            </div>

        </div>

    </div>

""")


col1, col2, col3 = st.columns(3)


with col1:

    country = st.text_input(
        "Country Code",
        value="PRT",
        max_chars=3
    ).upper()


with col2:

    agent = st.number_input(
        "Agent ID",
        min_value=0,
        max_value=600,
        value=9
    )


with col3:

    total_special_requests = st.number_input(
        "Total Special Requests",
        min_value=0,
        max_value=10,
        value=0
    )


company = st.number_input(
    "Company ID",
    min_value=0,
    max_value=600,
    value=0
)


st.html("""

</section>

</div>

""")


# ============================================================
# MONTH CONVERSION
# ============================================================

month_number = {

    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12

}


# ============================================================
# PREDICT BUTTON
# ============================================================

st.html("""

<div class="prediction-container">

<div class="predict-button-container">

""")


predict_button = st.button(
    "🔮  Predict Cancellation Risk",
    use_container_width=True
)


st.html("""

</div>

</div>

""")


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    if not model_loaded:

        st.error(
            "The machine learning model could not be loaded."
        )

        st.stop()


    # ========================================================
    # DATE VALIDATION
    # ========================================================

    try:

        arrival_date = datetime(
            int(arrival_year),
            month_number[arrival_month],
            int(arrival_day)
        )

    except ValueError:

        st.error(
            "Invalid arrival date. Please check the month and day."
        )

        st.stop()


    arrival_date_week_number = int(
        arrival_date.isocalendar().week
    )


    # ========================================================
    # LOADING ANIMATION
    # ========================================================

    loading_placeholder = st.empty()


    loading_placeholder.html("""

    <div class="prediction-container">

        <div class="loading-box">

            <div class="loader"></div>

            <div class="loading-text">
                AI is analyzing your booking...
            </div>

            <div class="loading-steps">

                <div class="loading-step active">
                    <span>✓</span>
                    Preparing booking data
                </div>

                <div class="loading-step">
                    <span>◌</span>
                    Running XGBoost model
                </div>

                <div class="loading-step">
                    <span>◌</span>
                    Calculating cancellation risk
                </div>

                <div class="loading-step">
                    <span>◌</span>
                    Generating prediction
                </div>

            </div>

        </div>

    </div>

    """)


    # ========================================================
    # INPUT DATA
    # ========================================================

    input_data = pd.DataFrame([{

        "hotel":
            hotel,

        "lead_time":
            lead_time,

        "arrival_date_year":
            arrival_year,

        "arrival_date_month":
            arrival_month,

        "arrival_date_week_number":
            arrival_date_week_number,

        "arrival_date_day_of_month":
            arrival_day,

        "stays_in_weekend_nights":
            weekend_nights,

        "stays_in_week_nights":
            week_nights,

        "adults":
            adults,

        "children":
            children,

        "babies":
            babies,

        "meal":
            meal,

        "market_segment":
            market_segment,

        "distribution_channel":
            distribution_channel,

        "is_repeated_guest":
            1 if repeated_guest == "Yes" else 0,

        "previous_cancellations":
            previous_cancellations,

        "previous_bookings_not_canceled":
            previous_bookings_not_canceled,

        "reserved_room_type":
            reserved_room_type,

        "assigned_room_type":
            assigned_room_type,

        "booking_changes":
            booking_changes,

        "deposit_type":
            deposit_type,

        "agent":
            agent,

        "company":
            company,

        "days_in_waiting_list":
            waiting_list,

        "customer_type":
            customer_type,

        "adr":
            adr,

        "required_car_parking_spaces":
            required_car_parking_spaces,

        "total_of_special_requests":
            total_special_requests,

        "country":
            country

    }])


    # ========================================================
    # RUN MODEL
    # ========================================================

    time.sleep(0.6)


    loading_placeholder.html("""

    <div class="prediction-container">

        <div class="loading-box">

            <div class="loader"></div>

            <div class="loading-text">
                Running XGBoost model...
            </div>

            <div class="loading-steps">

                <div class="loading-step completed">
                    <span>✓</span>
                    Booking data prepared
                </div>

                <div class="loading-step active">
                    <span>✓</span>
                    Running XGBoost model
                </div>

                <div class="loading-step">
                    <span>◌</span>
                    Calculating cancellation risk
                </div>

                <div class="loading-step">
                    <span>◌</span>
                    Generating prediction
                </div>

            </div>

        </div>

    </div>

    """)


    time.sleep(0.6)


    try:

        prediction = model.predict(
            input_data
        )[0]

        probability = model.predict_proba(
            input_data
        )[0][1]

    except Exception as e:

        loading_placeholder.empty()

        st.error("Prediction failed.")

        st.code(str(e))

        st.stop()


    # ========================================================
    # FINAL LOADING STEP
    # ========================================================

    loading_placeholder.html("""

    <div class="prediction-container">

        <div class="loading-box">

            <div class="loader"></div>

            <div class="loading-text">
                Finalizing AI prediction...
            </div>

            <div class="loading-steps">

                <div class="loading-step completed">
                    <span>✓</span>
                    Booking data prepared
                </div>

                <div class="loading-step completed">
                    <span>✓</span>
                    XGBoost model executed
                </div>

                <div class="loading-step completed">
                    <span>✓</span>
                    Cancellation risk calculated
                </div>

                <div class="loading-step active">
                    <span>✓</span>
                    Generating final result
                </div>

            </div>

        </div>

    </div>

    """)


    time.sleep(0.5)

    # IMPORTANT:
    # Remove loading completely before showing result

    loading_placeholder.empty()


    # ========================================================
    # RESULT
    # ========================================================

    probability_percent = probability * 100


    if probability_percent < 30:

        risk_level = "LOW RISK"

        risk_icon = "🟢"

        message = (
            "The reservation is unlikely to be cancelled."
        )

    elif probability_percent < 60:

        risk_level = "MEDIUM RISK"

        risk_icon = "🟡"

        message = (
            "The reservation has a moderate cancellation risk."
        )

    else:

        risk_level = "HIGH RISK"

        risk_icon = "🔴"

        message = (
            "The reservation has a high probability of cancellation."
        )


    if prediction == 1:

        result_text = (
            "Booking is likely to be cancelled."
        )

        prediction_label = "Cancelled"

    else:

        result_text = (
            "Booking is likely to be confirmed."
        )

        prediction_label = "Confirmed"


    # ========================================================
    # RESULT UI
    # ========================================================

    st.html(f"""

    <div class="prediction-container">

        <div class="result-wrapper">

            <div class="result-label">
                AI PREDICTION COMPLETE
            </div>

            <div class="result-probability">
                {probability_percent:.2f}%
            </div>

            <div class="probability-caption">
                Cancellation Probability
            </div>

            <div class="result-status">
                {risk_icon} {risk_level}
            </div>

            <div class="result-main">
                {result_text}
            </div>

            <div class="result-message">
                {message}
            </div>

            <div class="result-metrics">

                <div class="result-metric">

                    <div class="metric-value">
                        {prediction_label}
                    </div>

                    <div class="metric-label">
                        MODEL PREDICTION
                    </div>

                </div>


                <div class="result-metric">

                    <div class="metric-value">
                        {probability_percent:.1f}%
                    </div>

                    <div class="metric-label">
                        CANCELLATION RISK
                    </div>

                </div>


                <div class="result-metric">

                    <div class="metric-value">
                        XGBoost
                    </div>

                    <div class="metric-label">
                        ML ENGINE
                    </div>

                </div>

            </div>


            <div class="prediction-note">

                🤖 Prediction generated using the trained
                Hotel Booking XGBoost pipeline.

            </div>

        </div>

    </div>

    """)


# ============================================================
# FOOTER
# ============================================================

st.html("""

<div class="prediction-container">

    <footer class="footer">

        <div class="footer-title">
            Hotel Booking AI
        </div>

        <div class="footer-text">
            Machine Learning Prediction Platform
        </div>

    </footer>

</div>

""")