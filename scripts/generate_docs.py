import os
import re

SOURCE_DIR = "."
TARGET_DIR = "docs"

os.makedirs(TARGET_DIR, exist_ok=True)

def clean_title(folder_name):
    # remove leading numbers and hyphens
    name = re.sub(r'^\d+-', '', folder_name)
    return name.replace('-', ' ').title()

for folder in os.listdir(SOURCE_DIR):
    if not os.path.isdir(folder):
        continue

    if folder in ["docs", ".github", "scripts"]:
        continue

    readme_path = os.path.join(folder, "README.md")

    if not os.path.exists(readme_path):
        continue

    title = clean_title(folder)

    with open(readme_path, "r", encoding="utf-8") as f:
        problem = f.read()

    solutions = []

    EXTENSIONS = {
    ".py": "python",
    ".cpp": "cpp",
    ".java": "java"
    }

    for file in os.listdir(folder):
        ext = os.path.splitext(file)[1]

        if ext in EXTENSIONS:
            lang = EXTENSIONS[ext]

            with open(os.path.join(folder, file), "r",
                    encoding="utf-8") as f:
                code = f.read()

            solutions.append((file, code, lang))

    content = f"# {title}\n\n"
    content += "## Problem Statement\n\n"
    content += problem + "\n\n"

    for i, (name, code, lang) in enumerate(solutions):
        content += f"## Solution {i+1} ({name})\n\n"
        content += f"```{lang}\n"
        content += code
        content += "\n```\n\n"

    filename = title.lower().replace(" ", "-") + ".md"

    with open(os.path.join(TARGET_DIR, filename),
              "w", encoding="utf-8") as f:
        f.write(content)