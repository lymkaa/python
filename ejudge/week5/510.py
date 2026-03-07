import re

s = input().rstrip("\n")

print("Yes" if re.search(r'cat|dog', s) else "No")