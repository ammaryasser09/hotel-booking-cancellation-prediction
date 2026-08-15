import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="About | Hotel Booking AI",
    page_icon="🏨",
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
            circle at 8% 5%,
            rgba(59,130,246,0.12),
            transparent 24%
        ),

        radial-gradient(
            circle at 92% 20%,
            rgba(139,92,246,0.10),
            transparent 25%
        ),

        radial-gradient(
            circle at 50% 90%,
            rgba(59,130,246,0.05),
            transparent 30%
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
        fadeDown 0.7s ease both;

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

[data-testid="stSidebarNav"] a {{

    display: flex;

    align-items: center;

    border-radius: 12px;

    padding: 12px 14px;

    margin: 6px 0;

    color: #94A3B8 !important;

    background: transparent;

    border: 1px solid transparent;

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

.about-container {{

    max-width: 1350px;

    margin: auto;

    padding:
        20px 40px 60px;

}}


/* ============================================================
   HERO
============================================================ */

.about-hero {{

    position: relative;

    overflow: hidden;

    padding:
        65px 70px;

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
        heroEntrance 0.8s ease-out both;

}}


/* HERO GLOW */

.about-hero::before {{

    content: "";

    position: absolute;

    width: 500px;

    height: 500px;

    right: -180px;

    top: -240px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle,
            rgba(59,130,246,0.25),
            transparent 68%
        );

    filter: blur(5px);

    animation:
        floatingGlow 6s ease-in-out infinite;

}}


.about-hero::after {{

    content: "";

    position: absolute;

    width: 350px;

    height: 350px;

    left: -180px;

    bottom: -230px;

    border-radius: 50%;

    background:

        radial-gradient(
            circle,
            rgba(139,92,246,0.18),
            transparent 68%
        );

    filter: blur(10px);

    animation:
        floatingGlow 8s ease-in-out infinite reverse;

}}


.about-hero-content {{

    position: relative;

    z-index: 2;

}}


/* ============================================================
   BADGE
============================================================ */

.about-badge {{

    display: inline-flex;

    align-items: center;

    gap: 9px;

    padding:
        8px 15px;

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

}}


.about-dot {{

    width: 7px;

    height: 7px;

    border-radius: 50%;

    background:
        #60A5FA;

    box-shadow:
        0 0 14px
        rgba(96,165,250,0.9);

    animation:
        pulse 2s infinite;

}}


/* ============================================================
   HERO TITLE
============================================================ */

.about-hero h1 {{

    margin:
        24px 0 16px;

    font-size:
        clamp(42px, 5vw, 66px);

    line-height:
        1.03;

    letter-spacing:
        -3px;

    font-weight:
        900;

    color:
        var(--text);

}}


.about-hero h1 span {{

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

}}


.about-description {{

    max-width:
        850px;

    color:
        var(--muted);

    font-size:
        16px;

    line-height:
        1.8;

}}


/* ============================================================
   SECTION HEADER
============================================================ */

.section-header {{

    margin:
        45px 0 22px;

    animation:
        fadeUp 0.8s ease both;

}}

.section-label {{

    color:
        var(--primary-light);

    font-size:
        10px;

    font-weight:
        900;

    letter-spacing:
        2.5px;

}}

.section-title {{

    margin-top:
        8px;

    color:
        var(--text);

    font-size:
        30px;

    font-weight:
        900;

    letter-spacing:
        -1px;

}}

.section-description {{

    margin-top:
        7px;

    max-width:
        750px;

    color:
        var(--soft);

    font-size:
        13px;

    line-height:
        1.7;

}}


/* ============================================================
   ABOUT CARD
============================================================ */

.info-card {{

    height: 100%;

    padding:
        30px;

    border-radius:
        22px;

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

    transition:
        transform 0.35s ease,
        border-color 0.35s ease,
        box-shadow 0.35s ease;

    animation:
        fadeUp 0.8s ease both;

}}


.info-card:hover {{

    transform:
        translateY(-8px);

    border-color:
        rgba(96,165,250,0.25);

    box-shadow:
        0 25px 60px
        rgba(59,130,246,0.10);

}}


/* ============================================================
   ICON BOX
============================================================ */

.icon-box {{

    width: 58px;

    height: 58px;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 16px;

    margin-bottom: 20px;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.15),
            rgba(139,92,246,0.10)
        );

    border:
        1px solid
        rgba(96,165,250,0.18);

    font-size: 26px;

    transition:
        transform 0.3s ease;

}}

.info-card:hover .icon-box {{

    transform:
        scale(1.08)
        rotate(-3deg);

}}


.info-card-title {{

    color:
        #F8FAFC;

    font-size:
        19px;

    font-weight:
        850;

    margin-bottom:
        10px;

}}

.info-card-text {{

    color:
        #94A3B8;

    font-size:
        13px;

    line-height:
        1.8;

}}


/* ============================================================
   WORKFLOW
============================================================ */

.workflow {{

    display:
        grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:
        18px;

}}


.workflow-card {{

    position:
        relative;

    padding:
        28px 22px;

    border-radius:
        20px;

    background:
        rgba(13,27,42,0.85);

    border:
        1px solid
        var(--border);

    text-align:
        center;

    transition:
        all 0.35s ease;

    animation:
        fadeUp 0.8s ease both;

}}


.workflow-card:hover {{

    transform:
        translateY(-7px);

    border-color:
        rgba(96,165,250,0.25);

}}


.workflow-number {{

    position:
        absolute;

    top:
        12px;

    right:
        14px;

    color:
        rgba(96,165,250,0.35);

    font-size:
        11px;

    font-weight:
        900;

}}


.workflow-icon {{

    font-size:
        30px;

    margin-bottom:
        14px;

}}


.workflow-title {{

    color:
        #F8FAFC;

    font-size:
        15px;

    font-weight:
        800;

    margin-bottom:
        8px;

}}


.workflow-text {{

    color:
        #64748B;

    font-size:
        11px;

    line-height:
        1.6;

}}


/* ============================================================
   TECH STACK
============================================================ */

.tech-grid {{

    display:
        grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:
        18px;

}}


.tech-card {{

    padding:
        25px;

    border-radius:
        20px;

    background:
        linear-gradient(
            145deg,
            rgba(13,27,42,0.95),
            rgba(17,28,53,0.80)
        );

    border:
        1px solid
        var(--border);

    transition:
        all 0.35s ease;

}}


.tech-card:hover {{

    transform:
        translateY(-6px);

    border-color:
        rgba(139,92,246,0.28);

    box-shadow:
        0 20px 50px
        rgba(139,92,246,0.08);

}}


.tech-icon {{

    font-size:
        25px;

    margin-bottom:
        12px;

}}

.tech-name {{

    color:
        #F8FAFC;

    font-size:
        15px;

    font-weight:
        850;

}}

.tech-desc {{

    margin-top:
        6px;

    color:
        #64748B;

    font-size:
        11px;

    line-height:
        1.6;

}}


/* ============================================================
   BUSINESS VALUE
============================================================ */

.value-card {{

    padding:
        35px;

    border-radius:
        24px;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.10),
            rgba(139,92,246,0.08)
        );

    border:
        1px solid
        rgba(96,165,250,0.18);

    box-shadow:
        0 25px 60px
        rgba(0,0,0,0.18);

    animation:
        fadeUp 0.8s ease both;

}}


.value-item {{

    display:
        flex;

    align-items:
        flex-start;

    gap:
        14px;

    margin-bottom:
        20px;

}}


.value-icon {{

    width:
        42px;

    height:
        42px;

    flex-shrink:
        0;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        12px;

    background:
        rgba(59,130,246,0.10);

    border:
        1px solid
        rgba(96,165,250,0.15);

    font-size:
        19px;

}}


.value-title {{

    color:
        #F8FAFC;

    font-size:
        14px;

    font-weight:
        800;

}}

.value-text {{

    margin-top:
        4px;

    color:
        #64748B;

    font-size:
        11px;

    line-height:
        1.6;

}}


/* ============================================================
   TEAM
============================================================ */

.team-grid {{

    display:
        grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap:
        20px;

}}


.team-card {{

    padding:
        30px;

    border-radius:
        22px;

    background:
        rgba(13,27,42,0.90);

    border:
        1px solid
        var(--border);

    transition:
        all 0.35s ease;

}}


.team-card:hover {{

    transform:
        translateY(-6px);

    border-color:
        rgba(96,165,250,0.25);

}}


.team-avatar {{

    width:
        60px;

    height:
        60px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        50%;

    margin-bottom:
        18px;

    background:

        linear-gradient(
            135deg,
            #2563EB,
            #7C3AED
        );

    font-size:
        23px;

    box-shadow:
        0 10px 30px
        rgba(59,130,246,0.20);

}}


.team-name {{

    color:
        #F8FAFC;

    font-size:
        18px;

    font-weight:
        850;

}}

.team-role {{

    margin-top:
        5px;

    color:
        #60A5FA;

    font-size:
        11px;

    font-weight:
        800;

    letter-spacing:
        1px;

}}

.team-description {{

    margin-top:
        12px;

    color:
        #64748B;

    font-size:
        12px;

    line-height:
        1.7;

}}


/* ============================================================
   FOOTER
============================================================ */

.footer {{

    margin-top:
        80px;

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
            translateY(25px)
            scale(0.98);

    }}

    to {{

        opacity: 1;

        transform:
            translateY(0)
            scale(1);

    }}

}}


@keyframes fadeUp {{

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


@keyframes fadeDown {{

    from {{

        opacity: 0;

        transform:
            translateY(-15px);

    }}

    to {{

        opacity: 1;

        transform:
            translateY(0);

    }}

}}


@keyframes floatingGlow {{

    0%, 100% {{

        transform:
            translate(0, 0);

    }}

    50% {{

        transform:
            translate(-25px, 20px);

    }}

}}


@keyframes pulse {{

    0%, 100% {{

        transform:
            scale(1);

        opacity:
            1;

    }}

    50% {{

        transform:
            scale(1.4);

        opacity:
            0.6;

    }}

}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1000px) {{

    .workflow {{

        grid-template-columns:
            repeat(2, 1fr);

    }}

    .tech-grid {{

        grid-template-columns:
            repeat(2, 1fr);

    }}

}}

@media (max-width: 700px) {{

    .about-container {{

        padding:
            15px;

    }}

    .about-hero {{

        padding:
            40px 25px;

    }}

    .about-hero h1 {{

        font-size:
            43px;

    }}

    .workflow,
    .tech-grid,
    .team-grid {{

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

<div class="about-container">

<section class="about-hero">

    <div class="about-hero-content">

        <div class="about-badge">

            <span class="about-dot"></span>

            HOTEL BOOKING AI

        </div>


        <h1>

            Intelligent

            <span>Booking Prediction</span>

        </h1>


        <p class="about-description">

            Hotel Booking AI is a machine learning platform
            designed to analyze hotel reservation data and
            predict the probability of booking cancellation.

            The system transforms booking information into
            actionable risk insights using an XGBoost
            classification model.

        </p>

    </div>

</section>

</div>

""")


# ============================================================
# ABOUT PROJECT
# ============================================================

st.html("""

<div class="about-container">

    <div class="section-header">

        <div class="section-label">
            ABOUT THE PROJECT
        </div>

        <div class="section-title">
            Turning Booking Data Into Decisions
        </div>

        <div class="section-description">

            The platform combines data preprocessing,
            machine learning and an interactive dashboard
            to help understand the cancellation behavior
            of hotel reservations.

        </div>

    </div>


    <div class="info-card">

        <div class="icon-box">
            🏨
        </div>

        <div class="info-card-title">
            What is Hotel Booking AI?
        </div>

        <div class="info-card-text">

            Hotel Booking AI is an intelligent prediction
            system that evaluates reservation attributes
            and estimates the likelihood of cancellation.

            Instead of relying only on historical statistics,
            the system uses a trained machine learning model
            to generate a prediction for each individual booking.

        </div>

    </div>

</div>

""")


# ============================================================
# HOW IT WORKS
# ============================================================

st.html("""

<div class="about-container">

    <div class="section-header">

        <div class="section-label">
            SYSTEM WORKFLOW
        </div>

        <div class="section-title">
            How The AI Works
        </div>

        <div class="section-description">

            From raw booking information to a final
            cancellation risk prediction.

        </div>

    </div>


    <div class="workflow">


        <div class="workflow-card">

            <div class="workflow-number">
                01
            </div>

            <div class="workflow-icon">
                📋
            </div>

            <div class="workflow-title">
                Booking Data
            </div>

            <div class="workflow-text">
                Reservation details and customer
                attributes are collected.
            </div>

        </div>


        <div class="workflow-card">

            <div class="workflow-number">
                02
            </div>

            <div class="workflow-icon">
                ⚙️
            </div>

            <div class="workflow-title">
                Preprocessing
            </div>

            <div class="workflow-text">
                Data is cleaned, transformed and
                prepared for the ML model.
            </div>

        </div>


        <div class="workflow-card">

            <div class="workflow-number">
                03
            </div>

            <div class="workflow-icon">
                🧠
            </div>

            <div class="workflow-title">
                XGBoost
            </div>

            <div class="workflow-text">
                The trained classification model
                analyzes the booking.
            </div>

        </div>


        <div class="workflow-card">

            <div class="workflow-number">
                04
            </div>

            <div class="workflow-icon">
                🎯
            </div>

            <div class="workflow-title">
                Risk Prediction
            </div>

            <div class="workflow-text">
                The system returns cancellation
                probability and risk level.
            </div>

        </div>


    </div>

</div>

""")


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.html("""

<div class="about-container">

    <div class="section-header">

        <div class="section-label">
            TECHNOLOGY
        </div>

        <div class="section-title">
            Machine Learning Technology Stack
        </div>

        <div class="section-description">

            Technologies used to build the Hotel Booking
            AI prediction platform.

        </div>

    </div>


    <div class="tech-grid">


        <div class="tech-card">

            <div class="tech-icon">
                🧠
            </div>

            <div class="tech-name">
                XGBoost
            </div>

            <div class="tech-desc">
                Gradient boosting algorithm used
                for cancellation classification.
            </div>

        </div>


        <div class="tech-card">

            <div class="tech-icon">
                🐍
            </div>

            <div class="tech-name">
                Python
            </div>

            <div class="tech-desc">
                Main programming language used
                for data processing and ML.
            </div>

        </div>


        <div class="tech-card">

            <div class="tech-icon">
                📊
            </div>

            <div class="tech-name">
                Pandas
            </div>

            <div class="tech-desc">
                Used for data manipulation,
                cleaning and analysis.
            </div>

        </div>


        <div class="tech-card">

            <div class="tech-icon">
                ⚡
            </div>

            <div class="tech-name">
                Streamlit
            </div>

            <div class="tech-desc">
                Interactive web interface for
                the machine learning application.
            </div>

        </div>


    </div>

</div>

""")


# ============================================================
# BUSINESS VALUE
# ============================================================

st.html("""

<div class="about-container">

    <div class="section-header">

        <div class="section-label">
            BUSINESS VALUE
        </div>

        <div class="section-title">
            Why Cancellation Prediction Matters
        </div>

        <div class="section-description">

            Predicting cancellation risk can help hotels
            make better operational and revenue decisions.

        </div>

    </div>


    <div class="value-card">


        <div class="value-item">

            <div class="value-icon">
                🎯
            </div>

            <div>

                <div class="value-title">
                    Identify High-Risk Bookings
                </div>

                <div class="value-text">
                    Detect reservations that have a higher
                    probability of cancellation.
                </div>

            </div>

        </div>


        <div class="value-item">

            <div class="value-icon">
                💰
            </div>

            <div>

                <div class="value-title">
                    Improve Revenue Planning
                </div>

                <div class="value-text">
                    Cancellation insights can support
                    better room and revenue management.
                </div>

            </div>

        </div>


        <div class="value-item">

            <div class="value-icon">
                📈
            </div>

            <div>

                <div class="value-title">
                    Support Better Decisions
                </div>

                <div class="value-text">
                    Transform historical booking patterns
                    into actionable business insights.
                </div>

            </div>

        </div>


        <div class="value-item">

            <div class="value-icon">
                🤖
            </div>

            <div>

                <div class="value-title">
                    Automated AI Prediction
                </div>

                <div class="value-text">
                    Generate a prediction automatically
                    using the trained XGBoost pipeline.
                </div>

            </div>

        </div>


    </div>

</div>

""")


# ============================================================
# PROJECT TEAM
# ============================================================

st.html("""

<div class="about-container">

    <div class="section-header">

        <div class="section-label">
            PROJECT TEAM
        </div>

        <div class="section-title">
            Built With AI & Machine Learning
        </div>

        <div class="section-description">

            Hotel Booking AI combines machine learning
            engineering with an interactive user experience.

        </div>

    </div>


    <div class="team-grid">


        <div class="team-card">

            <div class="team-avatar">
                👨‍💻
            </div>

            <div class="team-name">
                Ammar Yasser Zaki
            </div>

            <div class="team-role">
                AI / MACHINE LEARNING
            </div>

            <div class="team-description">
                Responsible for data analysis, preprocessing,
                machine learning model development,
                evaluation and deployment of the prediction pipeline.
            </div>

        </div>


        <div class="team-card">

            <div class="team-avatar">
                👨‍🏫
            </div>

            <div class="team-name">
                Eng. Moheb Allam
            </div>

            <div class="team-role">
                PROJECT SUPERVISOR
            </div>

            <div class="team-description">
                Project supervision, technical guidance
                and support throughout the development
                of the Hotel Booking AI system.
            </div>

        </div>


    </div>

</div>

""")


# ============================================================
# FOOTER
# ============================================================

st.html("""

<div class="about-container">

    <footer class="footer">

        <div class="footer-title">
            Hotel Booking AI
        </div>

        <div class="footer-text">
            Intelligent Hotel Booking Cancellation Prediction
            • Machine Learning Platform
        </div>

    </footer>

</div>

""")