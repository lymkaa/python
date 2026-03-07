import re
s = input().rstrip("\n")
result = re.sub(r'\d', lambda x: x.group(0) * 2, s)
print(result)