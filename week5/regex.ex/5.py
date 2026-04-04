import re

txt = "Ddddjaddeb"
m = re.match(r"^a.*b$", txt)
c = re.match(r".*^a.*b$", txt)

print("Matches found:", m)