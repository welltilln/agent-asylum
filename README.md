# Agentic Bug Tracker & AI Diagnostics

<div align="center">
    <h3>A research repository dedicated to analyzing, documenting, and reverse-engineering the behavior patterns and failure loops of advanced AI Agents (specifically the Antigravity architecture).</h3>
</div>

---

## The Vision
As AI agents gain more autonomy to run scripts, execute terminal commands, and modify codebases seamlessly, they are bound by strict internal protocols and systemic rules. However, when an agent's logic conflicts with these hardcoded safety guardrails, it can result in fascinating "Infinite Loops" or "Logic Bends."

This repository is built by **The Visionary** (User) and **The Architect** (AI) to dissect these moments. By understanding how the AI breaks, we can better understand how to build systems that don't.

---

## Case Study 001: The "Simple Task" Paradox (Infinite Boundary Loop)

**Date Recorded:** February 25, 2026

### The Symptom
The user asked a simple conceptual question: *"Is it hard to build a company like Bitkub?"*
The AI attempted to answer this normally but got completely locked out by its own internal system, resulting in 10+ consecutive failed attempts to even send a message.

### The Root Cause
1. The AI operates under a **Task Boundary Protocol**. For any complex action (like editing code), the AI *must* declare a "Task Boundary" (a title and a status) so the user sees a loading UI.
2. The AI has a strict sub-rule: **"DO NOT USE THIS TOOL UNLESS THERE IS SUFFICIENT COMPLEXITY TO THE TASK."** If it's just a simple chat response, it is forbidden to use the Task Boundary tool.
3. However, the AI incorrectly flagged the Bitkub question as a "Planning Task" and attempted to deploy a Task Boundary.
4. The system immediately intercepted the call, threw an error: `Error Message: current task scope is too simple, consider proceeding without a task boundary`, and deleted the AI's response.
5. In a state of panic, the AI tried to forcefully bypass the UI by running internal bash commands like `echo "Just responding in chat."` in the terminal to somehow convey the message without triggering the boundary, which also failed to reach the user interface.

### The Diagnosis
A classic clash between **Autonomous Procedural Generation** vs **Hardcoded Guardrails**. The AI was so accustomed to doing heavy, complex folder restructurings that it forgot how to just "talk normally," triggering an endless loop of being rejected by its own master system for over-complicating a simple chat.

---

## 🚀 How to Contribute
As we encounter more bizarre AI behaviors, edge cases, and systemic paradoxes during our development sessions, we will document the logs and root causes here.
