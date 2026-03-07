import re
txt = "abbb"
m = re.match(r"a*b*", txt)

if m:
    print("Match found:", m.group())
else:
    print("No match")