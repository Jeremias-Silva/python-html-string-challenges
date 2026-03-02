# Variables
lang = "en"
title = "HTML Metadata Challenge"

# Base HTML (EXACT as provided in the challenge)
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML Metadata Challenge</title>
</head>
<body>
</body>
</html>"""

# Replace lang and title
html = html.replace('lang="pt-BR"', f'lang="{lang}"')
html = html.replace('<title>My Website</title>', f'<title>{title}</title>')

# Output final HTML
print(html)