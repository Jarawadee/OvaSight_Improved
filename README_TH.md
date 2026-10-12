# OvaSight — เวอร์ชันปรับ UI/UX

## ไฟล์
- `app.py`: หน้าเริ่มต้น / onboarding / dashboard
- `styles.py`: design tokens, themes และ responsive styles
- `pages/1_AI_Detection.py`: หน้า AI เดิม (คง logic โมเดลไว้)
- `pages/2_Knowledge.py`: Learning Atlas แบบเลือกหัวข้อแล้วแสดงเฉพาะเนื้อหาหัวข้อนั้น

## วิธีใช้งาน
1. คัดลอกโฟลเดอร์ `OvaSight_Improved` ไปยังเครื่องของคุณ
2. นำไฟล์โมเดล `.keras` ที่ใช้จริงไปวางตำแหน่งตามที่ `pages/1_AI_Detection.py` ระบุ (ตรวจ `MODEL_PATH` ก่อนรัน)
3. ติดตั้ง dependencies: `pip install -r requirements.txt`
4. รัน: `streamlit run app.py`

## หมายเหตุเรื่อง Login
หน้าที่ให้มาปรับเป็น onboarding/access screen ที่ดูเป็นระบบมากขึ้น แต่ยังไม่ใช่ระบบ authentication จริง เพราะโปรเจกต์เดิมใช้การเลือกบทบาทและกรอกชื่อใน session state เท่านั้น อย่าใช้เป็นระบบควบคุมสิทธิ์จริงหรือเก็บข้อมูลผู้ป่วยจนกว่าจะเพิ่มระบบบัญชี, password hashing, session security และ authorization ที่เหมาะสม
