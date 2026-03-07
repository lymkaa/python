import re
s = input().rstrip("\n")
print("Yes" if re.match(r'^[a-zA-Z].*\d$', s) else "No")
