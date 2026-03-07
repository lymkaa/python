import re

txt = "this_is_a_snake_case_string"

res = re.sub(r"_(.)", lambda x: x.group(1).upper(), txt)
res = res[0].lower() + res[1:]

print("Camel case:", res)