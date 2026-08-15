import streamlit as st



# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Hotel Booking AI",
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
   STREAMLIT UI
============================================================ */

#MainMenu {{
    visibility: hidden;
}}

header {{
    visibility: visible !important;
    background: transparent !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

[data-testid="stToolbar"] {{
    visibility: visible !important;
}}

footer {{
    visibility: hidden;
}}


/* ============================================================
   MAIN APP
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
   NAVIGATION / SIDEBAR
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
   NAVIGATION HEADER
============================================================ */

[data-testid="stSidebarNav"]::before {{

    content:
        "HOTEL BOOKING AI";

    display:
        block;

    color:
        #F8FAFC;

    font-size:
        18px;

    font-weight:
        900;

    letter-spacing:
        -0.5px;

    padding:
        10px 14px 18px;

    border-bottom:
        1px solid
        rgba(148,163,184,0.08);

    margin-bottom:
        12px;

}}


/* ============================================================
   NAVIGATION LINKS
============================================================ */

[data-testid="stSidebarNav"] {{

    padding:
        10px;

}}


[data-testid="stSidebarNav"] a {{

    position:
        relative;

    display:
        flex;

    align-items:
        center;

    border-radius:
        12px;

    padding:
        12px 14px;

    margin:
        6px 0;

    color:
        #94A3B8 !important;

    background:
        transparent;

    border:
        1px solid
        transparent;

    transition:
        all 0.3s ease;

}}


/* ============================================================
   NAVIGATION HOVER
============================================================ */

[data-testid="stSidebarNav"] a:hover {{

    color:
        #F8FAFC !important;

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

    box-shadow:
        0 8px 25px
        rgba(59,130,246,0.10);

}}


/* ============================================================
   ACTIVE NAVIGATION
============================================================ */

[data-testid="stSidebarNav"] a[aria-current="page"] {{

    color:
        #FFFFFF !important;

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


/* ACTIVE INDICATOR */

[data-testid="stSidebarNav"] a[aria-current="page"]::before {{

    content:
        "";

    position:
        absolute;

    left:
        4px;

    top:
        50%;

    transform:
        translateY(-50%);

    width:
        3px;

    height:
        24px;

    border-radius:
        10px;

    background:

        linear-gradient(
            180deg,
            #60A5FA,
            #8B5CF6
        );

    box-shadow:
        0 0 15px
        rgba(96,165,250,0.70);

}}


/* ============================================================
   SIDEBAR TEXT
============================================================ */

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {{

    color:
        #CBD5E1;

}}


/* ============================================================
   SIDEBAR CUSTOM BRAND
============================================================ */

.sidebar-brand {{

    padding:
        20px;

    margin:
        5px 5px 20px;

    border-radius:
        18px;

    background:

        linear-gradient(
            135deg,
            rgba(59,130,246,0.10),
            rgba(139,92,246,0.08)
        );

    border:
        1px solid
        rgba(96,165,250,0.15);

}}


.sidebar-brand-title {{

    font-size:
        18px;

    font-weight:
        900;

    color:
        #F8FAFC;

}}


.sidebar-brand-title span {{

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


.sidebar-brand-subtitle {{

    margin-top:
        5px;

    font-size:
        10px;

    color:
        #64748B;

    letter-spacing:
        1px;

}}


/* ============================================================
   MAIN CONTAINER
============================================================ */

.home-container {{

    max-width:
        1350px;

    margin:
        auto;

    padding:
        25px 40px 80px;

}}


/* ============================================================
   HERO
============================================================ */

.hero {{

    position:
        relative;

    min-height:
        620px;

    display:
        flex;

    align-items:
        center;

    overflow:
        hidden;

    padding:
        80px;

    border-radius:
        32px;

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
        heroEntrance 1s ease-out both;

}}


/* ============================================================
   HERO GLOW
============================================================ */

.hero-glow-one {{

    position:
        absolute;

    width:
        450px;

    height:
        450px;

    right:
        -140px;

    top:
        -150px;

    border-radius:
        50%;

    background:

        radial-gradient(
            circle,
            rgba(59,130,246,0.28),
            transparent 68%
        );

    filter:
        blur(10px);

    animation:
        floatingGlow 7s ease-in-out infinite;

}}


.hero-glow-two {{

    position:
        absolute;

    width:
        350px;

    height:
        350px;

    left:
        -180px;

    bottom:
        -180px;

    border-radius:
        50%;

    background:

        radial-gradient(
            circle,
            rgba(139,92,246,0.20),
            transparent 70%
        );

    filter:
        blur(15px);

    animation:
        floatingGlowReverse 9s ease-in-out infinite;

}}


/* ============================================================
   HERO CONTENT
============================================================ */

.hero-content {{

    position:
        relative;

    z-index:
        2;

    max-width:
        800px;

    animation:
        contentEntrance 1.2s ease-out both;

    animation-delay:
        0.15s;

}}


/* ============================================================
   BADGE
============================================================ */

.hero-badge {{

    display:
        inline-flex;

    align-items:
        center;

    gap:
        9px;

    padding:
        8px 15px;

    border-radius:
        50px;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.20);

    color:
        var(--primary-light);

    font-size:
        10px;

    font-weight:
        800;

    letter-spacing:
        2px;

    animation:
        badgeEntrance 1s ease-out both;

    animation-delay:
        0.5s;

}}


.badge-dot {{

    width:
        7px;

    height:
        7px;

    border-radius:
        50%;

    background:
        var(--primary-light);

    box-shadow:
        0 0 12px
        rgba(96,165,250,0.8);

    animation:
        pulse 2s infinite;

}}


/* ============================================================
   HERO TITLE
============================================================ */

.hero h1 {{

    margin:
        25px 0 18px;

    font-size:
        clamp(48px, 6vw, 76px);

    line-height:
        1.02;

    letter-spacing:
        -3px;

    font-weight:
        900;

    color:
        var(--text);

    animation:
        titleEntrance 1s ease-out both;

    animation-delay:
        0.35s;

}}


.hero h1 span {{

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

    background-size:
        200% auto;

    animation:
        gradientMove 4s linear infinite;

}}


/* ============================================================
   HERO DESCRIPTION
============================================================ */

.hero-description {{

    max-width:
        720px;

    color:
        var(--muted);

    font-size:
        17px;

    line-height:
        1.8;

    animation:
        fadeUp 1s ease-out both;

    animation-delay:
        0.55s;

}}


/* ============================================================
   TAGS
============================================================ */

.hero-tags {{

    display:
        flex;

    flex-wrap:
        wrap;

    gap:
        10px;

    margin-top:
        30px;

    animation:
        fadeUp 1s ease-out both;

    animation-delay:
        0.7s;

}}


.hero-tag {{

    padding:
        8px 14px;

    border-radius:
        9px;

    background:
        rgba(255,255,255,0.035);

    border:
        1px solid
        rgba(255,255,255,0.08);

    color:
        #CBD5E1;

    font-size:
        12px;

    transition:
        all 0.3s ease;

}}


.hero-tag:hover {{

    transform:
        translateY(-4px);

    background:
        rgba(59,130,246,0.10);

    border-color:
        rgba(96,165,250,0.35);

    color:
        white;

    box-shadow:
        0 8px 20px
        rgba(59,130,246,0.15);

}}


/* ============================================================
   SECTION
============================================================ */

.section {{

    margin-top:
        100px;

    margin-bottom:
        32px;

}}


.section-label {{

    color:
        var(--primary-light);

    font-size:
        10px;

    font-weight:
        800;

    letter-spacing:
        2.5px;

}}


.section-title {{

    margin:
        10px 0;

    font-size:
        38px;

    line-height:
        1.2;

    font-weight:
        850;

    letter-spacing:
        -1px;

    color:
        var(--text);

}}


.section-title span {{

    color:
        var(--primary-light);

}}


.section-description {{

    max-width:
        760px;

    color:
        var(--soft);

    font-size:
        15px;

    line-height:
        1.8;

}}


/* ============================================================
   STATISTICS
============================================================ */

.stats {{

    display:
        grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:
        18px;

}}


.stat-card {{

    position:
        relative;

    overflow:
        hidden;

    padding:
        28px;

    min-height:
        155px;

    border-radius:
        18px;

    background:
        rgba(13,27,42,0.75);

    border:
        1px solid
        var(--border);

    transition:
        transform 0.35s ease,
        border-color 0.35s ease,
        box-shadow 0.35s ease;

}}


.stat-card::before {{

    content:
        "";

    position:
        absolute;

    top:
        0;

    left:
        -100%;

    width:
        100%;

    height:
        1px;

    background:

        linear-gradient(
            90deg,
            transparent,
            #60A5FA,
            transparent
        );

    transition:
        left 0.6s ease;

}}


.stat-card:hover::before {{

    left:
        100%;

}}


.stat-card:hover {{

    transform:
        translateY(-8px);

    border-color:
        rgba(96,165,250,0.30);

    box-shadow:
        0 18px 40px
        rgba(0,0,0,0.25);

}}


.stat-value {{

    color:
        var(--primary-light);

    font-size:
        32px;

    font-weight:
        900;

}}


.stat-title {{

    margin-top:
        8px;

    color:
        var(--text);

    font-size:
        14px;

    font-weight:
        700;

}}


.stat-description {{

    margin-top:
        6px;

    color:
        var(--soft);

    font-size:
        11px;

}}


/* ============================================================
   FEATURES
============================================================ */

.features {{

    display:
        grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap:
        20px;

}}


.feature-card {{

    position:
        relative;

    padding:
        30px;

    min-height:
        285px;

    border-radius:
        20px;

    background:

        linear-gradient(
            145deg,
            rgba(13,27,42,0.90),
            rgba(10,22,38,0.65)
        );

    border:
        1px solid
        var(--border);

    transition:
        transform 0.35s ease,
        border-color 0.35s ease,
        box-shadow 0.35s ease;

}}


.feature-card:hover {{

    transform:
        translateY(-10px);

    border-color:
        rgba(96,165,250,0.30);

    box-shadow:
        0 20px 45px
        rgba(0,0,0,0.25);

}}


.feature-number {{

    color:
        var(--primary);

    font-size:
        11px;

    font-weight:
        900;

    letter-spacing:
        1px;

}}


.feature-icon {{

    width:
        55px;

    height:
        55px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    margin:
        20px 0;

    border-radius:
        14px;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.12);

    font-size:
        23px;

    transition:
        transform 0.3s ease;

}}


.feature-card:hover .feature-icon {{

    transform:
        scale(1.1)
        rotate(-5deg);

}}


.feature-card h3 {{

    margin:
        0 0 10px;

    color:
        var(--text);

    font-size:
        19px;

}}


.feature-card p {{

    color:
        var(--soft);

    font-size:
        13px;

    line-height:
        1.8;

}}


/* ============================================================
   MODEL SECTION
============================================================ */

.model-section {{

    display:
        grid;

    grid-template-columns:
        1.7fr 1fr;

    gap:
        30px;

    padding:
        50px;

    margin-top:
        100px;

    border-radius:
        25px;

    background:

        linear-gradient(
            135deg,
            #0D1B2A,
            #111C35
        );

    border:
        1px solid
        rgba(96,165,250,0.12);

}}


.model-label {{

    color:
        var(--primary-light);

    font-size:
        10px;

    font-weight:
        800;

    letter-spacing:
        2px;

}}


.model-title {{

    margin-top:
        12px;

    color:
        var(--text);

    font-size:
        38px;

    font-weight:
        900;

}}


.model-title span {{

    color:
        var(--primary-light);

}}


.model-description {{

    max-width:
        680px;

    color:
        var(--soft);

    font-size:
        14px;

    line-height:
        1.8;

}}


.model-features {{

    display:
        grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap:
        10px;

    margin-top:
        25px;

}}


.model-feature {{

    padding:
        13px;

    border-radius:
        10px;

    background:
        rgba(255,255,255,0.03);

    border:
        1px solid
        rgba(255,255,255,0.06);

    color:
        #CBD5E1;

    font-size:
        12px;

    transition:
        all 0.3s ease;

}}


.model-feature:hover {{

    background:
        rgba(59,130,246,0.08);

    transform:
        translateX(4px);

}}


/* ============================================================
   TARGET
============================================================ */

.model-target {{

    padding:
        28px;

    border-radius:
        18px;

    background:
        rgba(255,255,255,0.035);

    border:
        1px solid
        rgba(255,255,255,0.08);

    animation:
        floatingCard 5s ease-in-out infinite;

}}


.target-label {{

    color:
        var(--soft);

    font-size:
        9px;

    font-weight:
        800;

    letter-spacing:
        2px;

}}


.target-name {{

    margin:
        15px 0 25px;

    color:
        white;

    font-size:
        26px;

    font-weight:
        900;

}}


.target-row {{

    display:
        flex;

    align-items:
        center;

    gap:
        12px;

    margin-top:
        14px;

    color:
        #CBD5E1;

    font-size:
        12px;

}}


.target-number {{

    width:
        30px;

    height:
        30px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    border-radius:
        8px;

    background:

        linear-gradient(
            135deg,
            #2563EB,
            #6366F1
        );

    color:
        white;

    font-weight:
        800;

}}


/* ============================================================
   WORKFLOW
============================================================ */

.workflow {{

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    gap:
        15px;

    padding:
        35px;

    border-radius:
        20px;

    background:
        rgba(13,27,42,0.70);

    border:
        1px solid
        var(--border);

}}


.workflow-step {{

    display:
        flex;

    flex-direction:
        column;

    align-items:
        center;

    text-align:
        center;

    min-width:
        115px;

}}


.workflow-number {{

    width:
        45px;

    height:
        45px;

    display:
        flex;

    align-items:
        center;

    justify-content:
        center;

    margin-bottom:
        9px;

    border-radius:
        50%;

    background:

        linear-gradient(
            135deg,
            #2563EB,
            #6366F1
        );

    color:
        white;

    font-size:
        11px;

    font-weight:
        900;

    transition:
        all 0.3s ease;

}}


.workflow-step:hover .workflow-number {{

    transform:
        scale(1.15);

    box-shadow:
        0 0 25px
        rgba(59,130,246,0.40);

}}


.workflow-name {{

    color:
        #CBD5E1;

    font-size:
        11px;

    font-weight:
        700;

}}


.workflow-line {{

    width:
        50px;

    height:
        1px;

    background:

        linear-gradient(
            90deg,
            #334155,
            #60A5FA,
            #334155
        );

}}


/* ============================================================
   FOOTER
============================================================ */

.footer {{

    margin-top:
        100px;

    padding:
        35px 0;

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
        transform: translateY(25px) scale(0.98);
    }}

    to {{
        opacity: 1;
        transform: translateY(0) scale(1);
    }}

}}


@keyframes contentEntrance {{

    from {{
        opacity: 0;
        transform: translateX(-35px);
    }}

    to {{
        opacity: 1;
        transform: translateX(0);
    }}

}}


@keyframes titleEntrance {{

    from {{
        opacity: 0;
        transform: translateY(20px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}


@keyframes fadeUp {{

    from {{
        opacity: 0;
        transform: translateY(30px);
    }}

    to {{
        opacity: 1;
        transform: translateY(0);
    }}

}}


@keyframes badgeEntrance {{

    from {{
        opacity: 0;
        transform: scale(0.85);
    }}

    to {{
        opacity: 1;
        transform: scale(1);
    }}

}}


@keyframes floatingGlow {{

    0%, 100% {{
        transform: translate(0, 0);
    }}

    50% {{
        transform: translate(-25px, 25px);
    }}

}}


@keyframes floatingGlowReverse {{

    0%, 100% {{
        transform: translate(0, 0);
    }}

    50% {{
        transform: translate(25px, -20px);
    }}

}}


@keyframes floatingCard {{

    0%, 100% {{
        transform: translateY(0);
    }}

    50% {{
        transform: translateY(-8px);
    }}

}}


@keyframes pulse {{

    0% {{
        box-shadow:
            0 0 0 0
            rgba(96,165,250,0.55);
    }}

    70% {{
        box-shadow:
            0 0 0 12px
            rgba(96,165,250,0);
    }}

    100% {{
        box-shadow:
            0 0 0 0
            rgba(96,165,250,0);
    }}

}}


@keyframes gradientMove {{

    0% {{
        background-position:
            0% 50%;
    }}

    50% {{
        background-position:
            100% 50%;
    }}

    100% {{
        background-position:
            0% 50%;
    }}

}}


/* ============================================================
   SCROLL
============================================================ */

html {{
    scroll-behavior:
        smooth;
}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 950px) {{

    .hero {{
        padding:
            55px;
    }}

    .stats {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .features {{
        grid-template-columns:
            1fr;
    }}

    .model-section {{
        grid-template-columns:
            1fr;
    }}

}}


@media (max-width: 600px) {{

    .home-container {{
        padding:
            15px;
    }}

    .hero {{
        min-height:
            500px;

        padding:
            40px 25px;
    }}

    .hero h1 {{
        font-size:
            43px;

        letter-spacing:
            -2px;
    }}

    .hero-description {{
        font-size:
            14px;
    }}

    .stats {{
        grid-template-columns:
            1fr;
    }}

    .model-section {{
        padding:
            30px;
    }}

    .model-features {{
        grid-template-columns:
            1fr;
    }}

    .workflow {{
        flex-direction:
            column;
    }}

    .workflow-line {{
        width:
            1px;

        height:
            25px;
    }}

}}


</style>


<!-- ============================================================
     SIDEBAR BRAND
============================================================ -->

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
# HOME PAGE
# ============================================================

st.html("""

<div class="home-container">


    <!-- ========================================================
         HERO
    ======================================================== -->

    <section class="hero">

        <div class="hero-glow-one"></div>

        <div class="hero-glow-two"></div>


        <div class="hero-content">

            <div class="hero-badge">

                <span class="badge-dot"></span>

                MACHINE LEARNING PROJECT

            </div>


            <h1>

                Hotel Booking
                <span>AI</span>

            </h1>


            <p class="hero-description">

                An intelligent machine learning system designed
                to analyze hotel booking behavior, discover
                meaningful patterns, and predict the probability
                of reservation cancellation.

            </p>


            <div class="hero-tags">

                <span class="hero-tag">
                    Python
                </span>

                <span class="hero-tag">
                    Machine Learning
                </span>

                <span class="hero-tag">
                    XGBoost
                </span>

                <span class="hero-tag">
                    Data Analytics
                </span>

            </div>

        </div>

    </section>


    <!-- ========================================================
         PROJECT OVERVIEW
    ======================================================== -->

    <section class="section">

        <div class="section-label">
            PROJECT OVERVIEW
        </div>

        <h2 class="section-title">

            Turning Hotel Data Into
            <span>Smart Decisions</span>

        </h2>

        <p class="section-description">

            Hotel Booking AI analyzes historical reservation data
            to identify cancellation patterns and transform raw
            booking information into meaningful business insights.

        </p>

    </section>


    <!-- ========================================================
         STATISTICS
    ======================================================== -->

    <section class="stats">


        <div class="stat-card">

            <div class="stat-value">
                119,390
            </div>

            <div class="stat-title">
                Total Bookings
            </div>

            <div class="stat-description">
                Historical reservations
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-value">
                27.49%
            </div>

            <div class="stat-title">
                Cancellation Rate
            </div>

            <div class="stat-description">
                Bookings cancelled
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-value">
                72.51%
            </div>

            <div class="stat-title">
                Confirmed Rate
            </div>

            <div class="stat-description">
                Bookings completed
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-value">
                32+
            </div>

            <div class="stat-title">
                Features
            </div>

            <div class="stat-description">
                Booking attributes
            </div>

        </div>


    </section>


    <!-- ========================================================
         CAPABILITIES
    ======================================================== -->

    <section class="section">

        <div class="section-label">
            SYSTEM CAPABILITIES
        </div>

        <h2 class="section-title">

            One Platform.
            <span>Three Core Functions.</span>

        </h2>

        <p class="section-description">

            The system combines data analysis, interactive
            business intelligence, and machine learning prediction
            into one unified platform.

        </p>

    </section>


    <!-- ========================================================
         FEATURES
    ======================================================== -->

    <section class="features">


        <div class="feature-card">

            <div class="feature-number">
                01
            </div>

            <div class="feature-icon">
                📊
            </div>

            <h3>
                Data Analysis
            </h3>

            <p>

                Explore booking distributions, customer behavior,
                missing values, outliers, correlations and
                cancellation patterns.

            </p>

        </div>


        <div class="feature-card">

            <div class="feature-number">
                02
            </div>

            <div class="feature-icon">
                📈
            </div>

            <h3>
                Interactive Dashboard
            </h3>

            <p>

                Monitor important hotel KPIs and discover
                meaningful business insights through interactive
                visualizations.

            </p>

        </div>


        <div class="feature-card">

            <div class="feature-number">
                03
            </div>

            <div class="feature-icon">
                🤖
            </div>

            <h3>
                AI Prediction
            </h3>

            <p>

                Predict whether a new hotel reservation is likely
                to be cancelled using the trained machine learning
                model.

            </p>

        </div>


    </section>


    <!-- ========================================================
         MACHINE LEARNING ENGINE
    ======================================================== -->

    <section class="model-section">


        <div>

            <div class="model-label">
                MACHINE LEARNING ENGINE
            </div>

            <div class="model-title">

                Powered by
                <span>XGBoost</span>

            </div>


            <p class="model-description">

                The prediction engine uses XGBoost, a powerful
                gradient boosting algorithm optimized for
                structured and tabular data. It learns relationships
                between booking features to estimate cancellation risk.

            </p>


            <div class="model-features">

                <div class="model-feature">
                    ✓ Binary Classification
                </div>

                <div class="model-feature">
                    ✓ Tabular Data
                </div>

                <div class="model-feature">
                    ✓ Complex Relationships
                </div>

                <div class="model-feature">
                    ✓ High Performance
                </div>

            </div>

        </div>


        <div class="model-target">

            <div class="target-label">
                PREDICTION TARGET
            </div>

            <div class="target-name">
                is_canceled
            </div>


            <div class="target-row">

                <div class="target-number">
                    0
                </div>

                Booking is not cancelled

            </div>


            <div class="target-row">

                <div class="target-number">
                    1
                </div>

                Booking is cancelled

            </div>

        </div>


    </section>


    <!-- ========================================================
         WORKFLOW TITLE
    ======================================================== -->

    <section class="section">

        <div class="section-label">
            MACHINE LEARNING WORKFLOW
        </div>

        <h2 class="section-title">

            From Raw Data To
            <span>Prediction</span>

        </h2>

    </section>


    <!-- ========================================================
         WORKFLOW
    ======================================================== -->

    <section class="workflow">


        <div class="workflow-step">

            <div class="workflow-number">
                01
            </div>

            <div class="workflow-name">
                Data Collection
            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="workflow-number">
                02
            </div>

            <div class="workflow-name">
                Data Analysis
            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="workflow-number">
                03
            </div>

            <div class="workflow-name">
                Preprocessing
            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="workflow-number">
                04
            </div>

            <div class="workflow-name">
                XGBoost Model
            </div>

        </div>


        <div class="workflow-line"></div>


        <div class="workflow-step">

            <div class="workflow-number">
                05
            </div>

            <div class="workflow-name">
                Prediction
            </div>

        </div>


    </section>


    <!-- ========================================================
         FOOTER
    ======================================================== -->

    <footer class="footer">

        <div class="footer-title">
            Hotel Booking AI
        </div>

        <div class="footer-text">
            Machine Learning Project
        </div>

    </footer>


</div>

""")