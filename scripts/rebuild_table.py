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

# Status mapping for localization
STATUS_MAP = {
    "Resolved": {
        "README.md": "Resolved",
        "README-TH.md": "แก้ไขแล้ว",
        "README-JA.md": "解決済み",
        "README-KO.md": "해결됨",
        "README-ZH.md": "已解决"
    },
    "Open": {
        "README.md": "Open",
        "README-TH.md": "เปิดอยู่",
        "README-JA.md": "進行中",
        "README-KO.md": "진행 중",
        "README-ZH.md": "待处理"
    }
}

def extract_case_info(filepath):
    """Extract metadata from the case markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Extract Case ID
        case_id_match = re.search(r'\|\s*\*\*Incident ID\*\*\s*\|\s*(.*?)\s*\|', content)
        case_id = case_id_match.group(1).replace("Case ", "").strip() if case_id_match else "???"
        
        # Extract Agent/LLM
        agent_match = re.search(r'\|\s*\*\*Underlying LLM\*\*\s*\|\s*(.*?)\s*\|', content)
        agent = agent_match.group(1).strip() if agent_match else "???"
        
        # Extract Symptom
        symptom_match = re.search(r'\|\s*\*\*Symptom\*\*\s*\|\s*(.*?)\s*\|', content)
        symptom = symptom_match.group(1).strip() if symptom_match else "Unknown"
        
        # Extract Short Description
        desc_match = re.search(r'\|\s*\*\*Short Description\*\*\s*\|\s*(.*?)\s*\|', content)
        description = desc_match.group(1).strip() if desc_match else "No description available."
        
        # Determine status
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

def build_rows(cases, current_readme_filename, is_in_docs=False):
    prefix = "" if not is_in_docs else "../"
    rows = []
    
    for c in sorted(cases, key=lambda x: x['id']):
        link_path = f"{prefix}cases/{c['filename']}"
        localized_status = STATUS_MAP.get(c['status'], {}).get(current_readme_filename, c['status'])
        
        rows.append(f"| [`{c['id']}`]({link_path}) | {c['symptom']} | {c['agent']} | {c['description']} | {localized_status} |")
    
    # Add submission row (Keep it standard)
    rows.append("| *(Your Case)* | *Submit yours below!* | ... | ... | Open |")
    
    return "\n".join(rows)

def update_readme(readme_path, row_content):
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find content between markers
        marker_pattern = re.compile(
            r'(<!-- CASE_TABLE_ROWS_START -->)[\s\S]*?(<!-- CASE_TABLE_ROWS_END -->)', 
            re.IGNORECASE
        )
        
        if marker_pattern.search(content):
            new_content = marker_pattern.sub(f"\\1\n{row_content}\n\\2", content)
            if new_content != content:
                print(f"Updated case rows in: {readme_path}")
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            else:
                print(f"No changes needed for: {readme_path}")
        else:
            print(f"Markers NOT found in {readme_path}. Skipping.")
            
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")

if __name__ == "__main__":
    cases = []
    if not os.path.exists(case_dir):
        print(f"Error: Case directory {case_dir} not found.")
        exit(1)
        
    for file in sorted(os.listdir(case_dir)):
        if file.endswith(".md"):
            info = extract_case_info(os.path.join(case_dir, file))
            if info:
                cases.append(info)
    
    if cases:
        for path in readme_paths:
            filename = os.path.basename(path)
            is_in_docs = "docs/" in path
            rows = build_rows(cases, filename, is_in_docs)
            update_readme(path, rows)
