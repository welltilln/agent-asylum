# Contributing to the Agent Asylum

Thank you for your interest in adding to the archives of architectural psychoses! We believe documenting AI agent failures is the key to building safer aligned systems.

## 🛡️ Ground Rules (The Containment Protocol)

To maintain the integrity of our records and protect our contributors, please adhere to the following:

1. **Sanitize Your Logs [CRITICAL]:** Before submitting *any* logs, terminal output, or code snippets, you **MUST** redact:
   - All API keys, tokens, and secrets (replace with `[REDACTED]`).
   - Personally Identifiable Information (PII) including real names (unless public), usernames, and email addresses.
   - Proprietary codebase logic, private repository URLs, and internal company architecture details.
   - Precise server IP addresses or internal domain names.

2. **Maintain Clinical Objectivity:** We are documenting failures, not roasting AI models. Keep the tone analytical, but feel free to lean into the "clinical/asylum" thematic style.

3. **Follow the Patient Record Format:** Ensure your case study matches the structure outlined in [`cases/templates/patient_record.md`](cases/templates/patient_record.md).

## 📝 How to Submit a New Case

1. **Fork the Repository.**
2. **Create a New Branch:** `git checkout -b patient-record-[short-description]`
3. **Draft the Case:**
   - Copy `cases/templates/patient_record.md`.
   - Rename the file following the format: `cases/XXX-short-description.md` (where `XXX` is the next sequential number).
   - Fill in the sections thoroughly.
4. **Update the Index:** Add a row for your new case in `cases/README.md`.
5. **Commit and Push:** `git commit -m "Add Patient Record XXX"`
6. **Open a Pull Request (PR):** Submit your PR to the `main` branch of this repository.

## 🗣️ Code of Conduct

Be respectful. This is a research community analyzing edge cases in bleeding-edge technology. Debate the architecture, do not attack the contributor.
