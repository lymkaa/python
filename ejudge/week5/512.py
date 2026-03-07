import re

s = input().rstrip("\n")

matches = re.findall(r'\d{2,}', s)

print(" ".join(matches))