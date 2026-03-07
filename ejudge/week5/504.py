import re

s = input().rstrip("\n")

digits = re.findall(r'\d', s)
print(" ".join(digits))
