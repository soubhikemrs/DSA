import os
import re

SOURCE_DIR = "."
TARGET_DIR = "docs"

os.makedirs(TARGET_DIR, exist_ok=True)

def html_to_markdown(text):
    # ---- Headings ----
    text = re.sub(r'<h2>.*?<a.*?>(.*?)</a>.*?</h2>', r'# \1', text)
    text = re.sub(r'<h3>(.*?)</h3>', r'### \1', text)

    # ---- Bold ----
    text = re.sub(r'<strong.*?>(.*?)</strong>', r'**\1**', text)

    # ---- Inline code ----
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)

    # ---- Paragraphs ----
    text = re.sub(r'<p>', '\n', text)
    text = re.sub(r'</p>', '\n', text)

    # ---- Lists ----
    text = re.sub(r'<li>(.*?)</li>', r'- \1', text)

    # ---- Remove <ul> ----
    text = re.sub(r'</?ul>', '', text)

    # ---- Images (convert to markdown) ----
    text = re.sub(
        r'<img.*?src="(.*?)".*?>',
        r'![image](\1)',
        text
    )

    # ---- Code blocks (<pre>) ----
    def replace_pre(match):
        content = match.group(1)
        content = re.sub(r'<.*?>', '', content)  # clean inside
        return f"\n```text\n{content.strip()}\n```\n"

    text = re.sub(r'<pre>(.*?)</pre>', replace_pre, text, flags=re.DOTALL)

    # ---- Remove <hr> safely ----
    text = text.replace('<hr>', '\n---\n')

    # ---- Remove remaining HTML ----
    text = re.sub(r'<.*?>', '', text)

    # ---- Clean spaces ----
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()

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
        problem = html_to_markdown(f.read())

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