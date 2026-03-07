import re

s = input().rstrip("\n")
pattern = input().rstrip("\n")
replacement = input().rstrip("\n")

print(re.sub(re.escape(pattern), replacement, s))