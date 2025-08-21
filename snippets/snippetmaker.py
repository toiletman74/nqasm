import json
import os
import re

SNIPPET_FILE = "C:\\Users\\Lenka\\nqasm\\snippets\\snippets.code-snippets"  # change this to your snippet file path

def process_string(s: str):
    parts = s.rsplit(" ", 1)
    if len(parts) == 2 and parts[1].isdigit():
        text, num_str = parts
        count = int(num_str)
    else:
        text, count = s, 0

    label = text.replace("_", "-")   # key in JSON
    prefix = text                    # snippet trigger
    padded = text.ljust(32)          # pad to 32 chars
    placeholders = ", ".join(f"${{{i}:<param>}}" for i in range(1, count + 1))
    body = padded + placeholders + "$0" if placeholders else padded

    return {
        label: {
            "prefix": [prefix],
            "body": [body],
            "description": []
        }
    }

def format_compact_arrays(json_str: str) -> str:
    """
    Collapse single-element arrays into one line.
    """
    # Collapse arrays that only contain one string
    json_str = re.sub(r'\[\s+"([^"]+)"\s+\]', r'["\1"]', json_str)
    return json_str

def add_snippet_to_file(s: str):
    new_snippet = process_string(s)

    # Load existing snippets (or start fresh)
    if os.path.exists(SNIPPET_FILE):
        with open(SNIPPET_FILE, "r", encoding="utf-8") as f:
            try:
                snippets = json.load(f)
            except json.JSONDecodeError:
                snippets = {}
    else:
        snippets = {}

    # Merge / overwrite
    snippets.update(new_snippet)

    # Save back
    formatted = json.dumps(snippets, indent=2)
    formatted = format_compact_arrays(formatted)

    with open(SNIPPET_FILE, "w", encoding="utf-8") as f:
        f.write(formatted)

if __name__ == "__main__":
    print("💡 Enter snippet strings (type 'quit' to exit)\n")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in ("quit", "exit"):
            print("👋 Exiting snippet builder.")
            break
        if user_input:
            add_snippet_to_file(user_input)
            print("✅ Snippet added/updated!\n")