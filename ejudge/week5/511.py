import re

s = input().rstrip("\n")

print(len(re.findall(r'[A-Z]', s)))