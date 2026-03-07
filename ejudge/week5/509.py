import re

s = input().rstrip("\n")

print(len(re.findall(r'\b\w{3}\b', s)))