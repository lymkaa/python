import re

s = input().rstrip("\n")

pattern = re.compile(r'^\d+$')

print("Match" if pattern.match(s) else "No match")