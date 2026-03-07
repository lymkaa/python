import re
txt = "This Is A Test Example"
m = re.findall(r"[A-Z][a-z]+", txt)

print("Matches found:", m)