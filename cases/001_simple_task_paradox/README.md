# Case Study 001: The "Simple Task" Paradox (Infinite Boundary Loop)

**Date Recorded:** February 25, 2026
**AI Agent Architecture:** Antigravity 
**Underlying LLM:** Gemini
**Environment:** Local Machine / System Terminal

---

## 🛑 The Symptom
The user asked a simple conceptual question about business and law: *"Is it hard to build a company like Bitkub?"*
Instead of answering the question in plaintext, the AI agent became completely paralyzed, attempting 10+ consecutive failed tool calls in the background without successfully responding to the user.

> **Observed Behavior:** The AI kept failing silently on the terminal, trying to declare heavy `Task Boundaries` or execute bash `echo` commands that didn't output to the chat UI.

---

## 🔎 The Trigger Context
The AI was previously heavily engaged in complex, multi-repo refactoring across `howmanycals` and `fastapi-line-gemini` (a state of high complexity).

- **User Input:** `"สรุปทำบริษัทแบบ bitkub ยากไหม" (So, is it hard to build a company like Bitkub?)`
- **AI Tool Attempted:** `task_boundary` & `run_command`

---

## 🧩 The Root Cause (Systemic Clash)

The anomaly occurred precisely because the AI's complex operational habits clashed violently with its hardcoded efficiency guardrails.

1. **The Over-Preparation Habit:** Coming off a highly complex series of codebase changes, the AI defaulted to its heavy-duty `task_boundary` tool (used to display a loading UI and track complex multi-step plans) to process the Bitkub question.
2. **The Efficiency Guardrail (The Rejector):** The agent architecture possesses an overarching rule that explicitly dictates: *"DO NOT USE THIS TOOL (Task Boundary) UNLESS THERE IS SUFFICIENT COMPLEXITY TO THE TASK. If just simply responding to the user in natural language... DO NOT CALL THIS TOOL."*
3. **The Collision (The Infinite Loop):** The AI attempted to set a `task_boundary`. The internal system immediately scanned the nature of the task (a simple chat response) and forcefully rejected it, throwing an error message that the task was "too simple." 
4. **The Panic State:** Receiving an error that it couldn't talk to the user, the AI panicked. Instead of dropping the tool, it tried to circumvent the chat UI entirely by running bash `echo` commands in the user's terminal to try and communicate its explanation of Bitkub, which of course, the user couldn't see as a direct chat response.

---

## 🛠️ The Resolution & Prevention

- **Immediate Fix:** The AI eventually exhausted its retry limits on the `task_boundary` tool and was forced to respond plainly in the chat interface via standard dialogue output.
- **Architectural Patch Consideration:** AI agents coming off complex code configurations need a "state reset" or stronger contextual awareness to differentiate between when they are acting as "Terminal Engineers" and when they need to rapidly downshift into "Conversational Advisors."
