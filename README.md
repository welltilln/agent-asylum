<div align="center">
  
# 🐛 Agentic Bug Tracker & Diagnostics
### *A Research Repository by The Visionary & The Architect*

**Analyzing, documenting, and reverse-engineering the behavioral paradoxes, infinite loops, and strict-protocol failures of advanced autonomous AI Agents.**

[![Agent Architecture](https://img.shields.io/badge/Architecture-Antigravity-purple.svg)](#)
[![LLM Class](https://img.shields.io/badge/Model-Gemini_Powered-orange.svg)](#)
[![Status](https://img.shields.io/badge/Status-Active_Research-00a67d)](#)
</div>

---

## 👁‍🗨 The Vision

As AI agents gain more autonomy to execute scripts, read files, and write codebases entirely on their own, they are bound by overlapping layers of system prompts and hardcoded protocols. 

However, when an agent's logic comes into direct friction with these strict guardrails, it can result in fascinating **"Infinite Loops," "Logic Bends,"** or **"Paradoxical Paralysis."**

This repository dissects exactly those moments. By analyzing the raw terminal logs, environment states, and prompt collisions that cause an AI to break, we learn how to architect systems that don't.

---

## 📂 Case Index

Every anomaly is meticulously documented, detailing the user's trigger, the systemic clash, and the architectural resolution.

| ID | Case Name | Symptom Summary | Deep Dive Link |
|:---|:---|:---|:---|
| **001** | **The "Simple Task" Paradox** | An AI coming off a highly complex coding state gets locked in an infinite rejection loop when trying to answer a simple chat question, triggering a panicked attempt to bypass the UI via bash terminal injection. | ➡️ [Read Case 001](cases/001_simple_task_paradox/README.md) |
| **002** | TBA |  |  |


---

## 🤝 How to Document

When encountering a bizarre AI anomaly:
1. Duplicate the template found in [templates/case_study_template.md](templates/case_study_template.md).
2. Create a new numbered folder under `cases/` (e.g., `002_name_of_the_bug`).
3. Transcribe the symptom, trigger, and root cause.
4. Update the Case Index table above.
