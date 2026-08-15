import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Hotel Booking AI | Analysis",
    page_icon="🔬",
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

    "blue": "#3B82F6",
    "blue_light": "#60A5FA",

    "purple": "#8B5CF6",
    "purple_light": "#A78BFA",

    "cyan": "#22D3EE",
    "green": "#22C55E",
    "yellow": "#F59E0B",
    "red": "#EF4444",
    "pink": "#EC4899",

    "text": "#F8FAFC",
    "muted": "#94A3B8",
    "soft": "#64748B",

    "border": "rgba(148,163,184,0.12)"
}


DATA_PATH = "hotel_bookings.csv"


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


try:
    df = load_data()
    data_loaded = True
    data_error = None

except Exception as e:
    df = None
    data_loaded = False
    data_error = str(e)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    f"""
<style>

:root {{
    --bg: {COLORS["background"]};
    --surface: {COLORS["surface"]};
    --surface-light: {COLORS["surface_light"]};

    --blue: {COLORS["blue"]};
    --blue-light: {COLORS["blue_light"]};

    --purple: {COLORS["purple"]};
    --purple-light: {COLORS["purple_light"]};

    --cyan: {COLORS["cyan"]};
    --green: {COLORS["green"]};
    --yellow: {COLORS["yellow"]};
    --red: {COLORS["red"]};
    --pink: {COLORS["pink"]};

    --text: {COLORS["text"]};
    --muted: {COLORS["muted"]};
    --soft: {COLORS["soft"]};
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
   APP
============================================================ */

.stApp {{
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(59,130,246,0.09),
            transparent 25%
        ),
        radial-gradient(
            circle at 95% 15%,
            rgba(139,92,246,0.08),
            transparent 25%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(34,211,238,0.035),
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


[data-testid="stSidebarNav"] {{
    padding: 10px;
}}


[data-testid="stSidebarNav"] a {{
    border-radius: 12px;
    padding: 12px 14px;
    margin: 6px 0;

    color: #94A3B8 !important;

    background: transparent;
    border: 1px solid transparent;

    transition: all 0.25s ease;
}}


[data-testid="stSidebarNav"] a:hover {{
    color: #F8FAFC !important;

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.12),
            rgba(139,92,246,0.07)
        );

    border:
        1px solid
        rgba(96,165,250,0.18);

    transform:
        translateX(4px);
}}


[data-testid="stSidebarNav"]
a[aria-current="page"] {{

    color: white !important;

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.20),
            rgba(139,92,246,0.13)
        );

    border:
        1px solid
        rgba(96,165,250,0.28);

    box-shadow:
        0 8px 30px
        rgba(59,130,246,0.12);
}}


/* ============================================================
   BRAND
============================================================ */

.sidebar-brand {{
    padding: 20px;
    margin: 5px 5px 22px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            rgba(59,130,246,0.12),
            rgba(139,92,246,0.09)
        );

    border:
        1px solid
        rgba(96,165,250,0.15);

    box-shadow:
        0 10px 35px
        rgba(0,0,0,0.20);
}}


.sidebar-brand-title {{
    font-size: 18px;
    font-weight: 900;
    color: white;
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
   MAIN CONTAINER
============================================================ */

.analysis-container {{
    max-width: 1450px;
    margin: auto;
    padding: 25px 42px 10px;
}}


/* ============================================================
   HERO
============================================================ */

.analysis-hero {{
    position: relative;
    overflow: hidden;

    padding: 48px 52px;
    margin-bottom: 25px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            #0B1728 0%,
            #0D1B2A 50%,
            #151633 100%
        );

    border:
        1px solid
        rgba(148,163,184,0.12);

    box-shadow:
        0 25px 70px
        rgba(0,0,0,0.28);

    animation:
        heroEnter 0.75s ease both;
}}


.analysis-hero::before {{
    content: "";

    position: absolute;

    width: 420px;
    height: 420px;

    right: -150px;
    top: -220px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(59,130,246,0.25),
            transparent 70%
        );

    filter: blur(10px);
}}


.analysis-hero::after {{
    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    left: -160px;
    bottom: -200px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(139,92,246,0.20),
            transparent 70%
        );
}}


.hero-content {{
    position: relative;
    z-index: 2;
}}


.hero-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;

    padding: 8px 14px;

    border-radius: 50px;

    color: #60A5FA;

    background:
        rgba(59,130,246,0.08);

    border:
        1px solid
        rgba(96,165,250,0.18);

    font-size: 10px;
    font-weight: 800;

    letter-spacing: 2px;
}}


.hero-title {{
    margin-top: 18px;

    font-size:
        clamp(38px, 5vw, 60px);

    font-weight: 900;

    letter-spacing: -3px;

    line-height: 1.05;

    color: white;
}}


.hero-title span {{
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


.hero-description {{
    max-width: 850px;

    margin-top: 16px;

    color: var(--muted);

    font-size: 15px;

    line-height: 1.8;
}}


/* ============================================================
   KPI
============================================================ */

.analysis-kpis {{
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 18px;

    margin-bottom: 30px;
}}


.analysis-kpi {{
    padding: 22px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(13,27,42,0.95),
            rgba(10,22,38,0.80)
        );

    border:
        1px solid
        rgba(148,163,184,0.10);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.17);

    transition:
        all 0.3s ease;

    animation:
        fadeUp 0.7s ease both;
}}


.analysis-kpi:hover {{
    transform:
        translateY(-6px);

    border-color:
        rgba(96,165,250,0.25);

    box-shadow:
        0 20px 45px
        rgba(59,130,246,0.10);
}}


.kpi-label {{
    color: var(--muted);

    font-size: 10px;

    font-weight: 800;

    letter-spacing: 1px;
}}


.kpi-number {{
    margin-top: 8px;

    font-size: 28px;

    font-weight: 900;

    color: white;
}}


.kpi-description {{
    margin-top: 6px;

    color: var(--soft);

    font-size: 10px;
}}


/* ============================================================
   FILTER BOX
============================================================ */

.filter-box {{
    padding: 24px;
    margin-bottom: 18px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(13,27,42,0.94),
            rgba(10,22,38,0.78)
        );

    border:
        1px solid
        rgba(148,163,184,0.10);

    animation:
        fadeUp 0.8s ease both;
}}


.filter-title {{
    color: white;

    font-size: 17px;

    font-weight: 850;
}}


.filter-subtitle {{
    margin-top: 5px;
    margin-bottom: 20px;

    color: var(--soft);

    font-size: 11px;
}}


/* ============================================================
   STREAMLIT INPUTS
============================================================ */

.stSelectbox label {{
    color: #CBD5E1 !important;
    font-weight: 700 !important;
}}


.stSelectbox > div > div {{
    background: #0D1B2A !important;

    border:
        1px solid
        rgba(148,163,184,0.15) !important;

    border-radius: 12px !important;

    color: white !important;
}}


/* ============================================================
   SECTION
============================================================ */

.section-title {{
    display: flex;

    align-items: center;

    gap: 12px;

    margin:
        38px 0 16px;

    font-size: 20px;

    font-weight: 850;

    color: white;
}}


.section-title::before {{
    content: "";

    width: 5px;
    height: 25px;

    border-radius: 10px;

    background:
        linear-gradient(
            180deg,
            #60A5FA,
            #8B5CF6
        );

    box-shadow:
        0 0 18px
        rgba(96,165,250,0.30);
}}


/* ============================================================
   CHART WRAPPER
============================================================ */

.chart-wrapper {{
    padding: 7px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(13,27,42,0.95),
            rgba(10,22,38,0.80)
        );

    border:
        1px solid
        rgba(148,163,184,0.09);

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.16);

    transition:
        all 0.3s ease;
}}


.chart-wrapper:hover {{
    transform:
        translateY(-4px);

    border-color:
        rgba(96,165,250,0.20);

    box-shadow:
        0 20px 50px
        rgba(59,130,246,0.08);
}}


/* ============================================================
   INSIGHTS
============================================================ */

.insight-grid {{
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 18px;

    margin-top: 20px;
}}


.insight-card {{
    position: relative;
    overflow: hidden;

    padding: 24px;

    min-height: 180px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(13,27,42,0.94),
            rgba(10,22,38,0.78)
        );

    border:
        1px solid
        rgba(148,163,184,0.09);

    transition:
        all 0.3s ease;
}}


.insight-card:hover {{
    transform:
        translateY(-6px);

    border-color:
        rgba(96,165,250,0.22);
}}


.insight-card::before {{
    content: "";

    position: absolute;

    width: 120px;
    height: 120px;

    right: -60px;
    top: -60px;

    border-radius: 50%;

    background:
        rgba(59,130,246,0.08);
}}


.insight-icon {{
    font-size: 25px;
    margin-bottom: 13px;
}}


.insight-title {{
    font-size: 15px;

    font-weight: 850;

    color: white;
}}


.insight-text {{
    margin-top: 10px;

    color: var(--muted);

    font-size: 12px;

    line-height: 1.7;
}}


/* ============================================================
   FOOTER
============================================================ */

.analysis-footer {{
    margin-top: 70px;

    padding:
        25px 0;

    text-align: center;

    border-top:
        1px solid
        rgba(148,163,184,0.08);

    color: #475569;

    font-size: 11px;
}}


/* ============================================================
   ANIMATIONS
============================================================ */

@keyframes heroEnter {{
    from {{
        opacity: 0;
        transform:
            translateY(-20px);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0);
    }}
}}


@keyframes fadeUp {{
    from {{
        opacity: 0;
        transform:
            translateY(18px);
    }}

    to {{
        opacity: 1;
        transform:
            translateY(0);
    }}
}}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width: 1000px) {{

    .analysis-kpis {{
        grid-template-columns:
            repeat(2, 1fr);
    }}

    .insight-grid {{
        grid-template-columns:
            1fr;
    }}
}}


@media (max-width: 650px) {{

    .analysis-container {{
        padding:
            15px;
    }}

    .analysis-hero {{
        padding:
            35px 25px;
    }}

    .analysis-kpis {{
        grid-template-columns:
            1fr;
    }}
}}

</style>
"""
)


# ============================================================
# SIDEBAR BRAND
# ============================================================

st.html(
    """
<div class="sidebar-brand">

    <div class="sidebar-brand-title">
        Hotel Booking <span>AI</span>
    </div>

    <div class="sidebar-brand-subtitle">
        MACHINE LEARNING PLATFORM
    </div>

</div>
"""
)


# ============================================================
# DATA CHECK
# ============================================================

if not data_loaded:

    st.error("Unable to load hotel booking dataset.")

    st.code(data_error)

    st.stop()


data = df.copy()


# ============================================================
# BASIC CLEANING
# ============================================================

if "is_canceled" in data.columns:

    data["is_canceled"] = pd.to_numeric(
        data["is_canceled"],
        errors="coerce"
    )

    data["is_canceled"] = data["is_canceled"].fillna(0)


if "adr" in data.columns:

    data["adr"] = pd.to_numeric(
        data["adr"],
        errors="coerce"
    )


if "lead_time" in data.columns:

    data["lead_time"] = pd.to_numeric(
        data["lead_time"],
        errors="coerce"
    )


# ============================================================
# HERO
# ============================================================

st.html(
    """
<div class="analysis-container">

    <section class="analysis-hero">

        <div class="hero-content">

            <div class="hero-badge">
                ● EXPLORATORY DATA ANALYSIS
            </div>

            <div class="hero-title">
                Hotel Booking <span>Analysis</span>
            </div>

            <div class="hero-description">
                Explore the hidden patterns behind hotel bookings,
                cancellation behavior, customer segments, lead time,
                pricing and revenue indicators.
            </div>

        </div>

    </section>

</div>
"""
)


# ============================================================
# FILTER TITLE
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="filter-box">

        <div class="filter-title">
            🔎 Analysis Filters
        </div>

        <div class="filter-subtitle">
            Select specific booking segments to perform a deeper analysis.
        </div>

    </div>

</div>
"""
)


# ============================================================
# FILTERS
# ============================================================

f1, f2, f3 = st.columns(3)


with f1:

    if "hotel" in data.columns:

        hotels = ["All Hotels"] + sorted(
            data["hotel"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_hotel = st.selectbox(
            "Hotel",
            hotels
        )

    else:

        selected_hotel = "All Hotels"


with f2:

    if "market_segment" in data.columns:

        segments = ["All Segments"] + sorted(
            data["market_segment"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        selected_segment = st.selectbox(
            "Market Segment",
            segments
        )

    else:

        selected_segment = "All Segments"


with f3:

    if "arrival_date_year" in data.columns:

        years_values = sorted(
            data["arrival_date_year"]
            .dropna()
            .unique()
            .tolist()
        )

        years = ["All Years"] + years_values

        selected_year = st.selectbox(
            "Arrival Year",
            years
        )

    else:

        selected_year = "All Years"


# ============================================================
# APPLY FILTERS
# ============================================================

filtered = data.copy()


if (
    selected_hotel != "All Hotels"
    and "hotel" in filtered.columns
):

    filtered = filtered[
        filtered["hotel"].astype(str) == selected_hotel
    ]


if (
    selected_segment != "All Segments"
    and "market_segment" in filtered.columns
):

    filtered = filtered[
        filtered["market_segment"].astype(str)
        == selected_segment
    ]


if (
    selected_year != "All Years"
    and "arrival_date_year" in filtered.columns
):

    filtered = filtered[
        filtered["arrival_date_year"] == selected_year
    ]


# ============================================================
# KPI VALUES
# ============================================================

total = len(filtered)


if (
    total > 0
    and "is_canceled" in filtered.columns
):

    cancel_rate = (
        filtered["is_canceled"].mean()
        * 100
    )

else:

    cancel_rate = 0


if (
    total > 0
    and "adr" in filtered.columns
):

    avg_adr = (
        filtered["adr"]
        .replace([np.inf, -np.inf], np.nan)
        .mean()
    )

else:

    avg_adr = 0


if (
    total > 0
    and "lead_time" in filtered.columns
):

    avg_lead = (
        filtered["lead_time"]
        .replace([np.inf, -np.inf], np.nan)
        .mean()
    )

else:

    avg_lead = 0


if pd.isna(avg_adr):
    avg_adr = 0


if pd.isna(avg_lead):
    avg_lead = 0


# ============================================================
# KPI CARDS
# ============================================================

st.html(
    f"""
<div class="analysis-container">

    <div class="analysis-kpis">

        <div class="analysis-kpi">

            <div class="kpi-label">
                ANALYZED BOOKINGS
            </div>

            <div class="kpi-number">
                {total:,}
            </div>

            <div class="kpi-description">
                Records after selected filters
            </div>

        </div>


        <div class="analysis-kpi">

            <div class="kpi-label">
                CANCELLATION RATE
            </div>

            <div class="kpi-number">
                {cancel_rate:.1f}%
            </div>

            <div class="kpi-description">
                Current cancellation behavior
            </div>

        </div>


        <div class="analysis-kpi">

            <div class="kpi-label">
                AVERAGE ADR
            </div>

            <div class="kpi-number">
                €{avg_adr:,.2f}
            </div>

            <div class="kpi-description">
                Average daily room rate
            </div>

        </div>


        <div class="analysis-kpi">

            <div class="kpi-label">
                AVG. LEAD TIME
            </div>

            <div class="kpi-number">
                {avg_lead:.1f}
            </div>

            <div class="kpi-description">
                Days between booking and arrival
            </div>

        </div>

    </div>

</div>
"""
)


# ============================================================
# CHART FUNCTIONS
# ============================================================

def style_chart(fig, height=410):

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        height=height,

        margin=dict(
            l=25,
            r=25,
            t=60,
            b=35
        ),

        font=dict(
            family="Inter, Arial",
            color="#CBD5E1"
        ),

        title_font=dict(
            size=17,
            color="#F8FAFC"
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        ),

        hoverlabel=dict(
            bgcolor="#0D1B2A",
            bordercolor="#334155",
            font_color="#F8FAFC"
        ),

        transition=dict(
            duration=500
        )

    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.06)",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148,163,184,0.06)",
        zeroline=False
    )

    return fig


def show_chart(fig):

    st.html(
        '<div class="chart-wrapper">'
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "responsive": True
        }
    )

    st.html(
        "</div>"
    )


# ============================================================
# SECTION 1
# BOOKING BEHAVIOR
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        📊 Booking Behavior Analysis
    </div>

</div>
"""
)


c1, c2 = st.columns(2)


# ============================================================
# HOTEL DISTRIBUTION
# ============================================================

with c1:

    if "hotel" in filtered.columns:

        hotel_df = (
            filtered["hotel"]
            .value_counts()
            .reset_index()
        )

        hotel_df.columns = [
            "Hotel",
            "Bookings"
        ]

        fig = px.bar(
            hotel_df,
            x="Hotel",
            y="Bookings",
            title="Booking Distribution by Hotel",
            text="Bookings",
            color="Hotel",
            color_discrete_sequence=[
                COLORS["blue"],
                COLORS["purple"]
            ]
        )

        fig.update_traces(
            texttemplate="%{text:,}",
            textposition="outside"
        )

        fig = style_chart(fig)

        fig.update_layout(
            showlegend=False
        )

        show_chart(fig)


# ============================================================
# CUSTOMER TYPE
# ============================================================

with c2:

    if "customer_type" in filtered.columns:

        customer_df = (
            filtered["customer_type"]
            .value_counts()
            .reset_index()
        )

        customer_df.columns = [
            "Customer Type",
            "Bookings"
        ]

        fig = px.pie(
            customer_df,
            names="Customer Type",
            values="Bookings",
            hole=0.62,
            title="Customer Type Distribution",
            color_discrete_sequence=[
                COLORS["blue"],
                COLORS["purple"],
                COLORS["cyan"],
                COLORS["pink"]
            ]
        )

        fig.update_traces(

            textinfo="percent+label",

            textfont_size=11,

            marker=dict(
                line=dict(
                    color="#07111F",
                    width=3
                )
            )
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# SECTION 2
# CANCELLATION DRIVERS
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        ❌ Cancellation Drivers
    </div>

</div>
"""
)


c1, c2 = st.columns(2)


# ============================================================
# DEPOSIT TYPE
# ============================================================

with c1:

    if (
        "deposit_type" in filtered.columns
        and "is_canceled" in filtered.columns
    ):

        deposit_df = (
            filtered
            .groupby("deposit_type")
            .agg(
                bookings=("is_canceled", "size"),
                cancellations=("is_canceled", "sum")
            )
            .reset_index()
        )

        deposit_df["Cancellation Rate"] = np.where(

            deposit_df["bookings"] > 0,

            (
                deposit_df["cancellations"]
                / deposit_df["bookings"]
                * 100
            ),

            0
        )

        fig = px.bar(

            deposit_df,

            x="deposit_type",

            y="Cancellation Rate",

            title="Cancellation Rate by Deposit Type",

            text="Cancellation Rate",

            color="Cancellation Rate",

            color_continuous_scale=[
                COLORS["green"],
                COLORS["yellow"],
                COLORS["red"]
            ]
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(
            coloraxis_showscale=False,
            yaxis_title="Cancellation Rate (%)",
            xaxis_title=""
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# MARKET SEGMENT CANCELLATION
# ============================================================

with c2:

    if (
        "market_segment" in filtered.columns
        and "is_canceled" in filtered.columns
    ):

        market_cancel = (
            filtered
            .groupby("market_segment")
            .agg(
                bookings=("is_canceled", "size"),
                cancellations=("is_canceled", "sum")
            )
            .reset_index()
        )

        market_cancel["Cancellation Rate"] = np.where(

            market_cancel["bookings"] > 0,

            (
                market_cancel["cancellations"]
                / market_cancel["bookings"]
                * 100
            ),

            0
        )

        market_cancel = market_cancel.sort_values(
            "Cancellation Rate"
        )

        fig = px.bar(

            market_cancel,

            x="Cancellation Rate",

            y="market_segment",

            orientation="h",

            title="Cancellation Rate by Market Segment",

            text="Cancellation Rate",

            color="Cancellation Rate",

            color_continuous_scale=[
                COLORS["blue"],
                COLORS["purple"],
                COLORS["red"]
            ]
        )

        fig.update_traces(
            texttemplate="%{text:.1f}%",
            textposition="outside"
        )

        fig.update_layout(

            coloraxis_showscale=False,

            xaxis_title="Cancellation Rate (%)",

            yaxis_title=""
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# SECTION 3
# LEAD TIME
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        ⏱️ Lead Time Analysis
    </div>

</div>
"""
)


if (
    "lead_time" in filtered.columns
    and "is_canceled" in filtered.columns
):

    temp = filtered.copy()

    bins = [
        -1,
        30,
        60,
        120,
        180,
        10000
    ]

    labels = [
        "0–30 Days",
        "31–60 Days",
        "61–120 Days",
        "121–180 Days",
        "180+ Days"
    ]

    temp["Lead Group"] = pd.cut(
        temp["lead_time"],
        bins=bins,
        labels=labels
    )

    lead_analysis = (
        temp
        .groupby(
            "Lead Group",
            observed=False
        )
        .agg(
            bookings=("is_canceled", "size"),
            cancellations=("is_canceled", "sum")
        )
        .reset_index()
    )

    lead_analysis["Cancellation Rate"] = np.where(

        lead_analysis["bookings"] > 0,

        (
            lead_analysis["cancellations"]
            / lead_analysis["bookings"]
            * 100
        ),

        0
    )

    l1, l2 = st.columns(2)


    # --------------------------------------------------------
    # BOOKING VOLUME
    # --------------------------------------------------------

    with l1:

        fig = px.bar(

            lead_analysis,

            x="Lead Group",

            y="bookings",

            title="Booking Volume by Lead Time",

            text="bookings"
        )

        fig.update_traces(

            marker_color=COLORS["blue_light"],

            texttemplate="%{text:,}",

            textposition="outside"
        )

        fig.update_layout(

            xaxis_title="Lead Time",

            yaxis_title="Bookings"
        )

        fig = style_chart(fig)

        show_chart(fig)


    # --------------------------------------------------------
    # CANCELLATION VS LEAD TIME
    # --------------------------------------------------------

    with l2:

        fig = px.line(

            lead_analysis,

            x="Lead Group",

            y="Cancellation Rate",

            title="Cancellation Rate vs Lead Time",

            markers=True
        )

        fig.update_traces(

            line=dict(
                color=COLORS["red"],
                width=4
            ),

            marker=dict(
                size=11
            )
        )

        fig.update_layout(

            xaxis_title="Lead Time",

            yaxis_title="Cancellation Rate (%)"
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# SECTION 4
# ADR ANALYSIS
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        💰 ADR & Pricing Analysis
    </div>

</div>
"""
)


a1, a2 = st.columns(2)


# ============================================================
# ADR DISTRIBUTION
# ============================================================

with a1:

    if "adr" in filtered.columns:

        adr_values = (
            filtered[
                filtered["adr"] >= 0
            ]["adr"]
            .dropna()
        )

        if len(adr_values) > 0:

            fig = px.histogram(

                adr_values,

                nbins=45,

                title="ADR Distribution"
            )

            fig.update_traces(

                marker_color=COLORS["blue"],

                marker_line_width=0
            )

            fig.update_layout(

                xaxis_title="ADR (€)",

                yaxis_title="Bookings"
            )

            fig = style_chart(fig)

            show_chart(fig)


# ============================================================
# ADR BY MARKET SEGMENT
# ============================================================

with a2:

    if (
        "adr" in filtered.columns
        and "market_segment" in filtered.columns
    ):

        adr_segment = (
            filtered
            .groupby("market_segment")["adr"]
            .mean()
            .reset_index()
            .sort_values("adr")
        )

        fig = px.bar(

            adr_segment,

            x="market_segment",

            y="adr",

            title="Average ADR by Market Segment",

            text="adr",

            color="adr",

            color_continuous_scale=[
                COLORS["blue"],
                COLORS["purple"],
                COLORS["pink"]
            ]
        )

        fig.update_traces(

            texttemplate="€%{text:.2f}",

            textposition="outside"
        )

        fig.update_layout(

            coloraxis_showscale=False,

            xaxis_title="",

            yaxis_title="Average ADR (€)"
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# SECTION 5
# DISTRIBUTION & OUTLIERS
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        📦 Distribution & Outlier Analysis
    </div>

</div>
"""
)


d1, d2 = st.columns(2)


# ============================================================
# LEAD TIME BOXPLOT
# ============================================================

with d1:

    if "lead_time" in filtered.columns:

        fig = px.box(

            filtered,

            y="lead_time",

            title="Lead Time Distribution & Outliers",

            points=False
        )

        fig.update_traces(
            marker_color=COLORS["purple"]
        )

        fig.update_layout(

            yaxis_title="Lead Time (Days)",

            xaxis_title=""
        )

        fig = style_chart(fig)

        show_chart(fig)


# ============================================================
# ADR BOXPLOT
# ============================================================

with d2:

    if "adr" in filtered.columns:

        adr_box = filtered[
            filtered["adr"] >= 0
        ]

        if len(adr_box) > 0:

            fig = px.box(

                adr_box,

                y="adr",

                title="ADR Distribution & Outliers",

                points=False
            )

            fig.update_traces(
                marker_color=COLORS["cyan"]
            )

            fig.update_layout(

                yaxis_title="ADR (€)",

                xaxis_title=""
            )

            fig = style_chart(fig)

            show_chart(fig)


# ============================================================
# SECTION 6
# CORRELATION
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        🔗 Feature Correlation Analysis
    </div>

</div>
"""
)


numeric_columns = (
    filtered
    .select_dtypes(include=np.number)
    .columns
    .tolist()
)


if len(numeric_columns) >= 2:

    corr = filtered[
        numeric_columns
    ].corr()

    fig = go.Figure(

        data=go.Heatmap(

            z=corr.values,

            x=corr.columns,

            y=corr.columns,

            colorscale=[

                [0, "#1E3A8A"],

                [0.5, "#0F172A"],

                [1, "#8B5CF6"]

            ],

            zmin=-1,

            zmax=1,

            text=np.round(
                corr.values,
                2
            ),

            texttemplate="%{text}",

            hovertemplate=
                "%{x} × %{y}"
                "<br>Correlation: %{z:.2f}"
                "<extra></extra>"
        )
    )

    fig.update_layout(
        title="Numeric Feature Correlation Matrix",
        height=650
    )

    fig = style_chart(
        fig,
        650
    )

    show_chart(fig)


# ============================================================
# SECTION 7
# CANCELLATION BY REPEATED GUEST
# ============================================================

if (
    "is_repeated_guest" in filtered.columns
    and "is_canceled" in filtered.columns
):

    st.html(
        """
<div class="analysis-container">

    <div class="section-title">
        👤 Guest Loyalty Analysis
    </div>

</div>
"""
    )

    repeated_df = (
        filtered
        .groupby("is_repeated_guest")
        .agg(
            bookings=("is_canceled", "size"),
            cancellations=("is_canceled", "sum")
        )
        .reset_index()
    )

    repeated_df["Cancellation Rate"] = np.where(

        repeated_df["bookings"] > 0,

        (
            repeated_df["cancellations"]
            / repeated_df["bookings"]
            * 100
        ),

        0
    )

    repeated_df["Guest Type"] = (
        repeated_df["is_repeated_guest"]
        .map({
            0: "New Guest",
            1: "Repeated Guest"
        })
    )

    fig = px.bar(

        repeated_df,

        x="Guest Type",

        y="Cancellation Rate",

        title="Cancellation Rate: New vs Repeated Guests",

        text="Cancellation Rate",

        color="Guest Type",

        color_discrete_sequence=[
            COLORS["blue"],
            COLORS["green"]
        ]
    )

    fig.update_traces(

        texttemplate="%{text:.1f}%",

        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        yaxis_title="Cancellation Rate (%)",
        xaxis_title=""
    )

    fig = style_chart(fig)

    show_chart(fig)


# ============================================================
# SECTION 8
# AUTOMATIC BUSINESS INSIGHTS
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="section-title">
        🧠 Automated Business Insights
    </div>

</div>
"""
)


insights = []


# ============================================================
# CANCELLATION INSIGHT
# ============================================================

if cancel_rate >= 35:

    insights.append({

        "icon": "⚠️",

        "title": "High Cancellation Exposure",

        "text": (
            f"The selected segment has a cancellation rate of "
            f"{cancel_rate:.1f}%, indicating a relatively high "
            f"reservation retention risk."
        )

    })

elif cancel_rate >= 20:

    insights.append({

        "icon": "🟡",

        "title": "Moderate Cancellation Exposure",

        "text": (
            f"The current cancellation rate is "
            f"{cancel_rate:.1f}%. Monitoring cancellation "
            f"drivers could help improve booking retention."
        )

    })

else:

    insights.append({

        "icon": "🟢",

        "title": "Low Cancellation Exposure",

        "text": (
            f"The current cancellation rate is "
            f"{cancel_rate:.1f}%, suggesting relatively "
            f"stable reservation retention."
        )

    })


# ============================================================
# LEAD TIME INSIGHT
# ============================================================

if (
    "lead_time" in filtered.columns
    and "is_canceled" in filtered.columns
):

    long_lead = filtered[
        filtered["lead_time"] > 120
    ]

    if len(long_lead) > 0:

        long_cancel = (
            long_lead["is_canceled"].mean()
            * 100
        )

        insights.append({

            "icon": "⏱️",

            "title": "Long Lead-Time Risk",

            "text": (
                f"Bookings made more than 120 days before "
                f"arrival show a cancellation rate of "
                f"approximately {long_cancel:.1f}%."
            )

        })


# ============================================================
# ADR INSIGHT
# ============================================================

if "adr" in filtered.columns:

    valid_adr = filtered[
        filtered["adr"] >= 0
    ]["adr"].dropna()

    if len(valid_adr) > 0:

        median_adr = valid_adr.median()

        if avg_adr > median_adr:

            insights.append({

                "icon": "💰",

                "title": "Above-Median Pricing",

                "text": (
                    f"The average ADR of €{avg_adr:.2f} "
                    f"is above the selected data median of "
                    f"€{median_adr:.2f}, indicating relatively "
                    f"higher room pricing."
                )

            })

        else:

            insights.append({

                "icon": "💡",

                "title": "Competitive Pricing",

                "text": (
                    f"The average ADR of €{avg_adr:.2f} "
                    f"is around or below the selected data "
                    f"median of €{median_adr:.2f}."
                )

            })


# ============================================================
# MARKET SEGMENT INSIGHT
# ============================================================

if "market_segment" in filtered.columns:

    market_counts = (
        filtered["market_segment"]
        .value_counts()
    )

    if len(market_counts) > 0:

        top_market = market_counts.index[0]

        top_market_count = market_counts.iloc[0]

        insights.append({

            "icon": "🎯",

            "title": "Dominant Market Segment",

            "text": (
                f"{top_market} is the dominant market "
                f"segment with approximately "
                f"{top_market_count:,} bookings in the "
                f"selected dataset."
            )

        })


# ============================================================
# HOTEL INSIGHT
# ============================================================

if "hotel" in filtered.columns:

    hotel_counts = (
        filtered["hotel"]
        .value_counts()
    )

    if len(hotel_counts) > 0:

        dominant_hotel = hotel_counts.index[0]

        insights.append({

            "icon": "🏨",

            "title": "Most Active Hotel",

            "text": (
                f"{dominant_hotel} represents the largest "
                f"booking volume in the selected dataset."
            )

        })


# ============================================================
# DISPLAY INSIGHTS
# ============================================================

insights = insights[:6]


for start in range(
    0,
    len(insights),
    3
):

    group = insights[
        start:start + 3
    ]

    html = """
<div class="analysis-container">

    <div class="insight-grid">
"""

    for insight in group:

        html += f"""
        <div class="insight-card">

            <div class="insight-icon">
                {insight["icon"]}
            </div>

            <div class="insight-title">
                {insight["title"]}
            </div>

            <div class="insight-text">
                {insight["text"]}
            </div>

        </div>
"""

    html += """
    </div>

</div>
"""

    st.html(html)


# ============================================================
# FINAL SUMMARY
# ============================================================

st.html(
    f"""
<div class="analysis-container">

    <div class="section-title">
        📌 Analysis Summary
    </div>

    <div class="insight-card">

        <div class="insight-title">
            Hotel Booking Dataset Overview
        </div>

        <div class="insight-text">

            The current analysis covers
            <strong>{total:,}</strong> booking records.

            The observed cancellation rate is
            <strong>{cancel_rate:.1f}%</strong>,

            while the average daily rate is
            <strong>€{avg_adr:.2f}</strong>.

            Average booking lead time is approximately
            <strong>{avg_lead:.1f} days</strong>.

            Use the filters above to investigate how these
            indicators change across hotels, market segments
            and arrival years.

        </div>

    </div>

</div>
"""
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
<div class="analysis-container">

    <div class="analysis-footer">

        Hotel Booking AI
        •
        Exploratory Data Analysis
        •
        Machine Learning Analytics Platform
        •
        XGBoost

    </div>

</div>
"""
)