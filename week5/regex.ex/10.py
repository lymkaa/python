import re

txt = "camelCaseStringExample"

res = re.sub(r'([a-z])([A-Z])', r'\1_\2', txt).lower()

print("Snake case:", res)