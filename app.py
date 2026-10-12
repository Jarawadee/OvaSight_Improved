import pandas as pd
import plotly.express as px
import streamlit as st

from styles import footer, get_theme, inject_css, navbar, render_badge, render_stat_card


st.set_page_config(
    page_title="OvaSight — AI-assisted screening",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css()
navbar("home")

if "user_profile" not in st.session_state:
    st.session_state.user_profile = None
if "access_error" not in st.session_state:
    st.session_state.access_error = None
if "selected_role" not in st.session_state:
    st.session_state.selected_role = "general"


def render_onboarding() -> None:
    st.markdown("""
    <section class="ovs-login-shell">
      <div class="ovs-login-visual">
        <span class="ovs-login-kicker">OVASIGHT · SMART MICROSCOPY</span>
        <h1>มองเห็นรายละเอียด<br>เพื่อการคัดกรองที่ดีขึ้น</h1>
        <p>พื้นที่ทำงานสำหรับการเรียนรู้และ AI-assisted screening จากภาพ microscopy</p>
        <div class="ovs-login-visual-note">PRELIMINARY SCREENING · NOT A CONFIRMED DIAGNOSIS</div>
      </div>
      <div class="ovs-login-form-intro">
        <span class="ovs-eyebrow">WELCOME TO OVASIGHT</span>
        <h2 class="ovs-section-title">เริ่มต้นใช้งาน</h2>
        <p class="ovs-card__copy">เลือกประเภทผู้ใช้งานเพื่อจัดมุมมองให้เหมาะกับคุณ</p>
      </div>
    </section>
    """, unsafe_allow_html=True)

    selected_role = st.radio(
        "เลือกประเภทผู้ใช้งาน",
        options=("general", "medical"),
        format_func=lambda role: "บุคคลทั่วไป" if role == "general" else "บุคลากรทางการแพทย์",
        key="selected_role",
        horizontal=True,
        label_visibility="visible",
    )

    if selected_role == "medical":
        role_summary = "สำหรับสายการแพทย์ · เลือกบทบาทย่อยเพื่อเข้าถึงพื้นที่ AI-assisted screening หรือเนื้อหาการเรียนรู้"
        occupation_options = [
            "บุคลากรทางการแพทย์ / นักเทคนิคการแพทย์",
            "นักศึกษาสาขาแพทยศาสตร์ / สาธารณสุข",
        ]
    else:
        role_summary = "สำหรับบุคคลทั่วไป · เรียนรู้เรื่องพยาธิเข็มหมุด อาการ การป้องกัน และการเก็บตัวอย่างอย่างปลอดภัย"
        occupation_options = [
            "ประชาชนทั่วไป", "ผู้ปกครอง", "เด็ก / นักเรียน", "ครูอนามัย / ครูผู้ดูแลนักเรียน",
        ]

    st.markdown(f'<div class="ovs-card ovs-card--info" style="margin:18px 0 24px;">{role_summary}</div>', unsafe_allow_html=True)
    with st.form("onboarding_form", border=True):
        st.markdown("**ข้อมูลผู้ใช้งาน**")
        fullname = st.text_input("ชื่อที่ต้องการให้แสดง", placeholder="กรอกชื่อหรือชื่อเรียก", max_chars=80)
        occupation = st.selectbox("บทบาทของคุณ", occupation_options)
        disclaimer_agree = st.checkbox("ฉันเข้าใจว่าผลจาก AI เป็นการสนับสนุนการคัดกรองเบื้องต้น ไม่ใช่ผลยืนยันทางห้องปฏิบัติการ")
        submit_reg = st.form_submit_button("เข้าสู่ OvaSight  →", use_container_width=True, type="primary")
        if submit_reg:
            if not fullname.strip():
                st.warning("กรุณากรอกชื่อ-นามสกุลก่อนทำรายการ")
            elif not disclaimer_agree:
                st.warning("กรุณายอมรับข้อตกลงการใช้งานก่อนเข้าสู่ระบบ")
            else:
                st.session_state.user_profile = {
                    "name": fullname.strip(),
                    "occupation": occupation,
                    "is_medical": occupation == "บุคลากรทางการแพทย์ / นักเทคนิคการแพทย์",
                }
                st.session_state.access_error = None
                st.rerun()
    st.caption("Prototype access · การเลือกบทบาทนี้ยังไม่ใช่ระบบยืนยันตัวตนหรือบัญชีผู้ใช้จริง")


def render_dashboard(user: dict) -> None:
    permission = render_badge("AI Detection available", "success") if user["is_medical"] else render_badge("Learning access", "info")
    st.markdown(f"""
    <section class="ovs-hero ovs-hero--accent">
      <span class="ovs-hero__badge">OvaSight workspace</span>
      <h1 class="ovs-hero__title">สวัสดีค่ะ คุณ {user['name']}</h1>
      <p class="ovs-hero__copy">แพลตฟอร์ม AI-assisted screening สำหรับสนับสนุนการทบทวนภาพ microscopy ในกระบวนการคัดกรองเบื้องต้น</p>
      <div class="ovs-hero__meta">
        <div class="ovs-hero__metric"><strong>{user['occupation']}</strong><span>บทบาทผู้ใช้งาน</span></div>
        <div class="ovs-hero__metric"><strong>{permission}</strong><span>สิทธิ์ปัจจุบัน</span></div>
      </div>
    </section>
    """, unsafe_allow_html=True)

    logout_col, _ = st.columns([0.32, 0.68])
    with logout_col:
        if st.button("ออกจากระบบ / เปลี่ยนผู้ใช้", key="btn_logout", use_container_width=True):
            st.session_state.user_profile = None
            st.session_state.access_error = None
            st.rerun()

    st.markdown('<div class="ovs-eyebrow" style="margin-top:30px;">Workspace</div><h2 class="ovs-section-title">เลือกโมดูลการทำงาน</h2>', unsafe_allow_html=True)
    ai_col, knowledge_col = st.columns(2)
    with ai_col:
        st.markdown("""
        <article class="ovs-card ovs-card--highlight">
          <h3 class="ovs-card__title">AI Detection Workspace</h3>
          <p class="ovs-card__copy">อัปโหลดภาพ microscopy เพื่อรับผล AI-assisted screening พร้อมตำแหน่งบริเวณที่ระบบตรวจพบ</p>
        </article>
        """, unsafe_allow_html=True)
        if st.button("เปิด AI Detection", key="btn_go_ai", use_container_width=True):
            if user["is_medical"]:
                st.session_state.access_error = None
                st.switch_page("pages/1_AI_Detection.py")
            else:
                st.session_state.access_error = "AI Detection สงวนสิทธิ์สำหรับบุคลากรทางการแพทย์ / นักเทคนิคการแพทย์ คุณยังใช้งาน Learning Atlas ได้ตามปกติ"
    with knowledge_col:
        st.markdown("""
        <article class="ovs-card">
          <h3 class="ovs-card__title">Learning Atlas</h3>
          <p class="ovs-card__copy">คู่มือสำหรับทำความเข้าใจอาการ การป้องกัน และการเก็บตัวอย่างอย่างปลอดภัย</p>
        </article>
        """, unsafe_allow_html=True)
        if st.button("เปิด Learning Atlas", key="btn_go_know", use_container_width=True):
            st.session_state.access_error = None
            st.switch_page("pages/2_Knowledge.py")

    if st.session_state.access_error:
        st.warning(st.session_state.access_error)

    st.markdown('<div class="ovs-eyebrow" style="margin-top:42px;">Demo data · not clinical data</div><h2 class="ovs-section-title">ภาพรวมการใช้งานตัวอย่าง</h2>', unsafe_allow_html=True)
    stat_values = [
        ("จำนวนการสแกนสะสม", "1,482 ครั้ง", ""),
        ("ตัวอย่างที่ระบบทำเครื่องหมาย", "412 เคส (27.8%)", "danger"),
        ("ความไวของระบบ (demo)", "96.5%", ""),
        ("กลุ่มอายุที่พบใน demo", "4–7 ปี", "warning"),
    ]
    for column, (label, value, kind) in zip(st.columns(4), stat_values):
        with column:
            st.markdown(render_stat_card(label, value, kind), unsafe_allow_html=True)

    chart_col, note_col = st.columns([1.25, 0.75])
    with chart_col:
        insight_data = pd.DataFrame({
            "กลุ่มอายุ": ["3–5 ปี", "6–8 ปี", "9–12 ปี", "13 ปีขึ้นไป"],
            "ตัวอย่างที่ระบบทำเครื่องหมาย": [180, 154, 62, 16],
        })
        theme = get_theme()
        chart = px.bar(
            insight_data, x="กลุ่มอายุ", y="ตัวอย่างที่ระบบทำเครื่องหมาย",
            color_discrete_sequence=[theme["primary"]], title="ข้อมูลจำลอง: ตัวอย่างที่ระบบทำเครื่องหมายตามกลุ่มอายุ",
        )
        chart.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Noto Sans Thai, sans-serif", color=theme["text"]),
            margin=dict(t=50, b=0, l=0, r=0), showlegend=False,
        )
        chart.update_yaxes(gridcolor=theme["chart_grid"])
        st.plotly_chart(chart, use_container_width=True)
    with note_col:
        st.markdown("""
        <aside class="ovs-card ovs-card--info">
          <h3 class="ovs-card__title">เกี่ยวกับข้อมูลตัวอย่าง</h3>
          <p class="ovs-card__copy">ตัวเลขทั้งหมดในส่วนนี้ใช้เพื่อสาธิต UI เท่านั้น ไม่ใช่ผลการประเมินทางคลินิกหรืออัตราประสิทธิภาพที่ผ่านการยืนยัน</p>
        </aside>
        """, unsafe_allow_html=True)


st.markdown('<main class="ovs-page">', unsafe_allow_html=True)
if st.session_state.user_profile is None:
    render_onboarding()
else:
    render_dashboard(st.session_state.user_profile)
st.markdown('</main>', unsafe_allow_html=True)
footer()
