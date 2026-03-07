import re

s = input().rstrip("\n")
sub = input().rstrip("\n")

print("Yes" if re.search(re.escape(sub), s) else "No")