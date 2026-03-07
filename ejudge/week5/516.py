import re

s = input().rstrip("\n")


match = re.match(r"Name: (.+?), Age: (\d+)", s)

if match:

    print(match.group(1), match.group(2))
else:
    print("No match")