import os
import re
import html

SOURCE_DIR = "."
TARGET_DIR = "docs"

os.makedirs(TARGET_DIR, exist_ok=True)

def html_to_markdown(text):
    # Decode HTML entities like &nbsp;, &lt;, &gt;
    text = html.unescape(text)

    # Remove the LeetCode H2 title completely (we add our own clean H1 later)
    text = re.sub(r'<h2>.*?</h2>', '', text, flags=re.DOTALL)
    
    # Format the H3 difficulty properly
    text = re.sub(r'<h3>(.*?)</h3>', r'**Difficulty:** \1\n\n', text)

    # Handle <pre> blocks FIRST so we don't convert inner HTML to Markdown
    def replace_pre(match):
        content = match.group(1)
        content = re.sub(r'<.*?>', '', content)  # clean tags inside pre
        return f"\n```text\n{content.strip()}\n```\n"

    text = re.sub(r'<pre>(.*?)</pre>', replace_pre, text, flags=re.DOTALL)

    # Superscript / Subscript (fixes 10^4 becoming 104)
    text = re.sub(r'<sup>(.*?)</sup>', r'^\1', text)
    text = re.sub(r'<sub>(.*?)</sub>', r'_\1', text)

    # Strong / Bold
    text = re.sub(r'<strong.*?>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b.*?>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)

    # Inline code
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
    
    # Emphasis / Italic
    text = re.sub(r'<em.*?>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i.*?>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)

    # Paragraphs -> Newlines
    text = re.sub(r'</?p>', '\n\n', text)

    # Lists
    text = re.sub(r'<li>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)
    text = re.sub(r'</?ul>', '\n\n', text)
    text = re.sub(r'</?ol>', '\n\n', text)

    # Images (convert to markdown format)
    text = re.sub(
        r'<img.*?src="(.*?)".*?>',
        r'![image](\1)',
        text
    )

    # Horizontal Rule
    text = text.replace('<hr>', '\n---\n')

    # Remove any other leftover HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Clean up excessive empty newlines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()

def clean_title(folder_name):
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
        ".java": "java",
        ".js": "javascript",
        ".ts": "typescript"
    }

    for file in os.listdir(folder):
        ext = os.path.splitext(file)[1]
        if ext in EXTENSIONS:
            lang = EXTENSIONS[ext]
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                code = f.read()
            solutions.append((file, code, lang))

    content = f"# {title}\n\n"
    content += "## Problem Statement\n\n"
    content += problem + "\n\n"

    for i, (name, code, lang) in enumerate(solutions):
        content += f"## Solution {i+1} ({name})\n\n"
        content += f"```{lang}\n"
        content += code.strip()
        content += "\n```\n\n"

    filename = title.lower().replace(" ", "-") + ".md"

    with open(os.path.join(TARGET_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)