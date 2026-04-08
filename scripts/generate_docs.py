import os
import re
import html
import json
import urllib.request
import time

SOURCE_DIR = "."
TARGET_DIR = "docs"

os.makedirs(TARGET_DIR, exist_ok=True)

# 1. Load manual overrides (categories.json)
category_map = {}
if os.path.exists("categories.json"):
    with open("categories.json", "r", encoding="utf-8") as f:
        category_map = json.load(f)

# 2. Load API cache (categories_api.json)
api_cache_file = "categories_api.json"
api_cache = {}
if os.path.exists(api_cache_file):
    with open(api_cache_file, "r", encoding="utf-8") as f:
        api_cache = json.load(f)

# 3. Function to ask LeetCode for the category
def fetch_leetcode_category(folder_name):
    match = re.match(r'^\d+-(.*)', folder_name)
    if not match:
        return "Other" 
    
    slug = match.group(1)
    url = "https://leetcode.com/graphql"
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": "query questionData($titleSlug: String!) { question(titleSlug: $titleSlug) { topicTags { name } } }"
    }
    
    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(payload).encode('utf-8'), 
            headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            res = json.loads(response.read().decode())
            tags = res.get("data", {}).get("question", {}).get("topicTags", [])
            if tags:
                return tags[0]["name"]
    except Exception:
        pass 
    
    return "Uncategorized"

def html_to_markdown(text):
    text = html.unescape(text)
    text = re.sub(r'<h2>.*?</h2>', '', text, flags=re.DOTALL)
    text = re.sub(r'<h3>(.*?)</h3>', r'**Difficulty:** \1\n\n', text)

    def replace_pre(match):
        content = match.group(1)
        content = re.sub(r'<.*?>', '', content)
        return f"\n```text\n{content.strip()}\n```\n"

    text = re.sub(r'<pre>(.*?)</pre>', replace_pre, text, flags=re.DOTALL)
    text = re.sub(r'<sup>(.*?)</sup>', r'^\1', text)
    text = re.sub(r'<sub>(.*?)</sub>', r'_\1', text)
    text = re.sub(r'<strong.*?>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<b.*?>(.*?)</b>', r'**\1**', text, flags=re.DOTALL)
    text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
    text = re.sub(r'<em.*?>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'<i.*?>(.*?)</i>', r'*\1*', text, flags=re.DOTALL)
    text = re.sub(r'</?p>', '\n\n', text)
    text = re.sub(r'<li>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL)
    text = re.sub(r'</?ul>', '\n\n', text)
    text = re.sub(r'</?ol>', '\n\n', text)
    text = re.sub(r'<img.*?src="(.*?)".*?>', r'![image](\1)', text)
    text = text.replace('<hr>', '\n---\n')
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def clean_title(folder_name):
    name = re.sub(r'^\d+-', '', folder_name)
    return name.replace('-', ' ').title()

# Track if we made new API calls
cache_updated = False

for folder in os.listdir(SOURCE_DIR):
    if not os.path.isdir(folder) or folder in ["docs", ".github", "scripts", "build", "node_modules"]:
        continue

    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        continue

    title = clean_title(folder)

    with open(readme_path, "r", encoding="utf-8") as f:
        problem = html_to_markdown(f.read())

    solutions = []
    EXTENSIONS = {".py": "python", ".cpp": "cpp", ".java": "java", ".js": "javascript", ".ts": "typescript"}

    for file in os.listdir(folder):
        ext = os.path.splitext(file)[1]
        if ext in EXTENSIONS:
            lang = EXTENSIONS[ext]
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                code = f.read()
            solutions.append((file, code, lang))

    content = f"# {title}\n\n## Problem Statement\n\n{problem}\n\n"
    for i, (name, code, lang) in enumerate(solutions):
        content += f"## Solution {i+1}\n\n```{lang}\n{code.strip()}\n```\n\n"

    filename = title.lower().replace(" ", "-") + ".md"

    # 4. Determine the category!
    if folder in category_map:
        category_path = category_map[folder]
    elif folder in api_cache:
        category_path = api_cache[folder]
    else:
        category_path = fetch_leetcode_category(folder)
        api_cache[folder] = category_path
        cache_updated = True
        time.sleep(0.2) # Polite delay
        
    out_dir = os.path.join(TARGET_DIR, category_path)
    os.makedirs(out_dir, exist_ok=True)
    
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# 5. Save the updated API cache if new problems were found
if cache_updated:
    with open(api_cache_file, "w", encoding="utf-8") as f:
        json.dump(api_cache, f, indent=4)