import re

txt = "this_is_a_test"
m = re.findall(r"[a-z]+(?:_[a-z]+)*", txt)
print("Matches found:", m)