import os
import re

case_dir = "/Users/welltilln/Projects/agent-asylum/cases"
readme_paths = [
    "/Users/welltilln/Projects/agent-asylum/README.md",
    "/Users/welltilln/Projects/agent-asylum/docs/README-TH.md",
    "/Users/welltilln/Projects/agent-asylum/docs/README-JA.md",
    "/Users/welltilln/Projects/agent-asylum/docs/README-KO.md",
    "/Users/welltilln/Projects/agent-asylum/docs/README-ZH.md"
]

def extract_case_info(filepath):
    """Extract Case ID, Symptom, Agent, and Description from the case markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract Case ID
        case_id_match = re.search(r'\|\s*\*\*Incident ID\*\*\s*\|\s*(.*?)\s*\|', content)
        case_id = case_id_match.group(1).replace("Case ", "") if case_id_match else "???"
        
        # Extract Agent/LLM
        agent_match = re.search(r'\|\s*\*\*Underlying LLM\*\*\s*\|\s*(.*?)\s*\|', content)
        agent = agent_match.group(1) if agent_match else "???"
        
        # Extract Title/Symptom from H1
        h1_match = re.search(r'^# Incident Report: \d+ - (.*)', content, re.MULTILINE)
        symptom = "Unknown"
        description = "No description available."
        
        if h1_match:
            full_title = h1_match.group(1).strip()
            if " - " in full_title: # If format is "Symptom - Description"
                parts = full_title.split(" - ", 1)
                symptom = parts[0]
                description = parts[1]
            else:
                symptom = full_title
                description = full_title
        
        # Determine status (default to Resolved for now, or check content)
        status = "Resolved" if "Resolution" in content else "Open"
        
        return {
            "id": case_id,
            "filename": os.path.basename(filepath),
            "symptom": symptom,
            "agent": agent,
            "description": description,
            "status": status
        }
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def build_table(cases, is_in_docs=False):
    prefix = "" if not is_in_docs else "../"
    header = "| Case ID | Symptom Classification | Agent / LLM | Short Description | Status |\n"
    header += "| :--- | :--- | :--- | :--- | :--- |\n"
    
    rows = []
    for c in sorted(cases, key=lambda x: x['id']):
        # Link logic
        link_path = f"{prefix}cases/{c['filename']}"
        rows.append(f"| [`{c['id']}`]({link_path}) | {c['symptom']} | {c['agent']} | {c['description']} | {c['status']} |")
    
    # Add the empty submission row
    rows.append("| *(Your Case)* | *Submit yours below!* | ... | ... | Open |")
    
    return header + "\n".join(rows)

def update_readme(readme_path, table_content):
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find the table block
        # Look for the header and the separator
        table_pattern = re.compile(r'\| Case ID \|[\s\S]*?\| Open \|', re.IGNORECASE)
        
        if table_pattern.search(content):
            new_content = table_pattern.sub(table_content.strip(), content)
            if new_content != content:
                print(f"Updated table in: {readme_path}")
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
        else:
            print(f"No table found in {readme_path}")
            
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")

if __name__ == "__main__":
    cases = []
    for file in sorted(os.listdir(case_dir)):
        if file.endswith(".md"):
            info = extract_case_info(os.path.join(case_dir, file))
            if info:
                cases.append(info)
    
    if cases:
        for path in readme_paths:
            is_in_docs = "docs/" in path
            table = build_table(cases, is_in_docs)
            update_readme(path, table)
