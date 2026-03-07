import re

s = input().rstrip("\n")
pattern = input().rstrip("\n")

print(",".join(re.split(pattern, s)))