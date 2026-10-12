"""Shared OvaSight design system, themes, and presentational helpers."""
from html import escape

import streamlit as st


THEMES = {
    "MEDICAL_GREEN": {
        "label": "Medical Green",
        "primary": "#2F9968", "primary_dark": "#237A52", "primary_light": "#EAF6F0",
        "background": "#F7F9F8", "surface": "#FFFFFF", "surface_secondary": "#F1F5F3",
        "text": "#111827", "text_secondary": "#667085", "border": "#D9E1DD",
        "success": "#2F9968", "warning": "#C98518", "danger": "#C83D3D", "info": "#3178C6",
        "chart_grid": "#E5ECE8",
    },
    "CLINICAL_BLUE": {
        "label": "Clinical Blue",
        "primary": "#2878C8", "primary_dark": "#1C5B9D", "primary_light": "#EAF3FC",
        "background": "#F7F9FC", "surface": "#FFFFFF", "surface_secondary": "#F1F5FA",
        "text": "#111827", "text_secondary": "#667085", "border": "#D9E2EC",
        "success": "#25805A", "warning": "#C98518", "danger": "#C83D3D", "info": "#2878C8",
        "chart_grid": "#E3EAF2",
    },
    "TEAL": {
        "label": "Teal",
        "primary": "#168A88", "primary_dark": "#126B6A", "primary_light": "#E6F6F5",
        "background": "#F6FAFA", "surface": "#FFFFFF", "surface_secondary": "#EFF6F6",
        "text": "#102A2A", "text_secondary": "#627777", "border": "#D5E4E3",
        "success": "#25805A", "warning": "#C98518", "danger": "#C83D3D", "info": "#2878C8",
        "chart_grid": "#DDEAEA",
    },
    "DARK_MEDICAL": {
        "label": "Dark Medical",
        "primary": "#48B982", "primary_dark": "#329866", "primary_light": "#173D2B",
        "background": "#101917", "surface": "#17231F", "surface_secondary": "#21312C",
        "text": "#F1F7F3", "text_secondary": "#B4C3BC", "border": "#34463E",
        "success": "#56C98F", "warning": "#E4AC4B", "danger": "#F07070", "info": "#72A9E5",
        "chart_grid": "#30443B",
    },
}


def get_theme() -> dict:
    """Return the active theme, keeping the selection ready for future user settings."""
    theme_name = st.session_state.get("theme", "MEDICAL_GREEN")
    return THEMES.get(theme_name, THEMES["MEDICAL_GREEN"])


def inject_css() -> None:
    theme = get_theme()
    tokens = f"""
    :root {{
        --ovs-primary: {theme['primary']};
        --ovs-primary-dark: {theme['primary_dark']};
        --ovs-primary-light: {theme['primary_light']};
        --ovs-background: {theme['background']};
        --ovs-surface: {theme['surface']};
        --ovs-surface-secondary: {theme['surface_secondary']};
        --ovs-text: {theme['text']};
        --ovs-text-secondary: {theme['text_secondary']};
        --ovs-border: {theme['border']};
        --ovs-success: {theme['success']};
        --ovs-warning: {theme['warning']};
        --ovs-danger: {theme['danger']};
        --ovs-info: {theme['info']};
        --ovs-chart-grid: {theme['chart_grid']};
        --ovs-radius-sm: 10px;
        --ovs-radius-md: 16px;
        --ovs-radius-lg: 24px;
        --ovs-radius-pill: 999px;
        --ovs-space-1: 4px;
        --ovs-space-2: 8px;
        --ovs-space-3: 12px;
        --ovs-space-4: 16px;
        --ovs-space-6: 24px;
        --ovs-space-8: 32px;
        --ovs-space-12: 48px;
    }}
    """
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+Thai:wght@400;500;600;700&display=swap');
    {tokens}

    html, body, [class*="css"] {{ font-family: 'DM Sans', 'Noto Sans Thai', sans-serif; }}
    [data-testid="stAppViewContainer"], .stApp {{ background: var(--ovs-background); color: var(--ovs-text); }}
    .main .block-container {{
        width: 100%; max-width: 1400px; margin: 0 auto; padding: 0 clamp(16px, 4vw, 48px) 48px !important;
    }}
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}
    [data-testid="stMarkdownContainer"] {{ color: var(--ovs-text); }}

    .ovs-nav {{
        display: flex; align-items: center; justify-content: space-between; gap: var(--ovs-space-4);
        padding: 16px 0; border-bottom: 1px solid var(--ovs-border); margin-bottom: 16px;
    }}
    .ovs-nav__brand {{ color: var(--ovs-text); font-size: clamp(1.15rem, 2vw, 1.4rem); font-weight: 700; letter-spacing: -0.03em; }}
    .ovs-nav__brand-mark {{ color: var(--ovs-primary); margin-right: 8px; }}
    .ovs-nav__links {{ display: flex; align-items: center; gap: 4px; flex-wrap: wrap; justify-content: flex-end; }}
    .ovs-nav__link {{ padding: 8px 10px; border-radius: var(--ovs-radius-pill); color: var(--ovs-text-secondary); font-size: .875rem; font-weight: 600; }}
    .ovs-nav__link--active {{ color: var(--ovs-primary-dark); background: var(--ovs-primary-light); }}
    .ovs-theme-row {{ display: flex; justify-content: flex-end; margin: -58px 0 22px; pointer-events: none; }}
    .ovs-theme-row > div {{ width: min(100%, 190px); pointer-events: auto; }}
    .st-key-theme [data-baseweb="select"] > div {{ min-height: 38px; border-radius: var(--ovs-radius-pill); border-color: var(--ovs-border); background: var(--ovs-surface); }}

    .ovs-page {{ padding-bottom: var(--ovs-space-8); }}
    .ovs-eyebrow {{ color: var(--ovs-primary-dark); font-size: .78rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
    .ovs-section-title {{ color: var(--ovs-text); font-size: clamp(1.25rem, 2.3vw, 1.7rem); font-weight: 700; letter-spacing: -.025em; margin: 0 0 var(--ovs-space-4); }}
    .ovs-section-copy {{ color: var(--ovs-text-secondary); line-height: 1.7; }}
    .ovs-hero {{ background: var(--ovs-surface); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-lg); padding: clamp(24px, 5vw, 52px); margin: 20px 0 28px; }}
    .ovs-hero--accent {{ border-left: 6px solid var(--ovs-primary); }}
    .ovs-hero__badge {{ display: inline-flex; padding: 6px 12px; border-radius: var(--ovs-radius-pill); background: var(--ovs-primary-light); color: var(--ovs-primary-dark); font-size: .78rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; }}
    .ovs-hero__title {{ color: var(--ovs-text); font-size: clamp(2rem, 4.2vw, 3.25rem); font-weight: 700; line-height: 1.16; letter-spacing: -.045em; margin: 16px 0 12px; }}
    .ovs-hero__copy {{ max-width: 760px; color: var(--ovs-text-secondary); font-size: clamp(.98rem, 1.6vw, 1.08rem); line-height: 1.7; margin: 0; }}
    .ovs-hero__meta {{ display: flex; flex-wrap: wrap; gap: clamp(16px, 3vw, 36px); margin-top: 28px; padding-top: 20px; border-top: 1px solid var(--ovs-border); }}
    .ovs-hero__metric strong {{ display: block; color: var(--ovs-text); font-size: 1rem; }}
    .ovs-hero__metric span {{ color: var(--ovs-text-secondary); font-size: .78rem; }}

    .ovs-card {{ background: var(--ovs-surface); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-md); padding: clamp(18px, 2.5vw, 28px); }}
    .ovs-card--highlight {{ border-color: var(--ovs-primary); background: var(--ovs-primary-light); }}
    .ovs-card--result {{ border-left: 5px solid var(--ovs-primary); }}
    .ovs-card--warning {{ border-left: 5px solid var(--ovs-warning); background: color-mix(in srgb, var(--ovs-warning) 8%, var(--ovs-surface)); }}
    .ovs-card--danger {{ border-left: 5px solid var(--ovs-danger); background: color-mix(in srgb, var(--ovs-danger) 7%, var(--ovs-surface)); }}
    .ovs-card--info {{ border-left: 5px solid var(--ovs-info); background: color-mix(in srgb, var(--ovs-info) 7%, var(--ovs-surface)); }}
    .ovs-card__title {{ color: var(--ovs-text); font-size: 1.05rem; font-weight: 700; margin: 0 0 8px; }}
    .ovs-card__copy {{ color: var(--ovs-text-secondary); font-size: .92rem; line-height: 1.65; margin: 0; }}
    .ovs-section-break {{ border-top: 1px solid var(--ovs-border); margin: clamp(36px, 6vw, 64px) 0 24px; padding-top: 24px; }}
    .ovs-feature {{ height: 100%; text-align: center; }}
    .ovs-feature__icon {{ color: var(--ovs-primary); font-size: 1.75rem; line-height: 1; margin-bottom: 14px; }}
    .ovs-step {{ margin: 12px 0; }}
    .ovs-intro {{ margin: 8px 0 18px; }}
    .ovs-atlas {{ padding-bottom: var(--ovs-space-12); }}
    .ovs-atlas-hero {{ display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(220px, .75fr); gap: clamp(20px, 4vw, 48px); align-items: center; }}
    .ovs-atlas-visual {{ min-height: 220px; border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-lg); background: var(--ovs-surface-secondary); position: relative; overflow: hidden; }}
    .ovs-atlas-visual::before, .ovs-atlas-visual::after {{ content: ""; position: absolute; border: 2px solid var(--ovs-primary); border-radius: 50%; opacity: .6; }}
    .ovs-atlas-visual::before {{ width: 180px; height: 180px; right: 18%; top: 20px; }}
    .ovs-atlas-visual::after {{ width: 88px; height: 88px; left: 15%; bottom: 22px; }}
    .ovs-atlas-visual__label {{ position: absolute; left: 20px; bottom: 18px; color: var(--ovs-text-secondary); font-size: .75rem; font-weight: 600; }}
    .ovs-atlas-visual__dot {{ position: absolute; width: 28px; height: 28px; border-radius: 50%; background: var(--ovs-primary); right: 37%; top: 42%; box-shadow: 0 0 0 12px color-mix(in srgb, var(--ovs-primary) 12%, transparent); }}
    [class*="st-key-atlas_topic_"] > div > button {{ min-height: 144px; white-space: pre-line; text-align: left; align-items: flex-start; justify-content: flex-start; padding: 18px !important; border-color: var(--ovs-border); background: var(--ovs-surface); color: var(--ovs-text); }}
    [class*="st-key-atlas_topic_"] > div > button:hover {{ background: var(--ovs-primary-light); border-color: var(--ovs-primary); color: var(--ovs-primary-dark); transform: translateY(-2px); }}
    [class*="st-key-atlas_nav_"] > div > button {{ min-height: 40px; padding: 7px 10px !important; border-radius: var(--ovs-radius-pill); border-color: var(--ovs-border); background: var(--ovs-surface); color: var(--ovs-text-secondary); font-size: .78rem; }}
    [class*="st-key-atlas_nav_"] > div > button:hover, [class*="st-key-atlas_nav_active_"] > div > button {{ background: var(--ovs-primary-light); border-color: var(--ovs-primary); color: var(--ovs-primary-dark); transform: none; }}
    .ovs-atlas-flow {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; align-items: stretch; }}
    .ovs-atlas-flow__item {{ background: var(--ovs-surface-secondary); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-sm); color: var(--ovs-text); padding: 14px 10px; text-align: center; font-size: .84rem; font-weight: 700; }}
    .ovs-atlas-flow__num {{ display: block; color: var(--ovs-primary); font-size: .72rem; letter-spacing: .08em; margin-bottom: 6px; }}
    .ovs-atlas-step {{ height: 100%; }}
    .ovs-atlas-step__number {{ color: var(--ovs-primary); font-size: .78rem; font-weight: 700; letter-spacing: .08em; }}
    .ovs-atlas-header {{ display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(180px, .55fr); gap: clamp(18px, 4vw, 40px); align-items: center; padding: clamp(20px, 3vw, 32px); margin: 12px 0 22px; }}
    .ovs-atlas-header .ovs-hero__title {{ font-size: clamp(1.8rem, 3.2vw, 2.55rem); margin: 10px 0 8px; }}
    .ovs-atlas-header .ovs-atlas-visual {{ min-height: 150px; }}
    .ovs-atlas-panel {{ background: var(--ovs-surface); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-lg); padding: clamp(20px, 4vw, 36px); margin-top: 20px; }}
    .ovs-atlas-panel__kicker {{ color: var(--ovs-primary-dark); font-size: .78rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }}
    .ovs-atlas-panel__title {{ color: var(--ovs-text); font-size: clamp(1.35rem, 2.8vw, 2rem); font-weight: 700; letter-spacing: -.03em; margin: 8px 0 16px; }}
    .ovs-atlas-content {{ display: grid; grid-template-columns: minmax(0, .82fr) minmax(0, 1fr); gap: clamp(20px, 4vw, 40px); align-items: start; }}
    .ovs-atlas-content__lead {{ color: var(--ovs-text-secondary); font-size: 1rem; line-height: 1.7; margin: 0 0 16px; }}
    .ovs-atlas-list {{ margin: 0; padding-left: 20px; color: var(--ovs-text-secondary); line-height: 1.75; }}
    .ovs-atlas-list li + li {{ margin-top: 8px; }}
    .ovs-atlas-timeline {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
    .ovs-atlas-timeline__step {{ border-top: 2px solid var(--ovs-primary); padding-top: 12px; color: var(--ovs-text-secondary); font-size: .9rem; line-height: 1.55; }}
    .ovs-atlas-timeline__step strong {{ display: block; color: var(--ovs-text); margin: 6px 0; }}
    .st-key-atlas_topic div[data-testid="stRadio"] > div[role="radiogroup"] {{ display: flex !important; flex-wrap: nowrap !important; width: 100%; gap: 8px !important; overflow-x: auto; padding: 2px 0 8px; scrollbar-width: thin; }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"] {{ position: relative; flex: 0 0 auto; margin: 0 !important; padding: 9px 14px !important; border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-pill); background: var(--ovs-surface); cursor: pointer; transition: background-color .2s ease, border-color .2s ease; }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"] p {{ margin: 0 !important; color: var(--ovs-text) !important; font-family: 'Noto Sans Thai', sans-serif !important; font-size: clamp(.76rem, 1.5vw, .88rem) !important; font-weight: 700 !important; white-space: nowrap; transition: color .2s ease; }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {{ border-color: var(--ovs-primary); background: var(--ovs-primary-light); }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {{ border-color: var(--ovs-primary); background: var(--ovs-primary); }}
    .st-key-atlas_topic div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p {{ color: #fff !important; }}
    .ovs-stat {{ background: var(--ovs-surface); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-md); padding: 20px; min-height: 124px; }}
    .ovs-stat__label {{ color: var(--ovs-text-secondary); font-size: .82rem; font-weight: 600; }}
    .ovs-stat__value {{ color: var(--ovs-text); font-size: clamp(1.35rem, 2.5vw, 1.8rem); font-weight: 700; letter-spacing: -.035em; margin-top: 6px; }}
    .ovs-stat__value--danger {{ color: var(--ovs-danger); }} .ovs-stat__value--warning {{ color: var(--ovs-warning); }}
    .ovs-badge {{ display: inline-flex; align-items: center; gap: 6px; border-radius: var(--ovs-radius-pill); padding: 5px 10px; font-size: .75rem; font-weight: 700; }}
    .ovs-badge--success {{ color: var(--ovs-success); background: color-mix(in srgb, var(--ovs-success) 12%, var(--ovs-surface)); }}
    .ovs-badge--warning {{ color: var(--ovs-warning); background: color-mix(in srgb, var(--ovs-warning) 12%, var(--ovs-surface)); }}
    .ovs-badge--danger {{ color: var(--ovs-danger); background: color-mix(in srgb, var(--ovs-danger) 12%, var(--ovs-surface)); }}
    .ovs-badge--info {{ color: var(--ovs-info); background: color-mix(in srgb, var(--ovs-info) 12%, var(--ovs-surface)); }}

    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {{
        min-height: 44px; border-radius: var(--ovs-radius-sm); border: 1px solid var(--ovs-primary);
        background: var(--ovs-primary); color: #fff; font-weight: 700; transition: background-color .2s ease, border-color .2s ease, transform .2s ease;
    }}
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {{ background: var(--ovs-primary-dark); border-color: var(--ovs-primary-dark); color: #fff; transform: translateY(-1px); }}
    div.stButton > button:focus-visible, div[data-testid="stFormSubmitButton"] > button:focus-visible {{ outline: 3px solid color-mix(in srgb, var(--ovs-primary) 35%, transparent); outline-offset: 2px; }}
    [data-testid="stTextInput"] input, [data-testid="stSelectbox"] [data-baseweb="select"] > div {{ background: var(--ovs-surface); border-color: var(--ovs-border); border-radius: var(--ovs-radius-sm); color: var(--ovs-text); }}
    [data-testid="stTextInput"] input:focus, [data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within {{ border-color: var(--ovs-primary); box-shadow: 0 0 0 3px color-mix(in srgb, var(--ovs-primary) 18%, transparent); }}
    [data-testid="stFileUploader"] > section {{ border: 2px dashed var(--ovs-border) !important; border-radius: var(--ovs-radius-md) !important; background: var(--ovs-surface) !important; padding: clamp(18px, 3vw, 28px) !important; }}
    [data-testid="stFileUploader"] > section:hover {{ border-color: var(--ovs-primary) !important; background: var(--ovs-primary-light) !important; }}
    [data-testid="stAlert"] {{ border-radius: var(--ovs-radius-md); }}
    [data-testid="stExpander"] {{ border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-sm); background: var(--ovs-surface); }}
    div[data-testid="stForm"] {{ background: var(--ovs-surface); border: 1px solid var(--ovs-border); border-radius: var(--ovs-radius-md); padding: clamp(16px, 3vw, 24px); }}

    .st-key-selected_role div[data-testid="stRadio"] > div[role="radiogroup"] {{ display: flex !important; width: min(100%, 640px); min-height: 56px; margin: 0 auto; overflow: hidden; gap: 0 !important; border: 2px solid var(--ovs-text); border-radius: var(--ovs-radius-pill); background: var(--ovs-surface); }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] {{ position: relative; display: flex !important; flex: 1 1 50%; width: 50%; min-height: 52px; margin: 0 !important; padding: 0 16px !important; align-items: center !important; justify-content: center !important; background: var(--ovs-surface); cursor: pointer; transition: background-color .2s ease; }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] + label[data-baseweb="radio"] {{ border-left: 1px solid var(--ovs-text); }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] > div:first-child {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap; }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] p {{ margin: 0 !important; color: var(--ovs-text) !important; font-family: 'Noto Sans Thai', sans-serif !important; font-size: clamp(12px, 2.2vw, 16px) !important; font-weight: 700 !important; line-height: 1.35 !important; text-align: center; white-space: nowrap; transition: color .2s ease; }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {{ background: var(--ovs-primary-light); }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {{ background: var(--ovs-primary); }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p {{ color: #fff !important; }}
    .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"]:focus-within {{ outline: 2px solid var(--ovs-primary-dark); outline-offset: -4px; }}

    .ovs-footer {{ margin-top: clamp(40px, 7vw, 72px); padding: 28px 0; border-top: 1px solid var(--ovs-border); color: var(--ovs-text-secondary); font-size: .8rem; text-align: center; }}

    /* Login / onboarding layout */
    .ovs-login-shell {{ display:grid; grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr); gap:clamp(22px,4vw,56px); align-items:center; margin:clamp(18px,4vw,48px) 0 22px; }}
    .ovs-login-visual {{ min-height:350px; padding:clamp(24px,4vw,52px); border-radius:28px; background:linear-gradient(140deg,var(--ovs-primary-light),var(--ovs-surface)); border:1px solid var(--ovs-border); display:flex; flex-direction:column; justify-content:center; overflow:hidden; }}
    .ovs-login-kicker {{ font-size:.72rem; letter-spacing:.14em; font-weight:800; color:var(--ovs-primary); }}
    .ovs-login-visual h1 {{ color:var(--ovs-text); font-size:clamp(1.8rem,3.2vw,3rem); line-height:1.18; letter-spacing:-.035em; margin:22px 0 14px; }}
    .ovs-login-visual p {{ color:var(--ovs-text-secondary); max-width:38rem; font-size:1rem; line-height:1.8; }}
    .ovs-login-visual-note {{ margin-top:34px; color:var(--ovs-text-secondary); font-size:.68rem; letter-spacing:.08em; font-weight:700; }}
    .ovs-login-form-intro {{ padding:8px 0 2px; }}
    .ovs-atlas-nav-heading {{ margin:24px 0 12px; }}
    .ovs-atlas-current {{ display:flex; gap:16px; align-items:flex-start; margin:18px 0 26px; padding:18px 20px; background:var(--ovs-surface); border:1px solid var(--ovs-border); border-radius:18px; }}
    .ovs-atlas-current__index {{ display:flex; flex:0 0 44px; width:44px; height:44px; align-items:center; justify-content:center; border-radius:14px; color:var(--ovs-primary-dark); background:var(--ovs-primary-light); font-weight:800; }}
    .ovs-atlas-current h3 {{ margin:0 0 4px; color:var(--ovs-text); font-size:1.2rem; }}
    .ovs-atlas-current p {{ margin:0; color:var(--ovs-text-secondary); line-height:1.6; }}
    .st-key-atlas_topic_selector [role="radiogroup"] {{ display:flex; flex-wrap:wrap; gap:8px; }}
    .st-key-atlas_topic_selector [role="radiogroup"] label {{ border:1px solid var(--ovs-border); border-radius:999px; padding:8px 14px; background:var(--ovs-surface); }}
    .st-key-atlas_topic_selector [role="radiogroup"] label:has(input:checked) {{ background:var(--ovs-primary-light); border-color:var(--ovs-primary); }}

    @media (max-width: 991px) {{ .ovs-theme-row {{ margin: -2px 0 18px; }} .ovs-nav {{ align-items: flex-start; }} }}
    @media (max-width: 575px) {{
        .main .block-container {{ padding-inline: 16px !important; }}
        .ovs-nav {{ display: block; }} .ovs-nav__links {{ justify-content: flex-start; margin-top: 10px; }}
        .ovs-nav__link {{ padding: 6px 8px; font-size: .76rem; }}
        .ovs-theme-row {{ justify-content: flex-start; }}
        [data-testid="stHorizontalBlock"] {{ flex-wrap: wrap; }}
        [data-testid="stHorizontalBlock"] > [data-testid="column"] {{ min-width: 100% !important; }}
        .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] {{ min-height: 48px; padding: 0 8px !important; }}
        .st-key-selected_role div[data-testid="stRadio"] label[data-baseweb="radio"] p {{ font-size: 12px !important; }}
        .ovs-atlas-hero {{ grid-template-columns: 1fr; }}
        .ovs-atlas-header {{ grid-template-columns: 1fr; }}
        .ovs-atlas-visual {{ min-height: 180px; }}
        .ovs-atlas-flow {{ grid-template-columns: 1fr; }}
        .ovs-atlas-content {{ grid-template-columns: 1fr; }}
        .ovs-atlas-timeline {{ grid-template-columns: 1fr; }}
        [class*="st-key-atlas_topic_"] > div > button {{ min-height: 104px; }}
    }}
    </style>
    """, unsafe_allow_html=True)


def navbar(active_page: str = "home") -> None:
    labels = {"home": "Home", "ai": "AI Detection", "knowledge": "Knowledge", "about": "About"}
    links = "".join(
        f'<span class="ovs-nav__link {"ovs-nav__link--active" if page == active_page else ""}">{label}</span>'
        for page, label in labels.items()
    )
    st.markdown(f"""
    <nav class="ovs-nav" aria-label="OvaSight navigation">
        <div class="ovs-nav__brand"><span class="ovs-nav__brand-mark">●</span>OvaSight</div>
        <div class="ovs-nav__links">{links}</div>
    </nav>
    """, unsafe_allow_html=True)
    _, theme_column = st.columns([0.82, 0.18])
    with theme_column:
        st.selectbox("Appearance theme", list(THEMES), key="theme", format_func=lambda name: THEMES[name]["label"], label_visibility="collapsed")


def footer() -> None:
    st.markdown('<footer class="ovs-footer">OvaSight · AI-assisted microscopy screening · For preliminary screening support only</footer>', unsafe_allow_html=True)


def render_badge(label: str, kind: str = "info") -> str:
    return f'<span class="ovs-badge ovs-badge--{escape(kind)}">{escape(label)}</span>'


def render_stat_card(label: str, value: str, kind: str = "") -> str:
    modifier = f' ovs-stat__value--{escape(kind)}' if kind else ""
    return f'<div class="ovs-stat"><div class="ovs-stat__label">{escape(label)}</div><div class="ovs-stat__value{modifier}">{escape(value)}</div></div>'
