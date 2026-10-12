import streamlit as st

from styles import footer, inject_css, navbar, render_badge


st.set_page_config(page_title="OvaSight — Learning Atlas", page_icon="◉", layout="wide", initial_sidebar_state="collapsed")
inject_css()
navbar("knowledge")


TOPICS = {
    "overview": {"label": "Overview", "title": "รู้จักพยาธิเข็มหมุด", "short": "ข้อมูลพื้นฐานและสิ่งสำคัญที่ควรรู้"},
    "symptoms": {"label": "Symptoms", "title": "อาการที่ควรรู้", "short": "สังเกตอาการและปัจจัยที่ควรติดตาม"},
    "transmission": {"label": "Transmission", "title": "การแพร่เชื้อ", "short": "เข้าใจวงจรเพื่อช่วยตัดการแพร่เชื้อ"},
    "prevention": {"label": "Prevention", "title": "การป้องกัน", "short": "กิจวัตรเล็ก ๆ ที่ช่วยลดการติดซ้ำ"},
    "tape_test": {"label": "Tape Test", "title": "รู้จัก Tape Test", "short": "ภาพรวมการเตรียมตัวและการเก็บตัวอย่าง"},
    "care": {"label": "When to seek care", "title": "เมื่อไหร่ควรปรึกษาผู้เชี่ยวชาญ", "short": "แนวทางตัดสินใจอย่างระมัดระวัง"},
    "faq": {"label": "FAQ", "title": "คำถามที่พบบ่อย", "short": "คำตอบสั้น กระชับ และอ่านต่อได้"},
}


def set_active_topic(topic: str) -> None:
    st.session_state.atlas_active_topic = topic


def render_topic_button(topic: str, number: int) -> None:
    item = TOPICS[topic]
    if st.button(f"{number:02d}\n{item['title']}\n{item['short']}", key=f"atlas_topic_{topic}", use_container_width=True):
        set_active_topic(topic)


def render_atlas_hero(is_medical: bool) -> None:
    audience_note = "เน้น microscopy, specimen workflow และ AI-assisted screening" if is_medical else "เน้นอาการ การป้องกัน และการเตรียมตัวอย่างปลอดภัย"
    st.markdown(f"""
    <section class="ovs-hero ovs-hero--accent ovs-atlas-hero">
      <div>
        <span class="ovs-hero__badge">OvaSight · Learning Atlas</span>
        <h1 class="ovs-hero__title">รู้จักพยาธิเข็มหมุด</h1>
        <p class="ovs-hero__copy">เรียนรู้เกี่ยวกับพยาธิเข็มหมุดผ่านข้อมูลที่เข้าใจง่าย เลือกสำรวจหัวข้อที่สนใจ แล้วเปิดอ่านรายละเอียดเมื่อพร้อม</p>
        <div style="margin-top:18px;">{render_badge(audience_note, "info")}</div>
      </div>
      <div class="ovs-atlas-visual" role="img" aria-label="Abstract scientific visual for the OvaSight Learning Atlas, not a clinical microscopy image">
        <span class="ovs-atlas-visual__dot"></span>
        <span class="ovs-atlas-visual__label">Abstract scientific visual · not a clinical image</span>
      </div>
    </section>
    """, unsafe_allow_html=True)


def render_explorer(active_topic: str, preferred_topics: list[str]) -> None:
    """Single, compact topic navigator. Content is rendered separately below."""
    st.markdown('<div class="ovs-atlas-nav-heading"><div class="ovs-eyebrow">LEARNING ATLAS</div><h2 class="ovs-section-title">คุณอยากเรียนรู้เรื่องไหน?</h2><p class="ovs-card__copy">เลือกหัวข้อเพื่อดูเฉพาะข้อมูลที่ต้องการ ไม่จำเป็นต้องเลื่อนอ่านทั้งหน้า</p></div>', unsafe_allow_html=True)
    labels = list(TOPICS.keys())
    current = st.session_state.atlas_active_topic
    # Native Streamlit control is reliable on desktop and mobile; CSS gives it the shared theme.
    selected = st.radio(
        "หัวข้อใน Atlas",
        options=labels,
        index=labels.index(current) if current in labels else 0,
        format_func=lambda key: TOPICS[key]["label"],
        key="atlas_topic_selector",
        horizontal=True,
        label_visibility="collapsed",
    )
    if selected != st.session_state.atlas_active_topic:
        st.session_state.atlas_active_topic = selected
        st.rerun()
    item = TOPICS[st.session_state.atlas_active_topic]
    current_num = labels.index(st.session_state.atlas_active_topic) + 1
    st.markdown(f"<div class='ovs-atlas-current'><span class='ovs-atlas-current__index'>{current_num:02d}</span><div><div class='ovs-eyebrow'>SELECTED TOPIC</div><h3>{item['title']}</h3><p>{item['short']}</p></div></div>", unsafe_allow_html=True)


def render_basics() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Quick facts</div><h2 class="ovs-section-title">พยาธิเข็มหมุดคืออะไร?</h2></div>', unsafe_allow_html=True)
    facts = [
        ("ชื่อที่พบ", "เส้นเล็ก ๆ สีขาว อาจพบรอบทวารหนัก ชุดนอน หรือผ้าปูที่นอน โดยมักสังเกตได้ตอนกลางคืน"),
        ("อาการสำคัญ", "คันรอบทวารหนักตอนกลางคืน นอนกระสับกระส่าย และบางคนอาจไม่มีอาการ"),
        ("การแพร่เชื้อ", "ไข่ติดมือและเล็บ แล้วอาจเข้าสู่ปากผ่านมือ อาหาร ของเล่น หรือสิ่งของ"),
    ]
    for column, (title, copy) in zip(st.columns(3), facts):
        with column:
            st.markdown(f'<article class="ovs-card ovs-feature"><div class="ovs-feature__icon">●</div><h3 class="ovs-card__title">{title}</h3><p class="ovs-card__copy">{copy}</p></article>', unsafe_allow_html=True)

    with st.expander("อ่านเพิ่มเติม: วงจรการติดเชื้อและจุดตัดวงจร"):
        cycle_col, break_col = st.columns(2)
        with cycle_col:
            st.markdown("""
            **วงจรการติดเชื้อ**

            1. กลืนไข่ผ่านปากเข้าสู่ลำไส้
            2. พยาธิเติบโตในลำไส้เป็นเวลา 4–6 สัปดาห์
            3. ตัวเมียวางไข่รอบทวารหนักตอนกลางคืน
            4. การเกาทำให้ไข่ติดมือ เล็บ ผ้า และสิ่งของร่วม
            5. ไข่อาจกลับเข้าปากผ่านมือ อาหาร ของเล่น หรือสิ่งของ
            """)
        with break_col:
            st.markdown("""
            **จุดตัดวงจรที่สำคัญ**

            - ล้างมือให้สะอาดก่อนอาหารและหลังเข้าห้องน้ำ
            - ตัดเล็บให้สั้นและสะอาด
            - ลดการสัมผัสมือกับหน้าและปาก
            - ซักผ้าบ่อยขึ้น โดยใช้น้ำร้อนเมื่อเหมาะสม
            - ปฏิบัติตามแผนการดูแลจากบุคลากรสุขภาพ
            """)


def render_microscopy() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Microscopy context</div><h2 class="ovs-section-title">สิ่งที่ AI กำลังมองหา</h2></div>', unsafe_allow_html=True)
    left, right = st.columns([0.9, 1.1])
    with left:
        st.markdown("""
        <div class="ovs-atlas-visual" role="img" aria-label="Abstract microscopy-inspired visual, not a clinical microscopy image">
          <span class="ovs-atlas-visual__dot"></span>
          <span class="ovs-atlas-visual__label">AI-assisted screening context · not a clinical image</span>
        </div>
        """, unsafe_allow_html=True)
    with right:
        st.markdown("""
        <article class="ovs-card ovs-card--info">
          <h3 class="ovs-card__title">AI-assisted image screening</h3>
          <p class="ovs-card__copy">ในพื้นที่ AI Detection ของ OvaSight ระบบวิเคราะห์ภาพ microscopy เพื่อทำเครื่องหมายบริเวณที่สงสัยของ <i>Enterobius vermicularis</i> สำหรับการคัดกรองเบื้องต้น</p>
        </article>
        """, unsafe_allow_html=True)
        with st.expander("อ่านข้อควรทราบสำหรับการทบทวนภาพ"):
            st.markdown("ผลจาก AI มีวัตถุประสงค์เพื่อสนับสนุนการคัดกรองเบื้องต้น ควรทบทวนร่วมกับภาพต้นฉบับ และไม่ทดแทนการยืนยันจากห้องปฏิบัติการหรือดุลยพินิจทางคลินิก")


def render_symptoms_and_check() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Symptoms</div><h2 class="ovs-section-title">อาการที่ควรรู้</h2></div>', unsafe_allow_html=True)
    symptoms = [
        ("คันตอนกลางคืน", "อาการคันรอบทวารหนักมักสังเกตได้ตอนกลางคืน"),
        ("การนอนถูกรบกวน", "อาจนอนกระสับกระส่าย ตื่นบ่อย หรือหงุดหงิดตอนกลางคืน"),
        ("รอยแดงหรือรอยเกา", "ผิวหนังรอบทวารหนักอาจแดง แสบ หรือมีรอยเกาได้"),
    ]
    for column, (title, copy) in zip(st.columns(3), symptoms):
        with column:
            st.markdown(f'<article class="ovs-card"><h3 class="ovs-card__title">{title}</h3><p class="ovs-card__copy">{copy}</p></article>', unsafe_allow_html=True)

    st.info("บางคนอาจไม่มีอาการ ข้อมูลนี้ใช้เพื่อการศึกษา ไม่ใช่ผลวินิจฉัย")
    with st.expander("สำรวจอาการเบื้องต้น (ใช้เวลา 2–3 นาที)"):
        with st.form("quick_symptom_check"):
            st.markdown('<div class="ovs-eyebrow" style="margin:0 0 12px;">อาการที่สังเกตได้</div>', unsafe_allow_html=True)
            col_q1, col_q2 = st.columns(2)
            with col_q1:
                itch = st.radio("มีอาการคันรอบทวารหนักตอนกลางคืน?", ["ไม่มี", "บางครั้ง", "บ่อยมาก"])
                sleep = st.radio("มีอาการนอนกระสับกระส่าย ตื่นบ่อย หรือหงุดหงิดตอนกลางคืน?", ["ไม่มี", "บางครั้ง", "บ่อย"])
            with col_q2:
                skin = st.radio("ผิวหนังรอบทวารหนักแดง แสบ หรือมีรอยเกาจนถลอก?", ["ไม่มี", "เล็กน้อย", "ชัดเจน/ต่อเนื่อง"])
            seen = st.radio("เคยเห็นเส้นสีขาวรอบทวารหนัก/ชุดนอนหรือ?", ["ไม่เคย", "ไม่แน่ใจ", "เห็นชัด"])
            st.markdown('<div class="ovs-eyebrow" style="margin:18px 0 12px;">ความเสี่ยงจากคนใกล้ชิดและพฤติกรรม</div>', unsafe_allow_html=True)
            col_q3, col_q4 = st.columns(2)
            with col_q3:
                contact = st.radio("มีคนใกล้ชิดมีอาการคล้ายกันหรือ?", ["ไม่มี/ไม่ทราบ", "สงสัย", "มีแน่"])
                duration = st.radio("อาการคันหรือรบกวนการนอนต่อเนื่องนานเท่าไร?", ["ไม่มีอาการ", "น้อยกว่า 1 สัปดาห์", "1 สัปดาห์ขึ้นไป"])
            with col_q4:
                hand_mouth = st.radio("เด็กเอานิ้วเข้าปาก กัดเล็บ หรืออมของเล่นเป็นประจำ?", ["ไม่เป็น", "เป็นบางครั้ง", "เป็นประจำ"])
                nails = st.radio("เล็บมือยาวหรือมีสิ่งสกปรกใต้เล็บบ่อย?", ["ไม่", "เป็นบางครั้ง", "เป็นบ่อย"])
            submitted = st.form_submit_button("ดูคำแนะนำ", use_container_width=True)

        if submitted:
            score = 0
            score += {"ไม่มี": 0, "บางครั้ง": 1, "บ่อยมาก": 3}[itch]
            score += {"ไม่มี": 0, "บางครั้ง": 1, "บ่อย": 2}[sleep]
            score += {"ไม่มี": 0, "เล็กน้อย": 1, "ชัดเจน/ต่อเนื่อง": 2}[skin]
            score += {"ไม่เคย": 0, "ไม่แน่ใจ": 2, "เห็นชัด": 4}[seen]
            score += {"ไม่มี/ไม่ทราบ": 0, "สงสัย": 1, "มีแน่": 2}[contact]
            score += {"ไม่มีอาการ": 0, "น้อยกว่า 1 สัปดาห์": 1, "1 สัปดาห์ขึ้นไป": 2}[duration]
            score += {"ไม่เป็น": 0, "เป็นบางครั้ง": 1, "เป็นประจำ": 1}[hand_mouth]
            score += {"ไม่": 0, "เป็นบางครั้ง": 1, "เป็นบ่อย": 1}[nails]
            st.markdown(f'<div class="ovs-card ovs-card--info"><strong>สรุปคำตอบ</strong><br>มีปัจจัยที่ควรติดตาม {score} จาก 17 คะแนน</div>', unsafe_allow_html=True)
            if seen == "เห็นชัด" or score >= 7:
                st.warning("แนะนำให้ปรึกษาแพทย์หรือบุคลากรสุขภาพ เพื่อประเมินและรับคำแนะนำเรื่องการเก็บตัวอย่างหรือการรักษา โดยเฉพาะเมื่ออาการรบกวนการนอนหรือมีผิวหนังอักเสบ")
            elif score >= 3:
                st.info("เฝ้าสังเกตอาการต่อไป เน้นล้างมือ ตัดเล็บ และลดการเอามือเข้าปาก หากอาการต่อเนื่องหรือกังวล ควรปรึกษาบุคลากรสุขภาพ")
            else:
                st.success("ยังไม่พบสัญญาณเด่น รักษาสุขอนามัยมือและเล็บให้ดีต่อไป และสังเกตอาการหากมีการเปลี่ยนแปลง")


def render_transmission_and_prevention() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Transmission</div><h2 class="ovs-section-title">การแพร่เชื้อเกิดขึ้นได้อย่างไร?</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="ovs-atlas-flow">
      <div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">01</span>ไข่ติดมือและเล็บ</div>
      <div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">02</span>สัมผัสผ้าหรือสิ่งของร่วม</div>
      <div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">03</span>มือสัมผัสปากหรืออาหาร</div>
      <div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">04</span>ไข่เข้าสู่ร่างกาย</div>
      <div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">05</span>อาจแพร่สู่คนใกล้ชิด</div>
    </div>
    """, unsafe_allow_html=True)



def render_prevention() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Prevention</div><h2 class="ovs-section-title">ป้องกันอย่างไร?</h2></div>', unsafe_allow_html=True)
    prevention = [
        ("01", "ล้างมือให้สะอาด", "หลังเข้าห้องน้ำ หลังเปลี่ยนผ้าอ้อม และก่อนจับอาหาร ใช้สบู่กับน้ำ 20 วินาที"),
        ("02", "ดูแลเล็บ", "ตัดเล็บให้สั้น ขัดใต้เล็บให้สะอาด และชวนเด็กไม่กัดเล็บหรือเอานิ้วเข้าปาก"),
        ("03", "ดูแลผ้าและสิ่งแวดล้อม", "อาบน้ำตอนเช้า เปลี่ยนชุดนอน ผ้าขนหนู และผ้าปูที่นอนให้เหมาะสม"),
    ]
    for column, (number, title, copy) in zip(st.columns(3), prevention):
        with column:
            st.markdown(f'<article class="ovs-card ovs-atlas-step"><div class="ovs-atlas-step__number">{number}</div><h3 class="ovs-card__title">{title}</h3><p class="ovs-card__copy">{copy}</p></article>', unsafe_allow_html=True)


def render_tape_test() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Tape test</div><h2 class="ovs-section-title">รู้จัก Tape Test</h2></div>', unsafe_allow_html=True)
    st.info("ทำตามคำแนะนำของหน่วยตรวจประเมินเป็นหลัก ส่วนนี้เป็นคู่มือประกอบเพื่อเตรียมตัว")
    steps = [
        ("01", "เวลา", "เก็บตัวอย่างเป็นสิ่งแรกหลังตื่นนอน ก่อนอาบน้ำหรือใช้ห้องน้ำ"),
        ("02", "เทปใส", "ใช้ด้านกาว กดเบา ๆ บนผิวรอบทวารหนักเพื่อเก็บไข่"),
        ("03", "ทำต่อเนื่อง", "ทำ 3 เช้าติดต่อกัน เพื่อเพิ่มโอกาสพบไข่"),
        ("04", "ปิดผนึก", "เก็บเทปในภาชนะปิดตามคำแนะนำ และล้างมือให้ทั่วถึง"),
    ]
    for column, (number, title, copy) in zip(st.columns(4), steps):
        with column:
            st.markdown(f'<article class="ovs-card ovs-atlas-step"><div class="ovs-atlas-step__number">{number}</div><h3 class="ovs-card__title">{title}</h3><p class="ovs-card__copy">{copy}</p></article>', unsafe_allow_html=True)
    st.warning("อย่าสัมผัสใบหน้าระหว่างเก็บตัวอย่าง และใช้ชุดตัวอย่างจากหน่วยตรวจเมื่อมี")


def render_care_and_scenarios() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Care guidance</div><h2 class="ovs-section-title">เมื่อไหร่ควรปรึกษาบุคลากรทางการแพทย์?</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <article class="ovs-card ovs-card--warning">
      <h3 class="ovs-card__title">ควรขอคำแนะนำเพิ่มเติมเมื่อ</h3>
      <p class="ovs-card__copy">เห็นเส้นสีขาวชัดเจน มีอาการคันหรือรบกวนการนอนต่อเนื่อง มีผิวหนังอักเสบ หรือมีข้อกังวลเกี่ยวกับการเก็บตัวอย่างและการดูแล</p>
    </article>
    """, unsafe_allow_html=True)
    with st.expander("สำหรับผู้ปกครอง: การดูแลที่บ้าน"):
        parent_col, check_col = st.columns(2)
        with parent_col:
            st.markdown("""
            **วิธีพูดคุยกับเด็ก**

            “เชื้อเกาะมือได้ง่าย และถูกเด็กจำนวนมากด้วย เราจะช่วยกันล้างมือ ตัดเล็บ เปลี่ยนผ้า และกินยา เพื่อให้เชื้อออกไป”

            **3 ภารกิจหลัก**

            1. ล้างมือให้สะอาด
            2. ตัดและขัดเล็บ
            3. เปลี่ยนผ้าและซักบ่อย
            """)
        with check_col:
            st.markdown("**เช็กลิสต์ลดการติดซ้ำ**")
            checks = ["ทุกคนในบ้านล้างมือก่อนอาหาร", "เปลี่ยนชุดนอนและผ้าขนหนูบ่อย ๆ", "ซักด้วยน้ำร้อนถ้าเป็นไปได้", "ไม่ใช้ผ้าร่วมกัน", "เก็บเล็บให้สั้นทั้งบ้าน", "ตามแผนยาครบตามแพทย์สั่ง"]
            checked_count = sum(st.checkbox(item, key=f"parent_check_{idx}") for idx, item in enumerate(checks))
            st.progress(checked_count / len(checks), text=f"ทำแล้ว {checked_count}/{len(checks)}")
        st.markdown("**เรื่องยาที่ต้องรู้** · ยาเพื่อจำลองตัวพยาธิ แต่ไม่ทำลายไข่ มักให้ยาซ้ำหลังจากนั้น 1–2 สัปดาห์ และผู้ติดเชื้อหรือผู้ใกล้ชิดควรรับการประเมินโดยบุคลากรสุขภาพ")
    with st.expander("สำหรับครูอนามัย: การตอบสนองในโรงเรียน"):
        teacher_col, message_col = st.columns(2)
        with teacher_col:
            st.markdown("""
            **เมื่อได้รับแจ้ง**

            1. บันทึกข้อมูลส่วนตัวโดยไม่ระบุต่อสาธารณชน
            2. แจ้งผู้ปกครองเป็นการส่วนตัว ให้ปรึกษาบุคลากรสุขภาพ
            3. เน้นสุขอนามัยทั่วห้องเรียน ล้างมือและตัดเล็บ
            4. ทำความสะอาดพื้นผิวสัมผัส ของเล่น และห้องน้ำ
            """)
        with message_col:
            st.markdown('> “โรงเรียนแนะนำให้เด็กทุกคนล้างมือดี ๆ ตัดเล็บให้สั้น และหลีกเลี่ยงแบ่งของใช้ส่วนตัว หากบุตรหลานมีอาการคันตอนกลางคืน โปรดปรึกษาแพทย์เพื่อประเมินเพิ่มเติม”')
        st.warning("หลีกเลี่ยงการคัดกรอง ตรวจร่างกาย หรือให้ยาโดยไม่มีระบบอนุญาตและแนวทางของสถานศึกษา/บุคลากรสุขภาพ")
        st.markdown("**กิจกรรมห้องเรียน 10 นาที**\n\n| เวลา | กิจกรรม |\n|---|---|\n| นาที 1–2 | ถาม ‘มือสะอาด’ ใช้ทำอะไรได้บ้าง |\n| นาที 3–6 | ฝึกล้างมือ 5 ช่วง |\n| นาที 7–8 | สาธิตการใช้กระดาษทิชชู |\n| นาที 9–10 | ให้เด็กเลือก 1 ภารกิจกลับบ้านทำ |")


def render_faq_and_more() -> None:
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">FAQ</div><h2 class="ovs-section-title">คำถามที่พบบ่อย</h2></div>', unsafe_allow_html=True)
    faq_items = [
        ("จะร้ายแรงไหม?", "โดยทั่วไปไม่เป็นอันตรายถึงชีวิต แต่อาจรบกวนการนอนและการเรียน การรักษาอย่างถูกวิธีและการป้องกันเป็นหลัก"),
        ("ใช้เวลาหายนานไหม?", "พยาธิเติบโตเป็นตัวเต็มวัยใน 4–6 สัปดาห์ ยามักให้ซ้ำ 1–2 สัปดาห์หลังจากนั้น สุขอนามัยที่ดีช่วยลดการติดซ้ำ"),
        ("สบู่ชนิดไหนดี?", "สบู่เหลวหรือบาร์ล้างไข่ได้เท่า ๆ กัน สิ่งสำคัญคือล้างให้ทั่วซอกนิ้วและใต้เล็บ"),
        ("ทั้งบ้านต้องรับยาหรือ?", "ผู้ติดเชื้อและผู้ใกล้ชิดควรรับการประเมินจากแพทย์ ว่าจำเป็นต้องให้ยาหรือไม่"),
        ("ไข่จะตายในความร้อนไหม?", "น้ำร้อน การอบแดด และเครื่องอบแห้งช่วยทำลายไข่ได้"),
        ("ต้องทำความสะอาดเก้าอี้หรือของเล่นบ่อยไหม?", "สำคัญสำหรับสิ่งที่สัมผัสบ่อย โดยเฉพาะที่จับและของเล่น"),
    ]
    for question, answer in faq_items:
        with st.expander(question):
            st.markdown(answer)

    more_col, glossary_col = st.columns(2)
    with more_col:
        with st.expander("โภชนาการและสุขภาพ"):
            st.markdown("ไม่มีอาหาร ‘พิเศษ’ ที่ฆ่าพยาธิ แต่สุขภาพที่ดีช่วยให้ร่างกายต้านทานได้ ควรล้างผักและผลไม้ ใช้น้ำสะอาด เตรียมอาหารด้วยมือสะอาด และระวังอาหารดิบที่ไม่แน่ใจ")
        with st.expander("ด้านใจและการสื่อสาร"):
            st.markdown("เด็กบางคนอาจรู้สึกอายหรือกังวล ควรสื่อสารว่าเชื้อเกาะมือได้ง่าย เด็กไม่ได้ทำอะไรผิด และช่วยกันดูแลโดยไม่ทำให้เด็กรู้สึกแตกต่าง")
    with glossary_col:
        st.markdown("""
        <article class="ovs-card">
          <h3 class="ovs-card__title">คำศัพท์ที่ควรรู้</h3>
          <p class="ovs-card__copy"><strong>Enterobius vermicularis</strong> · ชื่อวิทยาศาสตร์ที่กล่าวถึงใน OvaSight<br><strong>Microscopy</strong> · การดูภาพผ่านกล้องจุลทรรศน์<br><strong>Tape Test</strong> · การเก็บตัวอย่างด้วยเทปใส</p>
        </article>
        """, unsafe_allow_html=True)

    with st.expander("References"):
        st.markdown("- WHO\n- CDC\n- แนวทางการสาธารณสุขจากหน่วยงานต่างประเทศ\n\nรายการอ้างอิงนี้คงตามหน้า Learning Atlas เดิม และไม่มีการเพิ่ม URL หรือ citation ใหม่")


profile = st.session_state.get("user_profile") or {}
is_medical = bool(profile.get("is_medical")) or st.session_state.get("selected_role") == "medical"
priority_topics = ["overview", "symptoms", "prevention", "tape_test", "care", "transmission", "faq"]
if is_medical:
    priority_topics = ["overview", "tape_test", "transmission", "symptoms", "prevention", "care", "faq"]
if "atlas_active_topic" not in st.session_state:
    st.session_state.atlas_active_topic = priority_topics[0]
if st.session_state.atlas_active_topic not in TOPICS:
    st.session_state.atlas_active_topic = priority_topics[0]

st.markdown('<main class="ovs-page ovs-atlas">', unsafe_allow_html=True)
if st.button("กลับหน้าหลัก", key="back_home_know"):
    st.switch_page("app.py")

render_atlas_hero(is_medical)
render_explorer(st.session_state.atlas_active_topic, priority_topics)
active_topic = st.session_state.atlas_active_topic

if active_topic == "overview":
    render_basics()
    render_microscopy()
elif active_topic == "symptoms":
    render_symptoms_and_check()
elif active_topic == "transmission":
    # Render only the transmission portion of the existing combined function.
    st.markdown('<div class="ovs-section-break"><div class="ovs-eyebrow">Transmission</div><h2 class="ovs-section-title">การแพร่เชื้อเกิดขึ้นได้อย่างไร?</h2></div>', unsafe_allow_html=True)
    st.markdown("""<div class="ovs-atlas-flow"><div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">01</span>ไข่ติดมือและเล็บ</div><div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">02</span>สัมผัสผ้าหรือสิ่งของร่วม</div><div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">03</span>มือสัมผัสปากหรืออาหาร</div><div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">04</span>ไข่เข้าสู่ร่างกาย</div><div class="ovs-atlas-flow__item"><span class="ovs-atlas-flow__num">05</span>อาจแพร่สู่คนใกล้ชิด</div></div>""", unsafe_allow_html=True)
elif active_topic == "prevention":
    render_prevention()
elif active_topic == "tape_test":
    render_tape_test()
elif active_topic == "care":
    render_care_and_scenarios()
elif active_topic == "faq":
    render_faq_and_more()

st.markdown("""
<aside class="ovs-card ovs-card--info" style="margin-top:32px;">
  <h2 class="ovs-card__title">Educational information only</h2>
  <p class="ovs-card__copy">ข้อมูลในหน้านี้มีวัตถุประสงค์เพื่อการศึกษา ไม่ใช้แทนการวินิจฉัยหรือคำแนะนำจากบุคลากรทางการแพทย์</p>
</aside>
</main>
""", unsafe_allow_html=True)
footer()
