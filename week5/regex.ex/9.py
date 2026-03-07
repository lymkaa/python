import re

txt = "ThisIsCamelCase"

res = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)

print("Modified string:", res)