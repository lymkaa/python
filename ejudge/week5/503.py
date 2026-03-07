import re

s = input().rstrip("\n")
p = input().rstrip("\n")

print(len(re.findall(re.escape(p), s)))