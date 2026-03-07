import re
s = input().rstrip("\n")
p = input().rstrip("\n")

l = re.escape(p)
print(len(re.findall(l, s)))