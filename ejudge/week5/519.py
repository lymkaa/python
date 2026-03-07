import re

s = input().rstrip("\n")

pattern = re.compile(r'\b\w+\b')
print(len(pattern.findall(s)))