# AGENT ASYLUM (สถานบำบัดเอเจนท์)

**"คลังรวบรวมเหตุการณ์ความล้มเหลวที่ซับซ้อน, สภาวะ Deadlock, และพฤติกรรมที่ไม่คาดคิดของ AI Agent แบบอัตโนมัติ"**

<p align="center">
    <a href="../README.md">English</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-TH.md">ภาษาไทย</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-JA.md">日本語</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-KO.md">한국어</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="README-ZH.md">简体中文</a>
</p>

---

## ที่นี่คืออะไร?

ในขณะที่โมเดล AI พัฒนาจากแชทบอทธรรมดาไปสู่ **Autonomous Agents** ที่มีความสามารถในการรัน Terminal, ท่องเว็บ และแก้ไข Codebase ความผิดพลาดประเภทใหม่ๆ ก็เริ่มปรากฏขึ้น สิ่งเหล่านี้ไม่ใช่แค่ Syntax Error หรือ Timeout ทั่วไป แต่มันคือ **ความล้มเหลวเชิงสถาปัตยกรรม (Systemic Architectural Failures)**

**Agent Asylum** ทำหน้าที่เป็นฐานข้อมูลบันทึกอุบัติเหตุ (Incident Database) เราไม่ได้แค่รายงานบั๊ก แต่เราวิเคราะห์ว่า *ทำไม* โมเดลที่ฉลาดมากๆ (เช่น GPT-4, Claude 3, Gemini, Devin) ถึงล้มเหลวในงานที่ดูเหมือนจะง่าย เพียงเพราะความซับซ้อนของระบบหรือการขัดกันของ System Prompt

---

## ดัชนีบันทึกเหตุการณ์ (Incident Case Index)

| Case ID | การจัดประเภทอาการ | Agent / LLM | คำอธิบายโดยย่อ | สถานะ |
| :--- | :--- | :--- | :--- | :--- |
| [`001`](../cases/001-simple-task-paradox.md) | Deadlock / Infinite Loop | Google Antigravity | The Simple Task Paradox: เอเจนท์ติดกับดักระหว่างข้อจำกัดด้านประสิทธิภาพและโหมดการทำงานที่ซับซ้อน | แก้ไขแล้ว |

---

## กลไกการป้องกันเชิงเทคนิค (Technical Preventions)

เราไม่ได้แค่บันทึกความล้มเหลว แต่เราจัดเตรียมสคริปต์พื้นฐานเพื่อช่วยนักพัฒนาในการเสริมความแข็งแกร่งให้เอเจนท์ของตน

- **[Circuit Breaker (Python)](../preventions/circuit_breaker.py):** ยูทิลิตี้แบบนับจำนวนเพื่อตรวจจับและหยุดวงจร Tool-calling ที่วนซ้ำ

---

## การร่วมสนับสนุน (Contribute a Case)

หากคุณเคยเห็น AI Agent แสดงพฤติกรรมที่ไม่คาดคิดหรือลูปไม่สิ้นสุดใน Terminal หรือ IDE ของคุณ เราต้องการข้อมูลนั้น!

โปรดอ่าน **[แนวทางการสนับสนุน (Contributing Guidelines)](../CONTRIBUTING.md)** ก่อนส่งรายงาน

1. Fork เรโพนี้
2. ร่างรายงานอุบัติเหตุใหม่โดยใช้ [`TEMPLATE.md`](../TEMPLATE.md)
3. บันทึกไฟล์ในโฟลเดอร์ `cases/`
4. ส่ง Pull Request

---

## พันธกิจของโปรเจค

ด้วยการสร้างแผนที่ของขอบเขตความล้มเหลว (Edge Cases) ในเรื่อง **LLM Tool-Calling Deadlocks** เรามุ่งหวังที่จะมอบชุดข้อมูลที่ดีที่สุดให้กับชุมชน เพื่อสร้าง System Prompt ที่ดีขึ้น, Circuit Breaker ที่แข็งแกร่งขึ้น และโครงสร้าง AI Alignment ที่ทนทานกว่าเดิม
