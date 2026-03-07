import re
txt = "abb"
m = re.match(r"ab{2,3}", txt)

if m:
    print("Match found:", m.group())
else:
    print("No match")