import re

txt = "HelloWorldTest"

res = re.findall(r'[A-Z][^A-Z]*', txt)

print("Split string:", res)