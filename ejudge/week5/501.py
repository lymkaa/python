import re

s = input().rstrip("\n")

print("Yes" if re.match(r"Hello", s) else "No")