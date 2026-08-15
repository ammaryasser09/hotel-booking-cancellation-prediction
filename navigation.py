import streamlit as st


def setup_navigation():

    st.markdown(
        """
        <style>

        /* =========================================
           FIXED SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            height: 100vh !important;

            overflow-y: auto !important;
            overflow-x: hidden !important;

            z-index: 999999 !important;

            background: #0B1728 !important;
        }


        /* =========================================
           SIDEBAR CONTENT
        ========================================= */

        [data-testid="stSidebar"] > div:first-child {
            height: 100vh !important;
            overflow-y: auto !important;
        }


        /* =========================================
           NAVIGATION CONTAINER
        ========================================= */

        [data-testid="stSidebarNav"] {
            padding: 12px !important;
        }


        /* =========================================
           NAVIGATION LINKS
        ========================================= */

        [data-testid="stSidebarNav"] a {

            display: flex !important;
            align-items: center !important;

            position: relative !important;

            padding: 12px 14px !important;
            margin: 6px 0 !important;

            border-radius: 12px !important;

            color: #94A3B8 !important;

            background: transparent !important;

            border: 1px solid transparent !important;

            /*
                IMPORTANT:
                No transform.
                No position animation.
            */

            transform: none !important;

            transition:
                background-color 0.25s ease,
                border-color 0.25s ease,
                color 0.25s ease,
                box-shadow 0.25s ease !important;
        }


        /* =========================================
           HOVER
        ========================================= */

        [data-testid="stSidebarNav"] a:hover {

            color: #F8FAFC !important;

            background:
                linear-gradient(
                    135deg,
                    rgba(59,130,246,0.10),
                    rgba(139,92,246,0.06)
                ) !important;

            border-color:
                rgba(96,165,250,0.18) !important;

            transform: none !important;

            box-shadow:
                0 8px 25px
                rgba(59,130,246,0.10) !important;
        }


        /* =========================================
           ACTIVE PAGE
        ========================================= */

        [data-testid="stSidebarNav"] a[aria-current="page"] {

            color: #FFFFFF !important;

            background:
                linear-gradient(
                    135deg,
                    rgba(59,130,246,0.18),
                    rgba(139,92,246,0.12)
                ) !important;

            border-color:
                rgba(96,165,250,0.28) !important;

            box-shadow:
                0 8px 30px
                rgba(59,130,246,0.12) !important;

            transform: none !important;
        }


        /* =========================================
           ACTIVE INDICATOR
        ========================================= */

        [data-testid="stSidebarNav"] a[aria-current="page"]::before {

            content: "" !important;

            position: absolute !important;

            left: 4px !important;
            top: 50% !important;

            transform: translateY(-50%) !important;

            width: 3px !important;
            height: 24px !important;

            border-radius: 10px !important;

            background:
                linear-gradient(
                    180deg,
                    #60A5FA,
                    #8B5CF6
                ) !important;

            box-shadow:
                0 0 15px
                rgba(96,165,250,0.70) !important;
        }


        /* =========================================
           REMOVE GLOBAL SMOOTH SCROLL
        ========================================= */

        html {
            scroll-behavior: auto !important;
        }


        /* =========================================
           SIDEBAR SCROLLBAR
        ========================================= */

        [data-testid="stSidebar"]::-webkit-scrollbar {
            width: 5px;
        }

        [data-testid="stSidebar"]::-webkit-scrollbar-track {
            background: transparent;
        }

        [data-testid="stSidebar"]::-webkit-scrollbar-thumb {
            background: rgba(148,163,184,0.15);
            border-radius: 10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )