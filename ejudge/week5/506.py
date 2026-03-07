import re

s = input().rstrip("\n")

match = re.search(r'\S+@\S+\.\S+', s)

print(match.group() if match else "No email")